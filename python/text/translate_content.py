'''
    Translate the text content to English
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

def tran_content(fn,fi):
    fo = file(fn+'_temp','w')
    print '\n======================'
    print 'File: '+fn
    while True:
        line = fi.readline()
        if len(line) == 0:
            break
        else:  
            print '-----------------------------------------'
            print 'zh: '+ line[:40].replace('\n','') +'......'
            line = get_tran('* '+line)
            print 'en:'+ line[:40].replace('\n','') +'......'
            fo.write(line+'\n')
    fi.close()
    fo.close()

def replace(inName,outName):
    fi = file(inName,'r')
    fo = file(outName,'w')
    while True:
        line = fi.readline()
        if len(line) == 0:
            break
        else:
            line = line.replace('\\x3d','=')
            line = line.replace('\\x3cbr\\x3e','\n')
            line = line.replace('&#160;',' ')
            line = line.replace('\\x26#39;','\'')
            line = line.replace('* * ','* ')
            line = line.replace('*  * ',' * ')
            line = line.replace('* # ','# ')
            line = line.replace('* ## ','## ')
        fo.write(line)
    fi.close()
    fo.close()

if __name__ == '__main__':
    file_list = os.listdir('./')
    for fn in file_list:
        if not os.path.isfile(fn):
            continue
        suffix = os.path.splitext(fn)[1][1:]
        if suffix == 'py' or suffix == 'swp' or suffix == 'png' or suffix == 'jpg':
            continue
        f = file(fn,'r')
        tran_content(fn,f)
        f.close()
        os.remove(fn)
        replace(fn+'_temp',fn)
        os.remove(fn+'_temp')
    print '\nALL Completed!'
