#!/usr/bin/env python3
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

#password = getpass()
password = "cisco123!"
user     = "cisco"
host     = "192.168.56.102"
cisco1 = {
    "host": host,
    "username": user,
    "password": password,
    "device_type": "cisco_ios",
    "command": "show ip int brief",
}

#Note that this is a sandboxed Router on DevNet
arista1 = {
    "host": 'sbx-nxos-mgmt.cisco.com',
    "username": 'admin',
    "password": 'Admin_1234!',
    "device_type": "cisco_ios",
    "command": "show ip int brief",
}

srx1 = {
    "host": host,
    "username": user,
    "password": password,
    "device_type": "cisco_ios",
     "command": "show ip interface brief",
}

for device in (cisco1, arista1, srx1):
    command = device.pop("command")
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    print()
    print("-" * 80)
    print("{}: {}".format(device["host"], device["device_type"]))
    print(output)
    print("-" * 80)
    print()
