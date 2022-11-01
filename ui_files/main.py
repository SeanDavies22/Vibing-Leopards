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

        # Sample print text to console to see if input file button works. 
        self.ui.inputFileButton.clicked.connect(self.printTextButtonClick)
    
    def printTextButtonClick(self):
        print("Input file button working!")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()

