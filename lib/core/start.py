from lib.core.data import running_config
from lib.core.exploit import exploit

def start_scan():
    print("扫描开始")
    exploit(running_config.urls, running_config.plugins, running_config.threads).run()