
import requests
from requests.auth import HTTPBasicAuth
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)


class lennox_thermostat():
    """Some cool description here"""
    def __init__(self, username, password):
        self._name = 'lennox'
        self._username = username
        self._password = password
        self.systems = "Unknown"
        self._system = system
        self._zone = zone
        self._serialNumber = "Unknown"
        self._baseURL = "https://services.myicomfort.com/DBAcessService.svc/"


    def get(self):
        systemInfo = requests.get(self._baseURL + "GetSystemsInfo?UserId=" + self._username, auth=HTTPBasicAuth(self._username, self._password))
        pp.pprint( systemInfo.json())
    def getSystems(self):
        systemInfo = requests.get(self._baseURL + "GetSystemsInfo?UserId=" + self._username, auth=HTTPBasicAuth(self._username, self._password))
        systems = systemInfo.json()
        pp.pprint( systems["Systems"])
        self.systems = systems["Systems"]