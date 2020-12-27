# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vulnscan.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 395)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.urlLabel = QtWidgets.QLabel(self.tab)
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout_7.addWidget(self.urlLabel)
        self.urlLineEdit = QtWidgets.QLineEdit(self.tab)
        self.urlLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.horizontalLayout_7.addWidget(self.urlLineEdit)
        self.importPushButton = QtWidgets.QPushButton(self.tab)
        self.importPushButton.setObjectName("importPushButton")
        self.horizontalLayout_7.addWidget(self.importPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.urlsTableViewModel = QtGui.QStandardItemModel(0, 2)
        self.urlsTableViewModel.setHorizontalHeaderLabels(['ID', '网站地址'])
        self.urlsTableView = QtWidgets.QTableView(self.tab)
        self.urlsTableView.setObjectName("urlsTableView")
        self.urlsTableView.setModel(self.urlsTableViewModel)
        self.urlsTableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.urlsTableView)

        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startPushButton = QtWidgets.QPushButton(self.tab)
        self.startPushButton.setObjectName("startPushButton")
        self.verticalLayout_3.addWidget(self.startPushButton)
        self.importFromFilePushButton = QtWidgets.QPushButton(self.tab)
        self.importFromFilePushButton.setObjectName("importFromFilePushButton")
        self.verticalLayout_3.addWidget(self.importFromFilePushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.vulnsTableViewModel = QtGui.QStandardItemModel(0, 2)
        self.vulnsTableViewModel.setHorizontalHeaderLabels(['ID', '漏洞类型'])
        self.vulnsTableView = QtWidgets.QTableView(self.tab_2)
        self.vulnsTableView.setObjectName("vulnsTableView")
        self.vulnsTableView.setModel(self.vulnsTableViewModel)
        self.vulnsTableView.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_6.addWidget(self.vulnsTableView)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.threadsLabel = QtWidgets.QLabel(self.groupBox)
        self.threadsLabel.setObjectName("threadsLabel")
        self.horizontalLayout_4.addWidget(self.threadsLabel)
        self.threadsLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.threadsLineEdit.setObjectName("threadsLineEdit")
        self.horizontalLayout_4.addWidget(self.threadsLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.timeoutLabel = QtWidgets.QLabel(self.groupBox)
        self.timeoutLabel.setObjectName("timeoutLabel")
        self.horizontalLayout_5.addWidget(self.timeoutLabel)
        self.timeoutLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.timeoutLineEdit.setObjectName("timeoutLineEdit")
        self.horizontalLayout_5.addWidget(self.timeoutLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userAgentLabel = QtWidgets.QLabel(self.groupBox)
        self.userAgentLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.userAgentLabel.setObjectName("userAgentLabel")
        self.horizontalLayout_3.addWidget(self.userAgentLabel)
        self.userAgentLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userAgentLineEdit.setObjectName("userAgentLineEdit")
        self.horizontalLayout_3.addWidget(self.userAgentLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cookieLabel = QtWidgets.QLabel(self.groupBox)
        self.cookieLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.cookieLabel.setObjectName("cookieLabel")
        self.horizontalLayout_9.addWidget(self.cookieLabel)
        self.cookieLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.cookieLineEdit.setObjectName("cookieLineEdit")
        self.horizontalLayout_9.addWidget(self.cookieLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.applyPushButton = QtWidgets.QPushButton(self.groupBox)
        self.applyPushButton.setObjectName("applyPushButton")
        self.verticalLayout_2.addWidget(self.applyPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "vulnscan"))
        self.urlLabel.setText(_translate("Form", "URL:"))
        self.importPushButton.setText(_translate("Form", "导入"))
        self.startPushButton.setText(_translate("Form", "开始"))
        self.importFromFilePushButton.setText(_translate("Form", "从文件导入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "目标"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "收录漏洞"))
        self.groupBox.setTitle(_translate("Form", "扫描设置"))
        self.threadsLabel.setText(_translate("Form", "线程数:       "))
        self.timeoutLabel.setText(_translate("Form", "超时时间:   "))
        self.userAgentLabel.setText(_translate("Form", "UserAgent:    "))
        self.cookieLabel.setText(_translate("Form", "Cookie:        "))
        self.applyPushButton.setText(_translate("Form", "应用"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "设置"))
