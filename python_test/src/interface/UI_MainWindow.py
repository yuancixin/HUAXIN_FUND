# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WorkSpace\Git\python_test\src\interface\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 751)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_update_state = QtWidgets.QLabel(self.frame)
        self.label_update_state.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_update_state.setFont(font)
        self.label_update_state.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_update_state.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_update_state.setLineWidth(3)
        self.label_update_state.setScaledContents(False)
        self.label_update_state.setObjectName("label_update_state")
        self.horizontalLayout.addWidget(self.label_update_state)
        self.check_update_future = QtWidgets.QCheckBox(self.frame)
        self.check_update_future.setChecked(True)
        self.check_update_future.setObjectName("check_update_future")
        self.horizontalLayout.addWidget(self.check_update_future)
        self.check_update_stock = QtWidgets.QCheckBox(self.frame)
        self.check_update_stock.setChecked(True)
        self.check_update_stock.setObjectName("check_update_stock")
        self.horizontalLayout.addWidget(self.check_update_stock)
        self.check_update_option = QtWidgets.QCheckBox(self.frame)
        self.check_update_option.setChecked(True)
        self.check_update_option.setObjectName("check_update_option")
        self.horizontalLayout.addWidget(self.check_update_option)
        self.check_update_actual = QtWidgets.QCheckBox(self.frame)
        self.check_update_actual.setChecked(True)
        self.check_update_actual.setObjectName("check_update_actual")
        self.horizontalLayout.addWidget(self.check_update_actual)
        self.check_update_research = QtWidgets.QCheckBox(self.frame)
        self.check_update_research.setChecked(True)
        self.check_update_research.setObjectName("check_update_research")
        self.horizontalLayout.addWidget(self.check_update_research)
        self.button_update = QtWidgets.QPushButton(self.frame)
        self.button_update.setEnabled(True)
        self.button_update.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_update.setMouseTracking(False)
        self.button_update.setAcceptDrops(False)
        self.button_update.setToolTip("")
        self.button_update.setToolTipDuration(-1)
        self.button_update.setWhatsThis("")
        self.button_update.setObjectName("button_update")
        self.horizontalLayout.addWidget(self.button_update)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(5)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_stock = QtWidgets.QWidget()
        self.tab_stock.setObjectName("tab_stock")
        self.tabWidget.addTab(self.tab_stock, "")
        self.tab_bond = QtWidgets.QWidget()
        self.tab_bond.setObjectName("tab_bond")
        self.tabWidget.addTab(self.tab_bond, "")
        self.tab_fund = QtWidgets.QWidget()
        self.tab_fund.setObjectName("tab_fund")
        self.tabWidget.addTab(self.tab_fund, "")
        self.tab_future = QtWidgets.QWidget()
        self.tab_future.setObjectName("tab_future")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_future)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(55, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.check_fut_ave = QtWidgets.QCheckBox(self.tab_future)
        self.check_fut_ave.setChecked(True)
        self.check_fut_ave.setObjectName("check_fut_ave")
        self.horizontalLayout_13.addWidget(self.check_fut_ave)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.tab_future)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.input_future_n = QtWidgets.QSpinBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_future_n.sizePolicy().hasHeightForWidth())
        self.input_future_n.setSizePolicy(sizePolicy)
        self.input_future_n.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_n.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_n.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_future_n.setWrapping(False)
        self.input_future_n.setFrame(True)
        self.input_future_n.setSpecialValueText("")
        self.input_future_n.setMinimum(1)
        self.input_future_n.setMaximum(1000)
        self.input_future_n.setObjectName("input_future_n")
        self.verticalLayout_5.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.input_future_m = QtWidgets.QDoubleSpinBox(self.splitter_2)
        self.input_future_m.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_m.setMaximumSize(QtCore.QSize(120, 28))
        self.input_future_m.setSpecialValueText("")
        self.input_future_m.setDecimals(3)
        self.input_future_m.setSingleStep(0.001)
        self.input_future_m.setObjectName("input_future_m")
        self.verticalLayout_5.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_3)
        self.label_4.setObjectName("label_4")
        self.input_future_d = QtWidgets.QDoubleSpinBox(self.splitter_3)
        self.input_future_d.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_d.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_d.setSpecialValueText("")
        self.input_future_d.setMaximum(9999.0)
        self.input_future_d.setObjectName("input_future_d")
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.check_fut_nm = QtWidgets.QCheckBox(self.tab_future)
        self.check_fut_nm.setChecked(True)
        self.check_fut_nm.setObjectName("check_fut_nm")
        self.horizontalLayout_8.addWidget(self.check_fut_nm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.check_fut_different = QtWidgets.QCheckBox(self.tab_future)
        self.check_fut_different.setChecked(True)
        self.check_fut_different.setObjectName("check_fut_different")
        self.horizontalLayout_10.addWidget(self.check_fut_different)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.splitter_4 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_4)
        self.label_5.setObjectName("label_5")
        self.input_future_diff_code = QtWidgets.QLineEdit(self.splitter_4)
        self.input_future_diff_code.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_diff_code.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_diff_code.setObjectName("input_future_diff_code")
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.check_fut_comb = QtWidgets.QCheckBox(self.tab_future)
        self.check_fut_comb.setChecked(True)
        self.check_fut_comb.setObjectName("check_fut_comb")
        self.horizontalLayout_6.addWidget(self.check_fut_comb)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_5 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_5)
        self.label_6.setObjectName("label_6")
        self.input_future_comb_code1 = QtWidgets.QLineEdit(self.splitter_5)
        self.input_future_comb_code1.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_comb_code1.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_comb_code1.setObjectName("input_future_comb_code1")
        self.verticalLayout_6.addWidget(self.splitter_5)
        self.splitter_6 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_7 = QtWidgets.QLabel(self.splitter_6)
        self.label_7.setObjectName("label_7")
        self.input_future_comb_code2 = QtWidgets.QLineEdit(self.splitter_6)
        self.input_future_comb_code2.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_comb_code2.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_comb_code2.setObjectName("input_future_comb_code2")
        self.verticalLayout_6.addWidget(self.splitter_6)
        self.splitter_7 = QtWidgets.QSplitter(self.tab_future)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_8 = QtWidgets.QLabel(self.splitter_7)
        self.label_8.setObjectName("label_8")
        self.input_future_comb_n = QtWidgets.QSpinBox(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_future_comb_n.sizePolicy().hasHeightForWidth())
        self.input_future_comb_n.setSizePolicy(sizePolicy)
        self.input_future_comb_n.setMinimumSize(QtCore.QSize(120, 27))
        self.input_future_comb_n.setMaximumSize(QtCore.QSize(120, 27))
        self.input_future_comb_n.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_future_comb_n.setWrapping(False)
        self.input_future_comb_n.setFrame(True)
        self.input_future_comb_n.setSpecialValueText("")
        self.input_future_comb_n.setMinimum(1)
        self.input_future_comb_n.setMaximum(1000)
        self.input_future_comb_n.setObjectName("input_future_comb_n")
        self.verticalLayout_6.addWidget(self.splitter_7)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(28, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.button_future_strategy = QtWidgets.QPushButton(self.tab_future)
        self.button_future_strategy.setObjectName("button_future_strategy")
        self.horizontalLayout_9.addWidget(self.button_future_strategy)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(55, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.tabWidget.addTab(self.tab_future, "")
        self.tab_option = QtWidgets.QWidget()
        self.tab_option.setObjectName("tab_option")
        self.tabWidget.addTab(self.tab_option, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(5)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.button_clearlog = QtWidgets.QPushButton(self.frame_2)
        self.button_clearlog.setObjectName("button_clearlog")
        self.horizontalLayout_5.addWidget(self.button_clearlog)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.LogInfoBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.LogInfoBrowser.setObjectName("LogInfoBrowser")
        self.verticalLayout.addWidget(self.LogInfoBrowser)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileCloseAction = QtWidgets.QAction(MainWindow)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.fileNewAction)
        self.menu.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "华鑫基金"))
        self.label_title.setText(_translate("MainWindow", "HX_FUND"))
        self.label_update_state.setText(_translate("MainWindow", "数据更新   "))
        self.check_update_future.setText(_translate("MainWindow", "期货"))
        self.check_update_stock.setText(_translate("MainWindow", "股票"))
        self.check_update_option.setText(_translate("MainWindow", "期权"))
        self.check_update_actual.setText(_translate("MainWindow", "基价"))
        self.check_update_research.setText(_translate("MainWindow", "研报"))
        self.button_update.setText(_translate("MainWindow", "更新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stock), _translate("MainWindow", "股票"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bond), _translate("MainWindow", "债券"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fund), _translate("MainWindow", "基金"))
        self.check_fut_ave.setText(_translate("MainWindow", "均线策略"))
        self.label.setText(_translate("MainWindow", "   均线（N）"))
        self.label_2.setText(_translate("MainWindow", "   比率（M）"))
        self.label_4.setText(_translate("MainWindow", "   差值（D）"))
        self.check_fut_nm.setText(_translate("MainWindow", "NM策略"))
        self.check_fut_different.setText(_translate("MainWindow", "基差图"))
        self.label_5.setText(_translate("MainWindow", "   合约代码"))
        self.check_fut_comb.setText(_translate("MainWindow", "组合图"))
        self.label_6.setText(_translate("MainWindow", "   合约1"))
        self.label_7.setText(_translate("MainWindow", "   合约2"))
        self.label_8.setText(_translate("MainWindow", "   均线（N）"))
        self.button_future_strategy.setText(_translate("MainWindow", "策略查找"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_future), _translate("MainWindow", "期货"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_option), _translate("MainWindow", "期权"))
        self.label_3.setText(_translate("MainWindow", "日志信息"))
        self.button_clearlog.setText(_translate("MainWindow", "清空"))
        self.LogInfoBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.fileOpenAction.setText(_translate("MainWindow", "打开"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.fileNewAction.setText(_translate("MainWindow", "新建"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Alt+N"))
        self.fileCloseAction.setText(_translate("MainWindow", "关闭"))
        self.fileCloseAction.setShortcut(_translate("MainWindow", "Alt+C"))

