#coding:utf8
import urllib,urllib2,urlparse
import re,sys
import json
import misc
import random

class tulingbot:
    key = '140b354815e8e3e8319baf5155bad4a8'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    
    def __init__(self):
        pass

    def urlEncodeNonAscii(self,b):
        return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)
    
    def iriToUri(self,iri):
        parts= urlparse.urlparse(iri)
        return urlparse.urlunparse(
            part.encode('idna') if parti==1 else self.urlEncodeNonAscii(part.encode('utf-8'))
            for parti, part in enumerate(parts)
        )
        
    def getHtml(self,url):
        url = self.iriToUri(url)
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
    def response(self,Str):
        if '杨挺' in Str:
            return '我粑粑'
        elif re.match(u'^.*百度(一下|下).*$', Str):
            pat = re.compile(u'^.*百度(一下|下)')
            content = re.sub(pat,'',Str)
            return misc.baiduSearch(content)
        elif re.match(u'^.*用英语怎么说.*$', Str):
            return misc.baiduSearch(Str)
        else:
            request = self.api + Str
            response = self.getHtml(request)
            dic_json = json.loads(response)
            res = dic_json['text'].encode('utf-8')
            return res
