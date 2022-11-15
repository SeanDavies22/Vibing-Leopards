# Author: Nicholas Natale
# Created: 11/1/22
# Edited: 11/3/22

# This program will contain all of the code to add functionality to the 
# designed GUI, so that way new iterations of the GUI will not remove old working
# GUI functionality. 

from MainWindow import Ui_MainWindow
from RunScanWindow_actions import RunScanGUI
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

        # Action handling for runScanButton.. 
        self.ui.runScanButton.clicked.connect(self.run_scan_button_action_handling)

        # Action handling for About Program Tab press..
        self.ui.aboutProgramTabPress.triggered.connect(self.about_program_action_handling)

    def input_file_button_action_handling(self):
        options = QtWidgets.QFileDialog.Options()
        
        # The below comment will use the PyQt5 file explorer.
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog

        # Checks if file is able to be read or if a file was selected or not.
        # Displays an error Pop-up if conditions match.        
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self, "File Explorer", "", "Nessus Scan (*.nessus);;XML(*.xml);;All Files (*)",
            options=options)

            # Set the filepath to the filepath string in the tuple.
            self.filePath = file[0]
            f = open(self.filePath, "r")

        except OSError:
            self.filePath = None
            self.ui.fileNameLabel.setText(self.filePath) # Reset file name label before error.
            self.show_error_pop_up("File is not able to be read, does not exist or no file was selected. Please choose another file to continue. ")

        # Sets the label next to the inputFileButton to the chosen file path.
        # Label Will stay set to "" if the error conditions are met. 
        self.ui.fileNameLabel.setText(self.filePath)

    def run_scan_button_action_handling(self):
        if self.filePath == None:
            self.show_error_pop_up("No input file selected. Please select an input file.")
        else:
            self.rsg = RunScanGUI()
            self.rsg.show_gui()
            self.rsg.parse_xml(self.filePath)

    # Action handling for the about program tab option in the menu bar of the GUI. 
    def about_program_action_handling(self):
        aboutProgramText = "Welcome to the Cost-Benefit Analysis Tool. Some more stuff will be in here later.\n\n Developed By: Vibing Leopards"
        self.show_info_pop_up(aboutProgramText)

    # Displays an error pop up with given text as the first parameter.
    def show_error_pop_up(self, errorMessage):
            msg = QtWidgets.QMessageBox()
            msg.setText(errorMessage)
            msg.setWindowTitle("File Explorer")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()

    # displays a information pop up with given text as the first parameter. 
    def show_info_pop_up(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setText(text)
        msg.setWindowTitle("About Program")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

# Execute the program, and show the GUI if the program was
# called directly, not imported.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()
