from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtGui     import QStandardItem, QStandardItemModel

from lib.ui.vulnscan_ui import Ui_Form
from lib.core.data      import vulnscan_config, running_config

class MForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MForm, self).__init__(parent)
        self.setupUi(self)

        # 将配置文件内容显示出来
        # 收录漏洞页显示
        self.vulnsTableViewModel = QStandardItemModel(0, 2)
        self.vulnsTableViewModel.setHorizontalHeaderLabels(['ID', '漏洞类型'])
        self.model = QStandardItemModel(0, 2)
        plugins_count = len(running_config.plugins)
        for row in range(plugins_count):
            item=QStandardItem('%s' % (row + 1))
            self.model.setItem(row, 0, item)
            item=QStandardItem('%s' % running_config.plugins[row])
            self.model.setItem(row, 1, item)
        self.vulnsTableView.setModel(self.model)
        self.vulnsTableView.setModel(self.vulnsTableViewModel)

        # 设置页显示
        self.threadsLineEdit.setText(str(vulnscan_config.threads))
        self.timeoutLineEdit.setText(str(vulnscan_config.TimeOut))
        self.userAgentLineEdit.setText(vulnscan_config.UserAgent)
        self.cookieLineEdit.setText(vulnscan_config.Cookie)

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