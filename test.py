#!/usr/bin/env python3
from pynnox_api import lennox_thermostat
import pprint
import config

pp = pprint.PrettyPrinter(indent=4)

username = config.username
password = config.password

api = lennox_thermostat(username, password, "C")
api.getSystems()

print("Trying API")

print(api.systems[0]["Gateway_SN"])
api.getInfo("CC14B07685")