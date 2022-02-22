#!/usr/bin/env python3
"""
Find a command on your device that has additional prompting. Use send_command_timing to send the
command down the SSH channel. Capture the output and handle the additional prompting.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
#from getpass import getpass
#
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

filename = "smallfile"
command = "delete flash:{}".format(filename)

net_connect = Netmiko(**device)
output = net_connect.send_command_timing(
    command, strip_prompt=False, strip_command=False
)

#print (output)

if "?" in output:
    output += net_connect.send_command_timing(
        "smallfile", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
    #empty string confirms delete
    #   "", strip_prompt=F#alse, strip_command=False
    # I don't confirm the file delete.
        "n", strip_prompt=False, strip_command=False
    )
else:
    raise ValueError("Expected confirm message in output")

print()
print("-" * 80)
print(output)
print("-" * 80)
print()
