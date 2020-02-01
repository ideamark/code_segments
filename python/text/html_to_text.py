'''
This script is used to convert HTML files in current folder to Text
'''

import os
import shutil
import time
import re
from HTMLParser import HTMLParser 
from re import sub 
from sys import stderr 
from traceback import print_exc 
 
class _DeHTMLParser(HTMLParser): 
    def __init__(self): 
        HTMLParser.__init__(self) 
        self.__text = [] 
 
    def handle_data(self, data): 
        text = data.strip() 
        if len(text) > 0: 
            text = sub('[ \t\r\n]+', ' ', text) 
            self.__text.append(text + ' ') 
 
    def handle_starttag(self, tag, attrs): 
        if tag == 'p': 
            self.__text.append('\n\n') 
        elif tag == 'br': 
            self.__text.append('\n') 
 
    def handle_startendtag(self, tag, attrs): 
        if tag == 'br': 
            self.__text.append('\n\n') 
 
    def text(self): 
        return ''.join(self.__text).strip() 
 
 
def dehtml(text): 
    try: 
        parser = _DeHTMLParser() 
        parser.feed(text) 
        parser.close() 
        return parser.text() 
    except: 
        print_exc(file=stderr) 
        return text 
 
 
if __name__ == '__main__': 
    dir = './'
    if not os.path.isdir(dir+'output'):
        os.mkdir('output')
    filelist = os.listdir(dir)
    for f in filelist:
        if re.match('.*\.(html|htm)$',f):
            print 'converting '+f+'...'
            fi = open(f,'r')
            fo = open('output/'+f.replace('.html','').replace('.htm',''),'w')
            lines = fi.readlines()
            for line in lines:
                fo.write(dehtml(line))
            fi.close()
            fo.close()