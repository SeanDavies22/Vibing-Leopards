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

        # Run GUI functions from main to add flow of operations. 
        self.main()

    def main(self):
        
        # Initialize class variables
        self.filePath = None

        # Action handling for inputFileButton.. 
        self.ui.inputFileButton.clicked.connect(self.input_file_button_action_handling)

    def input_file_button_action_handling(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        # Checks if file is able to be read or if a file was selected or not
        # Displays an error Pop-up if conditions match.        
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(
                self, "File Explorer", "",
                "Nessus Scan (*.nessus);;XML(*.xml);;All Files (*)",
            options=options)

            # Set the filepath to the filepath string in the tuple.
            self.filePath = file[0]
            f = open(self.filePath, "r")

        except OSError:
            msg = QtWidgets.QMessageBox()
            msg.setText("File is not able to be read, does not exist or no file was selected. Please choose another file to continue. ")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()

        # Sets the label next to the inputFileButton to the chosen file path.
        # Will stay set to "blank" if the error conditions are met. 
        self.ui.fileNameLabel.setText(self.filePath)


# Execute the program.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()

