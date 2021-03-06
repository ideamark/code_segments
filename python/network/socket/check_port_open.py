#!/usr/bin/env python3
import socket

def is_open(ip, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print('%d is open' % port)
        return True
    except:
        print('%d is down' % port)
        return False

if __name__ == '__main__':
    is_open('127.0.0.1',80)
