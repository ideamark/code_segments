#!/usr/bin/env python3
"""
 This script used to resize image
 Command format(resize to 50%): python3 resize.py xxx.jpg 50
"""
from PIL import Image  
import os, sys

if __name__=='__main__':  
    im = Image.open(sys.argv[1])
    percent = int(sys.argv[2]) / 100
    w,h = im.size  
    im_ss = im.resize((int(w*percent), int(h*percent)))  
    im_ss.save('out.jpg') 
