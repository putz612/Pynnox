#!/usr/bin/env python3
from pynnox_api import lennox_thermostat

import config

username = config.username
password = config.password

api = lennox_thermostat(username, password, 0, 0)
api.get()