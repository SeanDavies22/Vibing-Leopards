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
        MainWindow.resize(800, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 575))
        MainWindow.setMaximumSize(QtCore.QSize(800, 575))
        MainWindow.setStyleSheet("background-color: ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 87, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.inputFileButton.setMaximumSize(QtCore.QSize(200, 23))
        self.inputFileButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputFileButton.setObjectName("inputFileButton")
        self.verticalLayout.addWidget(self.inputFileButton)
        self.futureButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.futureButton3.setObjectName("futureButton3")
        self.verticalLayout.addWidget(self.futureButton3)
        self.futureButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.futureButton2.setObjectName("futureButton2")
        self.verticalLayout.addWidget(self.futureButton2)
        self.futureButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.futureButton1.setAutoFillBackground(False)
        self.futureButton1.setFlat(False)
        self.futureButton1.setObjectName("futureButton1")
        self.verticalLayout.addWidget(self.futureButton1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 10, 301, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fileNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setText("")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.verticalLayout_2.addWidget(self.fileNameLabel, 0, QtCore.Qt.AlignTop)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 470, 251, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.runScanButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.runScanButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.runScanButton.setFont(font)
        self.runScanButton.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.runScanButton.setObjectName("runScanButton")
        self.verticalLayout_3.addWidget(self.runScanButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFileTab = QtWidgets.QMenu(self.menubar)
        self.menuFileTab.setObjectName("menuFileTab")
        self.menuExport = QtWidgets.QMenu(self.menuFileTab)
        self.menuExport.setObjectName("menuExport")
        self.menuAboutTab = QtWidgets.QMenu(self.menubar)
        self.menuAboutTab.setObjectName("menuAboutTab")
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
        self.aboutProgramTabPress = QtWidgets.QAction(MainWindow)
        self.aboutProgramTabPress.setObjectName("aboutProgramTabPress")
        self.actionXML_3 = QtWidgets.QAction(MainWindow)
        self.actionXML_3.setObjectName("actionXML_3")
        self.actionNessus = QtWidgets.QAction(MainWindow)
        self.actionNessus.setObjectName("actionNessus")
        self.menuExport.addAction(self.actionXML_3)
        self.menuExport.addAction(self.actionNessus)
        self.menuFileTab.addAction(self.menuExport.menuAction())
        self.menuAboutTab.addAction(self.aboutProgramTabPress)
        self.menubar.addAction(self.menuFileTab.menuAction())
        self.menubar.addAction(self.menuAboutTab.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cost-Benefit Analysis Tool"))
        self.inputFileButton.setText(_translate("MainWindow", "Select Input File"))
        self.futureButton3.setText(_translate("MainWindow", "Futue Button"))
        self.futureButton2.setText(_translate("MainWindow", "Future Button"))
        self.futureButton1.setText(_translate("MainWindow", "Future Button"))
        self.runScanButton.setText(_translate("MainWindow", "Run Scan"))
        self.menuFileTab.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuAboutTab.setTitle(_translate("MainWindow", "About"))
        self.actionXML.setText(_translate("MainWindow", "XML"))
        self.actionJSON.setText(_translate("MainWindow", "JSON"))
        self.actionXML_2.setText(_translate("MainWindow", "XML"))
        self.actionJSON_2.setText(_translate("MainWindow", "JSON"))
        self.actionAbout_Program.setText(_translate("MainWindow", "About Program"))
        self.aboutProgramTabPress.setText(_translate("MainWindow", "About Program"))
        self.actionXML_3.setText(_translate("MainWindow", "XML"))
        self.actionNessus.setText(_translate("MainWindow", "Nessus"))
