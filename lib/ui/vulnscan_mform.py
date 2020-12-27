from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore    import pyqtSlot

from lib.ui.vulnscan_ui import Ui_Form
from lib.core.data      import vulnscan_config

class MForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MForm, self).__init__(parent)
        self.setupUi(self)

        # 将配置文件内容显示出来
        # 收录漏洞页显示
        # 设置页显示
        self.threadsLineEdit.setText(vulnscan_config.threads)
        self.timeoutLineEdit.setText(vulnscan_config.timeout)

    @pyqtSlot()
    def on_importPushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_startPushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_importFromFilePushButton_clicked(self):
        pass

    @pyqtSlot()
    def on_applyPushButton_clicked(self):
        print('clicked')