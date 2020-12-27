import random
from urllib.parse import urlparse

VERSION = '0.1.0'
AUTHOR = 'zeta'


banner_0 = """\033[01;34m
██╗   ██╗    ██╗   ██╗    ██╗         ███╗   ██╗    ███████╗     ██████╗     █████╗     ███╗   ██╗
██║   ██║    ██║   ██║    ██║         ████╗  ██║    ██╔════╝    ██╔════╝    ██╔══██╗    ████╗  ██║
██║   ██║    ██║   ██║    ██║         ██╔██╗ ██║    ███████╗    ██║         ███████║    ██╔██╗ ██║
╚██╗ ██╔╝    ██║   ██║    ██║         ██║╚██╗██║    ╚════██║    ██║         ██╔══██║    ██║╚██╗██║
 ╚████╔╝     ╚██████╔╝    ███████╗    ██║ ╚████║    ███████║    ╚██████╗    ██║  ██║    ██║ ╚████║
  ╚═══╝       ╚═════╝     ╚══════╝    ╚═╝  ╚═══╝    ╚══════╝     ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝
\033[01;37m{ \033[01;m Version %s by %s   \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR)

banner_1 = """\033[01;34m
 _____________________________
< vulnscan Version:%s by %s >
 -----------------------------\033[0m
     \033[01;31m\\
      \033[01;33m\\\033[0m
          oO)-.                       .-(Oo
         /__  _\                     /_  __\\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '

""" % (VERSION, AUTHOR)

banner_2 = """\033[01;34m
 _____________________________
< vulnscan Version:%s by %s >
 -----------------------------\033[0m
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||

""" % (VERSION, AUTHOR)

banner_3 = """\033[01;34m
_____________________________
< vulnscan Version:%s by %s >
-----------------------------\033[0m
  \033[01;31m\\
    \033[01;33m\\\033[0m
      .--.
     |o_o |
     |:_/ |
    //   \ \\
   (|     | )
   /'\_   _/`\\
   \___)=(___/

""" % (VERSION, AUTHOR)

banners = [banner_0, banner_1, banner_2, banner_3]


def Banner():
    _ = banners[random.randint(0, 3)]
    print(_)

def makeurl(url):
    prox = "http://"
    if (url.startswith("https://")):
        prox = "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        url = prox + url
    url_info = urlparse(url)

    if url_info.path:
        url = prox + url_info.netloc + url_info.path
        if not url.endswith("/"):
            url = url + "/"
    else:
        url = prox + url_info.netloc + "/"
    return url

if __name__ == "__main__":
    url = makeurl("httpwww.baidu.com") 
    print(url)
