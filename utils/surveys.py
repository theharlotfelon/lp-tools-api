import requests
from .domains import *

def get_cb_auth(account_id,auth_token):
    domain = get_baseURI(account_id, "cbLeIntegrations")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://va.cbleintegrations.liveperson.net/sso/authenticate"
    response = requests.get(url, headers=headers)
    data = response.json()["successResult"]
    return {"organizationId": data["sessionOrganizationId"], "authorization": data["apiAccessToken"]}

def get_cb_surveys(account_id, auth):
    domain = get_baseURI(account_id, "cbBotPlatform")
    headers = {"Authorization": auth["authorization"], "OrganizationId": auth["organizationId"]}
    url = "https://{}/bot-groups/bots?sort-by=botName:asc&page=1&size=5&bot-group=un_assigned".format(domain)
    response = requests.get(url, headers=headers)
    return response.json()["successResult"]["data"]

def check_cb_surveys(surveys, check_skill):
    x = []
    for survey in surveys:
        if survey["skills"]:
            for skill in survey["skills"]:
                if skill["id"] == "{}".format(check_skill):
                    x.append(survey)
    return x


def get_pre_chat_surveys(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadWrite")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/engagement-window/survey-confs?v=2.0".format(
        domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_prechat(surveys, check_skill):
    x = []
    for survey in surveys:
        if survey["json"]["surveyType"] == "Pre-Chat":
            for question in survey["json"]["questions"]["surveyQuestion"]:
                if "type" in question:
                    if question["type"] == "routing_question":
                        for route in question["routingAnswersList"]["routingAnswer"]:
                            if route["skillId"] == "{}".format(check_skill):
                                x.append(survey)
    return x

def get_surveys(account_id, auth_token, check_skill):
    pre_chat_list, cb_chat_list = [], []
    pre_chat_list = check_prechat(get_pre_chat_surveys(account_id, auth_token), check_skill)
    auth = get_cb_auth(account_id, auth_token)
    cb_chat_list = check_cb_surveys(get_cb_surveys(account_id, auth), check_skill)
    return {"chat": pre_chat_list, "messaging": cb_chat_list}

