#!/usr/bin/env python
#coding:utf-8
import re, urllib2

reg = 'fk="\d+\.\d+\.\d+\.\d+" '
url = 'http://www.baidu.com/s?wd=gongwangip'

result = re.search(reg, urllib2.urlopen(url).read()).group(0)
result = re.search('\d+\.\d+\.\d+\.\d+',result).group(0)

print result
