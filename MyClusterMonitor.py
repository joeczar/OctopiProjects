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

ipAddresses = []

# Clean data 
for el in data:
    ip = el.replace('\n', '')
    if ip != '192.168.1.1' and ip!= '':
        ipAddresses.append(ip)

# Ping ips & get hostnames
#Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
for idx, ip in enumerate(ipAddresses):
    # ping each address
    rep = os.system('ping -c 1 ' + ip)
    if rep == 0:
        print(ip, ' is up')
        try:
            #clear()
            set_pixel(idx, 0, 0, 255)
            show()
        except:
            print('Error')
    else:
        print(ip, ' is down')
clear()
show()
# Check servers for ssh keys. (Adapted from - https://support.sciencelogic.com/s/article/1440)
k = paramiko.RSAKey.from_private_key_file("/home/pi/.ssh/id_rsa")
c = paramiko.SSHClient()

for idx, ip in enumerate(ipAddresses):
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print( "connecting to ", ip)
    try:
        c.connect( ip, username ="pi", pkey = k )
        try:
            clear()
            set_pixel(idx, 0, 128, 0)
            show()
        except:
            print('Error')
        print("connected to ", ip)
        commands = [ "hostname", "w" ]
        for command in commands:
            print( "Executing {}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print( stdout.read())
            print( "Errors")
            print( stderr.read())
        c.close()
    except:
        print("Could not connect to ", ip)

# print(ipAddresses)