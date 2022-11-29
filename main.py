# Author: Nicholas Natale
# Created: 11/1/22
# Edited: 11/28/22

# This program will contain all of the code to add functionality to the
# designed GUI, so that way new iterations of the GUI will not remove old working
# GUI functionality.

from MainWindow import Ui_MainWindow
from RunScanWindow_actions import RunScanGUI
from PyQt5 import QtCore, QtGui, QtWidgets

import xml.etree.ElementTree as ET


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
        self.businessSize = 0
        self.businessType = 0

        # TODO: Might want to merge businessSize and businessType into one variable.
        self.business_info = []

        # Action handing linking to the appropriate methods
        self.ui.inputFileButton.clicked.connect(
            self.input_file_button_action_handling)
        self.ui.runScanButton.clicked.connect(
            self.run_scan_button_action_handling)
        self.ui.aboutProgramTabPress.triggered.connect(
            self.about_program_action_handling)

        self.ui.smallBusinessRadioButton.pressed.connect(
            self.small_business_radio_button_action_handling)
        self.ui.mediumBusinessRadioButton.pressed.connect(
            self.medium_business_radio_button_action_handling)
        self.ui.largeBusinessRadioButton.pressed.connect(
            self.large_business_radio_button_action_handling)

        self.ui.homeSmallOfficeRadioButton.pressed.connect(
            self.small_home_office_business_action_handling)
        self.ui.corporateBusinessRadioButton.pressed.connect(
            self.corporate_office_business_action_handling)
        self.ui.federalBusinessRadioButton.pressed.connect(
            self.federal_office_business_action_handling)

    def input_file_button_action_handling(self):
        options = QtWidgets.QFileDialog.Options()

        # The below comment will use the PyQt5 file explorer.
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog

        # Checks if file is able to be read or if a file was selected or not.
        # Displays an error Pop-up if conditions match.
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(
                self, "File Explorer", "", "Nessus Scan (*.nessus);;XML(*.xml);;All Files (*)", options=options)

            # Set the filepath to the filepath string in the tuple.
            self.filePath = file[0]
            f = open(self.filePath, "r")

        except OSError:
            self.filePath = None
            # Reset file name label before error.
            self.ui.fileNameLabel.setText(self.filePath)
            self.show_error_pop_up(
                "File is not able to be read, does not exist or no file was selected. Please choose another file to continue. ")

        # Sets the label next to the inputFileButton to the chosen file path.
        # Label Will stay set to "" if the error conditions are met.
        self.ui.fileNameLabel.setText(self.filePath)

    def run_scan_button_action_handling(self):
        if (self.filePath == None):
            self.show_error_pop_up(
                "No input file selected. Please select an input file.")
        if (self.businessSize == 0):
            self.show_error_pop_up(
                "No business size selected. Please select a business size.")
        if (self.businessType == 0):
            self.show_error_pop_up(
                "No business type selected. Please select a business type.")
        if (self.check_xml_parsing(self.filePath) == False):
            self.show_error_pop_up(
                "Source file is not parseable. Please choose another XML-like file.")
        if ((self.filePath != None) and (self.businessSize > 0) and (self.businessType > 0) and (self.check_xml_parsing(self.filePath) == True)):
            self.rsg = RunScanGUI(self.filePath, self.business_info)
            self.rsg.show_gui()
            table = self.rsg.ui.dataTable
            table.show()


    def check_xml_parsing(self, filePath):
        file_parseable = True
        try:
            file = open(filePath, 'r')
            tree = ET.ElementTree(file=file)
        except (ET.ParseError, TypeError) as err:
            file_parseable = False

        return file_parseable


    # Action handling methods
    def about_program_action_handling(self):
        aboutProgramText = "Welcome to the Cost-Benefit Analysis Tool. Some more stuff will be in here later.\n\n Developed By: Vibing Leopards"
        self.show_info_pop_up(aboutProgramText)

    def small_business_radio_button_action_handling(self):
        self.businessSize = 1
        self.business_info.append(self.businessSize)

    def medium_business_radio_button_action_handling(self):
        self.businessSize = 2
        self.business_info.append(self.businessSize)

    def large_business_radio_button_action_handling(self):
        self.businessSize = 3
        self.business_info.append(self.businessSize)

    def small_home_office_business_action_handling(self):
        self.businessType = 1
        self.business_info.append(self.businessType)

    def corporate_office_business_action_handling(self):
        self.businessType = 2
        self.business_info.append(self.businessType)

    def federal_office_business_action_handling(self):
        self.businessType = 3
        self.business_info.append(self.businessType)

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
