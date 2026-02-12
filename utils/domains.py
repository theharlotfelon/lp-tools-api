import requests

def get_baseURI(account_id, service_name):
    url = "https://api.liveperson.net/api/account/{}/service/{}/baseURI.json?version=1.0".format(account_id, service_name)
    response = requests.get(url)
    return response.json()["baseURI"]