#!/usr/bin/env python
# UDP Client - udpclient.py
# code by www.cppblog.com/jerryma
import socket, sys

HOST = ''
PORT = 8002

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    port = int(PORT)
except ValueError:
    port = socket.getservbyname(PORT, 'udp')
s.connect((HOST, port))

while True:
    print "Enter data to transmit:"
    data = sys.stdin.readline().strip()
    s.sendall(data)
    print "Looking for replies; press Ctrl-C or Ctrl-Break to stop."
    buf = s.recv(2048)
    if not len(buf):
        break
    print "Server replies: ",
    sys.stdout.write(buf)
    print "\n"
