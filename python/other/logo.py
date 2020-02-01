#!/usr/bin/python
import os,time

while True:
    for i in range(3,29):
        if i == 9 or i == 10:
            continue
        os.system('linuxlogo -f -L '+ str(i))
        time.sleep(0.5)
