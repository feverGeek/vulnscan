from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore    import pyqtSlot

from lib.core.data        import vulnscan_config, running_config
from lib.core.common      import makeurl
from lib.ui.vulnscan_ui   import Ui_Form
from lib.utils.configfile import checkFile

class MForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MForm, self).__init__(parent)
        self.setupUi(self)

        # 将配置文件内容显示出来
        # 收录漏洞页显示
        plugins_count = len(running_config.plugins)
        for row in range(plugins_count):
            self.vulnsTableWidget.insertRow(row)
            item = QTableWidgetItem('%s' % (row + 1))
            self.vulnsTableWidget.setItem(row, 0, item)
            item = QTableWidgetItem('%s' % running_config.plugins[row])
            self.vulnsTableWidget.setItem(row, 1, item)

        # 设置页显示
        self.threadsLineEdit.setText(str(vulnscan_config.threads))
        self.timeoutLineEdit.setText(str(vulnscan_config.TimeOut))
        self.userAgentLineEdit.setText(vulnscan_config.UserAgent)
        self.cookieLineEdit.setText(vulnscan_config.Cookie)

    @pyqtSlot()
    def on_importPushButton_clicked(self):
        row = self.urlsTableWidget.rowCount()

        self.urlsTableWidget.insertRow(row)
        item = QTableWidgetItem('%s' % (row + 1))
        self.urlsTableWidget.setItem(row, 0, item)

        url = self.urlLineEdit.text()
        item = QTableWidgetItem('%s' % url)
        self.urlsTableWidget.setItem(row, 1, item)

    @pyqtSlot()
    def on_startPushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_importFromFilePushButton_clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "choose file", "", "*.txt")
        if not filename:
            return

        running_config.multiurl = True
        checkFile(filename)
        with open(filename, 'r') as fd:
            contents = fd.readlines()
            for _ in contents:
                running_config.urls.append(makeurl(_.strip()))
        print(running_config.urls)

        for row in range(self.urlsTableWidget.rowCount()):
            self.urlsTableWidget.removeRow(0)

        urls_count = len(running_config.urls)
        for row in range(urls_count):
            self.urlsTableWidget.insertRow(row)
            item = QTableWidgetItem('%s' % (row + 1))
            self.urlsTableWidget.setItem(row, 0, item)

            url = running_config.urls[row]
            item = QTableWidgetItem('%s' % url)
            self.urlsTableWidget.setItem(row, 1, item)


    @pyqtSlot()
    def on_applyPushButton_clicked(self):
        print('clicked')