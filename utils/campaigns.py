import requests
from .domains import *

def get_campaign(account_id, auth_token, campaign):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/le-campaigns/campaigns/{}?v=3.4".format(domain, account_id, campaign)
    response = requests.get(url, headers=headers)
    return response.json()

def get_campaigns(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/le-campaigns/campaigns?v=3.4".format(domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

# check engagements for skill assignment
def get_engagements(account_id, auth_token, check_skill):
    campaign_list = []
    engagement_list = []
    campaigns = get_campaigns(account_id, auth_token)
    for item in campaigns:
        campaign_list.append(item["id"])
    for campaign in campaign_list:
        data = get_campaign(account_id, auth_token, campaign)
        list = []
        if data["engagements"]:
            for engagement in data["engagements"]:
                if "skillId" in engagement and engagement["skillId"] == check_skill:
                    engagement.pop("displayInstances")
                    list.append(engagement)
            if list:
                engagement_list.append(
                    {"id": data["id"], "name": data["name"], "type": data["type"], "engagements": list})
    return engagement_list