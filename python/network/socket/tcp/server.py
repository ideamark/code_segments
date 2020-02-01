#!/usr/bin/env python
#coding:utf-8
import socket
import time

HOST = ''
PORT = 1080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

while True:
    thistime=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
    try:
        connection,address = sock.accept()
        connection.settimeout(5)
        buf = connection.recv(1024)
        print (thistime+"receive: "+buf+"")
        connection.send(thistime+':'+res)
    except socket.timeout:
        print 'time out'
    connection.close()
