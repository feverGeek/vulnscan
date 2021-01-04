import os
import time
import threading

from PyQt5.QtCore import QThread

from lib.utils import csv_tools
from lib.utils import output
from lib.core.data import running_config, vulnscan_paths
from lib.core.exploit import Exploit


class Starter(QThread):
    def __init__(self, parent=None):
        super(Starter, self).__init__(parent)

    def run(self):
        from lib.core.start import start_scan
        start_scan() 

def start_scan():
    print("扫描开始")
    output.prt('running_config', running_config)
    e = Exploit(running_config.urls, running_config.plugins, running_config.threads)
    e.run()

    csv_filename = time.strftime("%Y-%m-%d-%H-%M-%S.csv", time.localtime())
    csv_filename = os.path.join(vulnscan_paths['vulnscan_results_path'], csv_filename)
    # ID Url Script Vuln Type Request
    header = ['ID', '网站地址', '脚本', '漏洞信息', '请求类型', '请求包']
    output.prt('扫描结果')
    output.result_prt(e.results)
    csv_tools.csv_generate(csv_filename, header, e.results)

    output.prt('扫描结束')