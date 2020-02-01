# encoding: utf-8
# this python script can rename all the files in the folder.
import os
import shutil
import time

dir = "./"

if os.path.isdir(dir):
    print ("Directory is exit")
else:
    print ("Directory is not exit,please input right dir....") 
    time.sleep(5)
    exit()

filelist = os.listdir(dir)

for f in filelist:
    if str(f) == 'rename.py':
        continue
    NewFile = f.replace("0","")   
    print NewFile
    shutil.move(dir+f, dir+NewFile)
