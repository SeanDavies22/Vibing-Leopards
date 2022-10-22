# Test base application UI
# Casey Staples
# Save / Open_all menu buttons will open dialog boxes
# Github will open a web browser to the github page


import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow


class Ui_MainWindow(QMainWindow):

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            self.close()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
            self.close()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.close()

    def goToWebsite(self):
        webbrowser.open("https://github.com/SeanDavies22/Vibing-Leopards")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cost Benefit Analysis Tool")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_Open_Recent = QtWidgets.QMenu(self.menuFile)
        self.menu_Open_Recent.setObjectName("menu_Open_Recent")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionOpen_All = QtWidgets.QAction(MainWindow)
        self.actionOpen_All.setObjectName("actionOpen_All")
        self.action_Open_All = QtWidgets.QAction(MainWindow)
        self.action_Open_All.setObjectName("action_Open_All")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        self.action_GitHub = QtWidgets.QAction(MainWindow)
        self.action_GitHub.setObjectName("action_GitHub")

        self.action_GitHub.triggered.connect(self.goToWebsite)

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveFileDialog)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menu_Open_Recent.addAction(self.actionOpen_All)
        self.menu_Open_Recent.addSeparator()
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_Open_Recent.menuAction())
        self.menuFile.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menuAbout.addSeparator()
        self.menuHelp.addAction(self.action_GitHub)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_Open_Recent.triggered.connect(self.openFileNameDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu_Open_Recent.setTitle(
            _translate("MainWindow", "&Open Recent"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.actionOpen_All.setText(_translate("MainWindow", "Open All"))
        self.action_Open_All.setText(_translate("MainWindow", "&Open All"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.action_GitHub.setText(_translate("MainWindow", "&GitHub"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
