# 返回请求包
def make_request_package(request):
    line1 = f"{request.method} {request.path_url} HTTP/1.1\n"
    host = f"Host: {request.url.replace('https://','').replace('http://','').replace(request.path_url, '')}\n"
    headers = ""
    for k, v in request.headers.items():
        headers += f"{k}: {v}\n"
    body = f""
    if request.body:
        body = f"{request.body}\n"
    package = line1 + host + headers + body

    # print(package)
    return package
