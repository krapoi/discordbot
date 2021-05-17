import json
from urllib.request import urlopen

from requests.api import get

def getTemp():
    response = urlopen("http://hangang.dkserver.wo.tc/").read().decode('utf-8')

    responseJson = json.loads(response)
    return responseJson.get("temp")