import threading
import time

from PyQt5.QtCore import QThread

from lib.core.data import running_config
from lib.core.exploit import Exploit


class Starter(QThread):
    def __init__(self, parent=None):
        super(Starter, self).__init__(parent)

    def run(self):
        from lib.core.start import start_scan
        start_scan() 

def start_scan():
    print("扫描开始")
    Exploit(running_config.urls, running_config.plugins, running_config.threads).run()
    print('扫描结束')
