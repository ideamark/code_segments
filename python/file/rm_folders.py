# encoding: utf-8
import os
import shutil
import time
import re


for root, dirs, files in os.walk("./"):
    for dir in dirs:
        if dir == '使用说明':
            path = os.path.join(root, dir)
            shutil.rmtree(path)
            print('removed dir %s' % path)
