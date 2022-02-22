#!/usr/bin/env python3
"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

#try:
#    host = raw_input("Enter host to connect to: ")
#except NameError:
#    host = input("Enter host to connect to: ")

#password = getpass()
device = {
    "host": "192.168.56.102",
    "username": "cisco",
    "password": "cisco123!",
    "device_type": "cisco_ios",
}

command = "show ip int brief"
net_connect = Netmiko(**device)
output = net_connect.send_command(command)
print()
print("-" * 80)
print(output)
print("-" * 80)
print()
