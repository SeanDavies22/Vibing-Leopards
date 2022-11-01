# Author: Nicholas Natale
# Date: 11/1/22

# This program will contain all of the code to add functionality to the 
# designed GUI, so that way new iterations of the GUI will not remove old working
# GUI functionality. 

from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainGUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filePath = None
        self.ui.inputFileButton.clicked.connect(self.getInputFile)

    def getInputFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file = QtWidgets.QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "",
                    "Nessus Scan (*.nessus);;XML(*.xml);;Python(*.py);;All Files (*)",
                    options=options)
        self.filePath = file[0]
        self.ui.fileNameLabel.setText(self.filePath)
        
        # Temp print statement to see filepath provided. 
        #print(self.filePath)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()

