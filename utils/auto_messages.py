import requests
from .domains import *

# messaging auto messages
def get_unified_auto_messages(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/engagement-window/unified-auto-messages?v=2.0&view=FILTER_PER_SKILL".format(domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

# chat auto messages
def get_auto_messages(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/engagement-window/auto-messages?v=3.0&view=FILTER_PER_SKILL".format(domain,
                                                                                                         account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_message(list, check_skill):
    x = []
    for item in list:
        if "SKILL" in item["contexts"]:
            for skill in item["contexts"]["SKILL"]:
                if skill["skillId"] == check_skill:
                    x.append(item)
    return x

def get_automatic_messages(account_id, auth_token, check_skill):
    messaging_list = []
    chat_list = []
    messaging_list.append(check_message(get_unified_auto_messages(account_id, auth_token), check_skill))
    chat_list.append(check_message(get_auto_messages(account_id, auth_token), check_skill))
    return {"chat": chat_list, "messaging": messaging_list}

