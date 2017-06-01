#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

target_host = "www.google.com"
target_port = 80

# TCP
# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((target_host, target_port))

# sent msg
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# recieve data
response = client.recv(4096)

print(response)

# UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send msg
client.sendto("AAABBBCCC", (target_host, target_port))

# receive msg
data, addr = client.recvfrom(4096)

print(data)
