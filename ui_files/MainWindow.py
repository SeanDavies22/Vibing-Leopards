# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.topScreenLabel = QtWidgets.QLabel(self.centralwidget)
        self.topScreenLabel.setGeometry(QtCore.QRect(270, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.topScreenLabel.setFont(font)
        self.topScreenLabel.setObjectName("topScreenLabel")
        self.inputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputFileButton.setGeometry(QtCore.QRect(30, 110, 121, 28))
        self.inputFileButton.setObjectName("inputFileButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 60, 941, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionXML = QtWidgets.QAction(MainWindow)
        self.actionXML.setObjectName("actionXML")
        self.actionJSON = QtWidgets.QAction(MainWindow)
        self.actionJSON.setObjectName("actionJSON")
        self.actionXML_2 = QtWidgets.QAction(MainWindow)
        self.actionXML_2.setObjectName("actionXML_2")
        self.actionJSON_2 = QtWidgets.QAction(MainWindow)
        self.actionJSON_2.setObjectName("actionJSON_2")
        self.actionAbout_Program = QtWidgets.QAction(MainWindow)
        self.actionAbout_Program.setObjectName("actionAbout_Program")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cost-Benefit Analysis Tool"))
        self.topScreenLabel.setText(_translate("MainWindow", "Cost Jawn Analysis"))
        self.inputFileButton.setText(_translate("MainWindow", "Select Jawn"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionXML.setText(_translate("MainWindow", "XML"))
        self.actionJSON.setText(_translate("MainWindow", "JSON"))
        self.actionXML_2.setText(_translate("MainWindow", "XML"))
        self.actionJSON_2.setText(_translate("MainWindow", "JSON"))
        self.actionAbout_Program.setText(_translate("MainWindow", "About Program"))