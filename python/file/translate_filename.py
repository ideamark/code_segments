'''
    Only translate file name to English
'''
#coding:utf8
import os
import shutil
import time
import urllib,urllib2,re,sys

reload(sys)
sys.setdefaultencoding('utf-8')

def get_tran(Str):
    header = {'User-Agent':'chrome/28.0'}
    url = 'http://translate.google.cn'

    data = {'sl':'zh-CN','tl':'en','js':'n','prev':'_t','hl':'zh-CN','ie':'UTF-8','text':Str}
    data = urllib.urlencode(data)
    req = urllib2.Request(url,data,header)
    try:
        response = urllib2.urlopen(req).read()
    except Exception,e:
        print e
        sys.exit(1)
    r_tran = re.compile(r'TRANSLATED_TEXT=\'(.+)\';INPUT',re.L)
    return r_tran.findall(response)[0]


if __name__ == '__main__':
    dir = "./"
    if os.path.isdir(dir):
        print ("Directory is exit")
    else:
        print ("Directory is not exit,please input right dir....") 
        time.sleep(5)
        exit()
    filelist = os.listdir(dir)
    for f in filelist:
        suffix = os.path.splitext(str(f))[1][1:]
        if suffix == 'py':
            continue
        NewFile = get_tran(str(f)).replace(' ','_')
        print NewFile
        shutil.move(dir+f, dir+NewFile)
