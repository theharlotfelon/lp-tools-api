import requests
from .domains import *

def get_users(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/le-users/users?v=6&select=id,loginName,fullName,skillIds".format(domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_users(account_id, auth_token, check_skill):
    user_list = []
    users = get_users(account_id, auth_token)
    for user in users:
        if check_skill in user["skillIds"]:
            user_list.append(user)
    return user_list