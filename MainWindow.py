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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 87, 47))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.inputFileButtonVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.inputFileButtonVLayout.setContentsMargins(0, 0, 0, 0)
        self.inputFileButtonVLayout.setObjectName("inputFileButtonVLayout")
        self.inputFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputFileButton.sizePolicy().hasHeightForWidth())
        self.inputFileButton.setSizePolicy(sizePolicy)
        self.inputFileButton.setMaximumSize(QtCore.QSize(200, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.inputFileButton.setFont(font)
        self.inputFileButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputFileButton.setObjectName("inputFileButton")
        self.inputFileButtonVLayout.addWidget(self.inputFileButton, 0, QtCore.Qt.AlignTop)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 110, 661, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.fileNameLabelVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.fileNameLabelVLayout.setContentsMargins(0, 0, 0, 0)
        self.fileNameLabelVLayout.setObjectName("fileNameLabelVLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setText("")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.fileNameLabelVLayout.addWidget(self.fileNameLabel, 0, QtCore.Qt.AlignTop)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 470, 251, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.runScanButtonVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.runScanButtonVLayout.setContentsMargins(0, 0, 0, 0)
        self.runScanButtonVLayout.setObjectName("runScanButtonVLayout")
        self.runScanButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.runScanButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.runScanButton.setFont(font)
        self.runScanButton.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.runScanButton.setObjectName("runScanButton")
        self.runScanButtonVLayout.addWidget(self.runScanButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.programNameHLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.programNameHLayout.setContentsMargins(0, 0, 0, 0)
        self.programNameHLayout.setObjectName("programNameHLayout")
        self.programNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.programNameLabel.setFont(font)
        self.programNameLabel.setStyleSheet("")
        self.programNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.programNameLabel.setObjectName("programNameLabel")
        self.programNameHLayout.addWidget(self.programNameLabel)
        self.topScreenBorderLine = QtWidgets.QFrame(self.centralwidget)
        self.topScreenBorderLine.setGeometry(QtCore.QRect(0, 50, 801, 16))
        self.topScreenBorderLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topScreenBorderLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topScreenBorderLine.setObjectName("topScreenBorderLine")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 200, 133, 81))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.businessSizeButtonVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.businessSizeButtonVLayout.setContentsMargins(0, 0, 0, 0)
        self.businessSizeButtonVLayout.setObjectName("businessSizeButtonVLayout")
        self.smallBusinessRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.smallBusinessRadioButton.setObjectName("smallBusinessRadioButton")
        self.businessSizeButtonVLayout.addWidget(self.smallBusinessRadioButton)
        self.mediumBusinessRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.mediumBusinessRadioButton.setObjectName("mediumBusinessRadioButton")
        self.businessSizeButtonVLayout.addWidget(self.mediumBusinessRadioButton)
        self.largeBusinessRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.largeBusinessRadioButton.setObjectName("largeBusinessRadioButton")
        self.businessSizeButtonVLayout.addWidget(self.largeBusinessRadioButton)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 70, 761, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.inputFilePermanentVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.inputFilePermanentVLayout.setContentsMargins(0, 0, 0, 0)
        self.inputFilePermanentVLayout.setObjectName("inputFilePermanentVLayout")
        self.inputFilePermanentLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inputFilePermanentLabel.setFont(font)
        self.inputFilePermanentLabel.setObjectName("inputFilePermanentLabel")
        self.inputFilePermanentVLayout.addWidget(self.inputFilePermanentLabel)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 160, 761, 31))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.businessSizeLabelVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.businessSizeLabelVLayout.setContentsMargins(0, 0, 0, 0)
        self.businessSizeLabelVLayout.setObjectName("businessSizeLabelVLayout")
        self.businessSizeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.businessSizeLabel.setFont(font)
        self.businessSizeLabel.setObjectName("businessSizeLabel")
        self.businessSizeLabelVLayout.addWidget(self.businessSizeLabel)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 290, 761, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.businessTypeLabelVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.businessTypeLabelVLayout.setContentsMargins(0, 0, 0, 0)
        self.businessTypeLabelVLayout.setObjectName("businessTypeLabelVLayout")
        self.businessTypeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.businessTypeLabel.setFont(font)
        self.businessTypeLabel.setObjectName("businessTypeLabel")
        self.businessTypeLabelVLayout.addWidget(self.businessTypeLabel)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 330, 133, 81))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.businessTypeButtonVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.businessTypeButtonVLayout.setContentsMargins(0, 0, 0, 0)
        self.businessTypeButtonVLayout.setObjectName("businessTypeButtonVLayout")
        self.homeSmallOfficeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_8)
        self.homeSmallOfficeRadioButton.setObjectName("homeSmallOfficeRadioButton")
        self.businessTypeButtonVLayout.addWidget(self.homeSmallOfficeRadioButton)
        self.corporateBusinessRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_8)
        self.corporateBusinessRadioButton.setObjectName("corporateBusinessRadioButton")
        self.businessTypeButtonVLayout.addWidget(self.corporateBusinessRadioButton)
        self.federalBusinessRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_8)
        self.federalBusinessRadioButton.setObjectName("federalBusinessRadioButton")
        self.businessTypeButtonVLayout.addWidget(self.federalBusinessRadioButton)
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
        self.runScanButton.setText(_translate("MainWindow", "Run Scan"))
        self.programNameLabel.setText(_translate("MainWindow", "Cost-Benefit Analysis Tool"))
        self.smallBusinessRadioButton.setText(_translate("MainWindow", "Small Sized Business"))
        self.mediumBusinessRadioButton.setText(_translate("MainWindow", "Medium Sized Business"))
        self.largeBusinessRadioButton.setText(_translate("MainWindow", "Large Sized Business"))
        self.inputFilePermanentLabel.setText(_translate("MainWindow", "Input File:"))
        self.businessSizeLabel.setText(_translate("MainWindow", "Business Size:"))
        self.businessTypeLabel.setText(_translate("MainWindow", "Business Type:"))
        self.homeSmallOfficeRadioButton.setText(_translate("MainWindow", "Home/ Small Office"))
        self.corporateBusinessRadioButton.setText(_translate("MainWindow", "Corporate"))
        self.federalBusinessRadioButton.setText(_translate("MainWindow", "Federal/Govermental"))
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
