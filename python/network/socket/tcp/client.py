#!/usr/bin/env python
#coding:utf-8
import socket

HOST = ''
PORT = 1080

while True:
    temp=raw_input('input: ')
    if temp=="exit":
        break
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    strd=temp+""
    s.connect((HOST, PORT))
    s.send(strd+"")
    data = s.recv(1024)
    print data
    s.close()
