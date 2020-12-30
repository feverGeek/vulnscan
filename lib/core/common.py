import platform
import random
import sys

from urllib.parse import urlparse

from lib.core.enums import EXIT_STATUS
from lib.core.data import logger
from lib.core.exceptions import ToolkitValueException


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


def banner():
    if(platform.system()=='Windows'):
        import colorama
        from colorama import init,Fore,Back,Style
        init(autoreset=True)

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

def systemQuit(status=EXIT_STATUS.SYSETM_EXIT):
    if status == EXIT_STATUS.SYSETM_EXIT:
        logger.info('System exit.')
    elif status == EXIT_STATUS.USER_QUIT:
        logger.error('User quit!')
    elif status == EXIT_STATUS.ERROR_EXIT:
        logger.error('System exit.')
    else:
        raise ToolkitValueException('Invalid status code: %s' % str(status))
    sys.exit(0)

if __name__ == "__main__":
    banner()
