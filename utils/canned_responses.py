import requests
from .domains import *

def get_canned_responses(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/engagement-window/canned-responses?v=2.0&select=id,enabled,skillIds,categoriesIds,templateId,data(lang,title)".format(domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_canned_responses(account_id, auth_token, check_skill):
    canned_list = []
    canned_responses = get_canned_responses(account_id, auth_token)
    for canned_response in canned_responses:
        if "skillIds" in canned_response:
            if check_skill in canned_response["skillIds"]:
                canned_list.append(canned_response)
    return canned_list