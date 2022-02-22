#!/usr/bin/env python3
"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
"""

from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

import os
os.environ["NET_TEMPLATES_DIR"] = "/home/devasc/ntc-templates"
os.environ["NET_TEXTFSM"]  = "/home/devasc/ntc-templates/ntc_templates/templates"

#try:
#    host = raw_input("Enter host to connect to: ")
#except NameError:
#    host = input("Enter host to connect to: ")
#
#password = getpass()
device = {
    "host": "192.168.56.102",
    "username": "cisco",
    "password": "cisco123!",
    "device_type": "cisco_ios",
}

command = "show ip int brief"
net_connect = Netmiko(**device)
output = net_connect.send_command(command, use_textfsm=True)
print()
print(type(output))
print("-" * 80)
pprint(output)
print("-" * 80)
print()

print (output[0]["intf"], output[1]["intf"], output[2]["intf"])
print (output[0]["ipaddr"], output[1]["ipaddr"], output[2]["ipaddr"])
print (output[0]["status"], output[1]["status"], output[2]["status"])
