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
        self.ui.inputFileButton.clicked.connect(
            self.input_file_button_action_handling)

        # Action handling for runScanButton..
        self.ui.runScanButton.clicked.connect(
            self.run_scan_button_action_handling)

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
            msg.setText(
                "File is not able to be read, does not exist or no file was selected. Please choose another file to continue. ")
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
        # Pull the risk levels from the database, store into the array
        risk_list = db_handler.pull_risk_data()

        # This is suppose to create the tree thing so
        # that we can parse the nessus file
        tree = ET.ElementTree(file=self.filePath)
        root = tree.getroot()

        # This actually parses the nessus file
        # Prints out matches found in the nessus file
        for nessus_risk in root.iter('risk_factor'):
            for db_risk in risk_list:
                if nessus_risk.text.__contains__(db_risk):
                    print(nessus_risk.text)

        # This look just prints out what is in the nessus file
        # that we are comparing to the database array
        # useful to testing if we are collecting the right xml tag
        # for nessus_risk in root.iter('risk_factor'):
        #     print(nessus_risk.text)

        # Have to del database handler to close database connection .. will cause errors if not closed.
        # Will move this into a separate function to coneect and close the database for final realase.
        del db_handler


# Execute the program, and show the GUI if the program was
# called directly, not imported.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()
