import requests
from .domains import *

def get_skills(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/le-users/skills?select=$all".format(domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_skills(account_id, auth_token, check_skill):
    skills = get_skills(account_id, auth_token)
    skill_list = []
    for skill in skills:
        if "skillTransferList" in skill:
            if check_skill in skill["skillTransferList"]:
                skill_list.append(skill)
    return skill_list