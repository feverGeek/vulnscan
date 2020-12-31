import time
import threading

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QObject, QThread
from PyQt5.QtCore import Qt

from lib.core import data
from lib.core.start import Starter
from lib.core.data import vulnscan_config, running_config
from lib.core.common import makeurl
from lib.core.option import register_plugins
from lib.ui.vulnscan_ui import Ui_Form
from lib.utils.configfile import checkFile, modifyConfigFile

class MForm(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(MForm, self).__init__(parent)
        self.setupUi(self)

        self.scan_thread = Starter()
        self.scan_thread.finished.connect(self.finish_slot)

        # 设置页显示
        self.threadsLineEdit.setText(str(vulnscan_config.threads))
        self.timeoutLineEdit.setText(str(vulnscan_config.TimeOut))
        self.userAgentLineEdit.setText(vulnscan_config.UserAgent)
        self.cookieLineEdit.setText(vulnscan_config.Cookie)

    @pyqtSlot()
    def on_importPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        url = self.urlLineEdit.text()
        if not url:
            self.showdialog('警告', 'URL不能为空')
            return

        row = self.urlsTableWidget.rowCount()

        self.urlsTableWidget.insertRow(row)
        item = QTableWidgetItem('%s' % (row + 1))
        self.urlsTableWidget.setItem(row, 0, item)

        item = QTableWidgetItem('%s' % makeurl(url))
        self.urlsTableWidget.setItem(row, 1, item)

    @pyqtSlot()
    def on_startPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        running_config.urls = []
        running_config.plugins = []
        if not self.urlsTableWidget.rowCount():
            self.showdialog('警告', 'URL不能为空')
            return
        
        if not self.vulnsTableWidget.rowCount():
            self.showdialog('警告', '插件不能为空')
            return
        
        # 注册url
        row_count = self.urlsTableWidget.rowCount()
        for r in range(row_count):
            url = self.urlsTableWidget.item(r, 1).text()
            running_config.urls.append(url)
        
        # 注册插件
        plugins = []
        row_count = self.vulnsTableWidget.rowCount()
        for r in range(row_count):
            plugin = self.vulnsTableWidget.item(r, 1).text()
            plugins.append(plugin) 
        register_plugins(plugins)

        self.scan_thread.start()
        self.scanInfoLabel.setText('扫描信息: 扫描开始, 请等待...')

    @pyqtSlot()
    def on_stopScanPushButton_clicked(self):
        pass 

    @pyqtSlot()
    def on_importFromFilePushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        filename, filetype = QFileDialog.getOpenFileName(
            self, "choose file", "", "*.txt")
        if not filename:
            return

        running_config.multiurl = True
        checkFile(filename)
        with open(filename, 'r') as fd:
            contents = fd.readlines()
            urls_count = len(contents)
            offset = self.urlsTableWidget.rowCount()
            for row in range(urls_count):
                self.urlsTableWidget.insertRow(offset + row)
                item = QTableWidgetItem('%s' % (offset + row + 1))
                self.urlsTableWidget.setItem(offset + row, 0, item)

                item = QTableWidgetItem('%s' % makeurl(contents[row].strip()))
                self.urlsTableWidget.setItem(offset + row, 1, item)
        
    @pyqtSlot()
    def on_clearPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        for row in range(self.urlsTableWidget.rowCount()):
            self.urlsTableWidget.removeRow(0)
        running_config.urls = []

    @pyqtSlot()
    def on_importPluginPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        plugin = self.pluginsLineEdit.text()
        if not plugin:
            self.showdialog('警告', '插件不能为空')
            return

        if plugin not in data.all_plugins:
            self.showdialog('警告', f'不存在{plugin}')
            return

        row = self.vulnsTableWidget.rowCount()

        self.vulnsTableWidget.insertRow(row)
        item = QTableWidgetItem('%s' % (row + 1))
        self.vulnsTableWidget.setItem(row, 0, item)

        item = QTableWidgetItem('%s' % plugin)
        self.vulnsTableWidget.setItem(row, 1, item)

    @pyqtSlot()
    def on_clearPluginsPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        for row in range(self.vulnsTableWidget.rowCount()):
            self.vulnsTableWidget.removeRow(0)
        running_config.plugins = []

    @pyqtSlot()
    def on_applyPushButton_clicked(self):
        if threading.active_count() > 1:
            self.showdialog('警告', '正在扫描')
            return

        threads = self.threadsLineEdit.text()
        timeout = self.timeoutLineEdit.text()
        useragent = self.userAgentLineEdit.text()
        cookie = self.cookieLineEdit.text()
        if not threads or not timeout:
            self.showdialog('警告', '线程数和超时时间不能为空')
            return

        try:
            d = {
                'Config': {
                    'threads': int(threads),
                    'TimeOut': int(timeout),
                    'UserAgent': useragent,
                    'Cookie': cookie
                }
            }
            modifyConfigFile('config.conf', d)
            running_config.threads = vulnscan_config.threads
            if running_config.threads is None:
                running_config.threads = 10
            running_config.threads = int(running_config.threads)


            running_config.timeout = vulnscan_config.TimeOut
            if running_config.timeout is None:
                running_config.timeout = 10
            running_config.timeout = int(running_config.timeout)
            # print(vulnscan_config)
            # print(running_config)
        except ValueError:
            self.showdialog('警告', '线程数和超时时间为非法字符')
            return
        
    def showdialog(self, title, content):
        msg_box = QMessageBox(QMessageBox.Information, title, content)
        msg_box.exec_()

    def finish_slot(self):
        self.scanInfoLabel.setText('扫描信息: 扫描结束')

    # TODO: 加入中止扫描按键

