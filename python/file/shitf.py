# encoding: utf-8
# shitf the files to the upper folder
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

folderList = os.listdir(dir)

for folder in folderList:
    if os.path.isfile(folder):
        continue
    fileList = os.listdir(dir+folder+'/')    
    for f in fileList:
        os.system('mv '+dir+folder.replace(' ','\ ')+'/'+f.replace(' ','\ ')+' '+dir+folder.replace(' ','_')+'__'+f.replace(' ','_'))
    if not os.listdir(dir+folder):
        os.system('rm -r '+dir+folder.replace(' ','\ '))
