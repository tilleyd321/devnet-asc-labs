#!/usr/bin/env python3
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass


password = "cisco123!"
user     = "cisco"
host     = "192.168.56.102"

cisco1 = {
    "host": host,
    "username": user,
    "password": password,
    "device_type": "cisco_ios"
}

def checkNTP():
    print("Checking if NTP is already configured")
    net_connect = Netmiko(**cisco1)
    output = net_connect.send_command('show ntp associations')
    print()
    print("-" * 80)
    print("{}: {}".format(cisco1["host"], cisco1["device_type"]))
    if output == '':
        retVal = False
        print("NTP SERVER NOT CONFIGURED")
    else:
        retVal = True
        print(output)
    print("-" * 80)
    print()
    return retVal;

def setNTP(ntpServers):
    print("Configuring NTP")
    net_connect = Netmiko(**cisco1)
    
    cfg_commands = []
    
    for ntpServer in  ntpServers:
        ntp_command = "ntp server " + ntpServer
        cfg_commands.append(ntp_command)

    output_ntp = net_connect.send_config_set(cfg_commands)
    print(output_ntp)

def cfgNTP():
    if (checkNTP() == False ):
        print("Setting NTP Server")
        setNTP(('123.0.0.1','123.0.0.2'))
    else:
        print("NTP is already configured leaving untouched")


print("Running")
cfgNTP()

