#!/usr/bin/env python
import os
import time
import socket
import sys
import paramiko
from blinkt import set_brightness, set_pixel, show, clear

# clear the LEDs
set_brightness(0.1)
clear()
show()

# Read ip_list and store ip's in list

file = open('/home/pi/ip_list', 'r')
data = file.readlines()
file.close()

ipAddresses = {}

# Clean data
for idx, el in enumerate(data):
    ip = el.replace('\n', '')
    if ip != '192.168.1.1' and ip != '':
        ipAddresses[idx] = ip

# Ping ips & get hostnames
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for idx in ipAddresses:
    ip = ipAddresses[idx]
    # ping each address
    rep = os.system('ping -c 1 ' + ip)
    if rep == 0:
        ipAddresses[idx] = {"ip": ip}
        ipAddresses[idx]["ping"] = True

        # clear()
        set_pixel(idx, 0, 0, 50)
        show()

    else:
        ipAddresses[idx] = {"ip": ip}
        ipAddresses[idx]["ping"] = False


clear()
show()
# Check servers for ssh keys. (Adapted from - https://support.sciencelogic.com/s/article/1440)
k = paramiko.RSAKey.from_private_key_file("/home/pi/.ssh/id_rsa")
c = paramiko.SSHClient()

while True:
    for idx in ipAddresses:
        ip = ipAddresses[idx].get("ip")

        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            c.connect(ip, username="pi", pkey=k)

            clear()
            set_pixel(idx - 1, 0, 50, 0)
            show()

            print(idx, "connected to ", ip)
            commands = ["python3 blinktAnswer.py all 0 0 128"]
            for command in commands:

                stdin, stdout, stderr = c.exec_command(command)

            c.close()
            ipAddresses[idx]["ssh"] = True
        except:
            ipAddresses[idx]["ssh"] = False

            clear()
            set_pixel(idx - 1, 128, 0, 0)
            show()
    time.sleep(2)
