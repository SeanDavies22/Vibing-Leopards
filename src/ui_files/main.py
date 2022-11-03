# Author: Nicholas Natale, Casey Staples
# Created: 11/1/22
# Edited: 3/11/22 - By Casey added the database stuff

# This program will contain all of the code to add functionality to the 
# designed GUI, so that way new iterations of the GUI will not remove old working
# GUI functionality. 

from MainWindow import Ui_MainWindow
from RunScanWindow_actions import RunScanGUI
from PyQt5 import QtCore, QtGui, QtWidgets
from handle_db import *
import xml.etree.cElementTree as ET

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

    def input_file_button_action_handling(self):
        options = QtWidgets.QFileDialog.Options()
        # The below comment will use the PyQt5 file explorer.
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog

        # Checks if file is able to be read or if a file was selected or not
        # Displays an error Pop-up if conditions match.        
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(self, "File Explorer", "", "Nessus Scan (*.nessus);;XML(*.xml);;All Files (*)",
            options=options)

            # Set the filepath to the filepath string in the tuple.
            self.filePath = file[0]
            f = open(self.filePath, "r")

        except OSError:
            msg = QtWidgets.QMessageBox()
            msg.setText("File is not able to be read, does not exist or no file was selected. Please choose another file to continue. ")
            msg.setWindowTitle("File Explorer")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()

        # Sets the label next to the inputFileButton to the chosen file path.
        # Will stay set to "blank" if the error conditions are met. 
        self.ui.fileNameLabel.setText(self.filePath)

    def run_scan_button_action_handling(self):
        # Vars to handle the database
        risk_list = []
        db_handler = HandleDB()

        self.rsg = RunScanGUI()
        self.rsg.show_gui()
        #Pull the risk levels from the database, store into the array
        risk_list = db_handler.pull_risk_data()

        # This is suppose to create the tree thing so
        # that we can parse the nessus file
        tree = ET.ElementTree(file=self.filePath)
        root = tree.getroot()
        print(type(root))
        # This actually parses the nessus file
        # Not sure if it's prasing the right data, 
        # or if the right data is being checked from the array
        # But it does run without crashing, prints out a bunch of No Match
        for risk in root.iter('risk_factor'):
          if risk_list in risk:
            print(risk.text)
          else:
            print("No match")


    

            

# Execute the program, and show the GUI if the program was
# called directly, not imported.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()

