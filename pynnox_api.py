
import requests
from requests.auth import HTTPBasicAuth
import json

class lennox_thermostat():
    """Some cool description here"""
    def __init__(self, username, password, system, zone):
        self._name = 'lennox'
        self._username = username
        self._password = password
        
        self._system = system
        self._zone = zone
        self._serialNumber = "Unknown"

    def get(self):
        url = "https://services.myicomfort.com/DBAcessService.svc/"
        systemInfo = requests.get(url + "GetSystemsInfo?UserId=" + self._username, auth=HTTPBasicAuth(self._username, self._password))
        print ( systemInfo.text)