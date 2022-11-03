from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RunScanWindow(object):
    def setupUi(self, RunScanWindow):
        RunScanWindow.setObjectName("RunScanWindow")
        RunScanWindow.resize(800, 575)
        RunScanWindow.setMinimumSize(QtCore.QSize(800, 575))
        RunScanWindow.setMaximumSize(QtCore.QSize(800, 575))
        self.centralwidget = QtWidgets.QWidget(RunScanWindow)
        self.centralwidget.setObjectName("centralwidget")
        RunScanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RunScanWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        RunScanWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RunScanWindow)
        self.statusbar.setObjectName("statusbar")
        RunScanWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RunScanWindow)
        QtCore.QMetaObject.connectSlotsByName(RunScanWindow)

    def retranslateUi(self, RunScanWindow):
        _translate = QtCore.QCoreApplication.translate
        RunScanWindow.setWindowTitle(_translate("RunScanWindow", "Run Analysis"))
