# encoding: utf-8
# this python script can rename all the files in the folder.
import os
import shutil
import time
import re


for root, dirs, files in os.walk("./"):
    for old_file in files:
        if old_file == 'rename.py':
            continue
        new_file = old_file.replace("old","new")   
        print(new_file)
        shutil.move(os.path.join(root, old_file), os.path.join(root, new_file))
