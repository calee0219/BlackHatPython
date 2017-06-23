#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

target_host = "www.vnu.edu.tw"
target_port = 80

# TCP
print("TCP connector")
# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((target_host, target_port))

# sent msg
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

# recieve data
response = client.recv(4096)

print(response)

# UDP
print("")
print("UDP connector")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send msg
client.sendto("AAABBBCCC".encode(), (target_host, target_port))

# receive msg
data, addr = client.recvfrom(4096)

print(data)
