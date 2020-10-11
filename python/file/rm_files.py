# encoding: utf-8
import os
import re


for root, dirs, files in os.walk("./"):
    for file in files:
        if re.match(r'.*\.rar', file):
            path = os.path.join(root, file)
            os.remove(path)
            print('removed file %s' % path)
