#!/usr/bin/env python
import os
import time
import socket
import sys
from blinkt import set_brightness, set_pixel, show, clear

# clear the LEDs
set_brightness(0.1)
clear()
show()

# Read ip_list and store ip's in list

file = open('/home/pi/ip_list', 'r')
data = file.readlines()
file.close()

ipAddresses = []

# Clean data 
for el in data:
    ip = el.replace('\n', '')
    if ip != '192.168.1.1' and ip!= '':
        ipAddresses.append(ip)

# Ping ips
#Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
for ip in ipAddresses:
    rep = os.system('ping -c 1 ' + ip)
    if rep == 0:
        print(ip + ' is up')
    else:
        print(ip + ' is down')

# Get hostnames

for ip in ipAddresses:
    hostname = socket.getfqdn(ip)
    print(hostname)


print(ipAddresses)