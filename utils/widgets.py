import requests
from .domains import *

def get_widgets(account_id, auth_token):
    domain = get_baseURI(account_id, "accountConfigReadOnly")
    headers = {"Authorization": "Bearer {}".format(auth_token)}
    url = "https://{}/api/account/{}/configuration/le-ui-personalization/widgets?v=2.0&select=$all".format(
        domain, account_id)
    response = requests.get(url, headers=headers)
    return response.json()

def check_widgets(account_id, auth_token, check_skills):
    widget_list = []
    widgets = get_widgets(account_id, auth_token)
    for widget in widgets:
        if check_skills in widget["skillIds"]:
            widget_list.append(widget)
    return widget_list