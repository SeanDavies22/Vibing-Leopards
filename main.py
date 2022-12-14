# Author: Nicholas Natale, Casey Staples
# Created: 11/1/22
# Edited: 12/13/22

# This file contains all code to add functionality to the designed GUI,
# so new iterations of the GUI will not remove old working
# functional code.

from MainWindow import Ui_MainWindow
from RunScanWindow_actions import RunScanGUI
from PyQt5 import QtGui, QtWidgets
from os import path
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
        self.setWindowIcon(QtGui.QIcon('vl_img.ico'))

        # Action handle linking to the appropriate methods
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

        # Checks if file is able to be read or if a file was selected or not.
        # Displays an error Pop-up if conditions match.
        try:
            file = QtWidgets.QFileDialog.getOpenFileName(
                self, "File Explorer", "", "Nessus Scan (*.nessus);;Excel(*.xlsx);;XML(*.xml);;All Files (*)", options=options)

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
        # Label will stay set to "" if the error conditions are met.
        self.ui.fileNameLabel.setText(self.filePath)

    def run_scan_button_action_handling(self):
        file_extension = ""
        if self.filePath:
            # split file name to get extension for excel import
            file_extension = path.splitext(self.filePath)[1]

        if (file_extension == ".xlsx"):
            self.rsg = RunScanGUI(
                self.filePath, self.businessSize, self.businessType)
            self.rsg.show()
        elif (self.filePath == None):
            self.show_error_pop_up(
                "No input file selected. Please select an input file.")
        elif (self.businessSize == 0):
            self.show_error_pop_up(
                "No business size selected. Please select a business size.")
        elif (self.businessType == 0):
            self.show_error_pop_up(
                "No business type selected. Please select a business type.")
        elif (self.check_xml_parsing(self.filePath) == False):
            self.show_error_pop_up(
                "Source file is not parseable. Please choose another XML-like file.")
        elif ((self.filePath != None) and (self.businessSize > 0) and (self.businessType > 0) and (self.check_xml_parsing(self.filePath) == True)):
            self.rsg = RunScanGUI(
                self.filePath, self.businessSize, self.businessType)
            self.rsg.show()

    # Checks if the input file is parseable and if it has any CVE elements in it. 
    def check_xml_parsing(self, filePath):
        file = open(filePath, "r")
        cve_id_nessus = []

        # Create parsing tree to for scanning Nessus file.
        try:
            tree = ET.ElementTree(file=file)
            root = tree.getroot()
            for child in root.iter('cve'):
                cve_id_nessus.append(child.text)
        except ET.ParseError:
            return False

        # Add the cve_ids found in the source file to a list.
        # Return the list.
        if (len(cve_id_nessus) == 0):
            return False
        else:
            return True

    # Action handling methods
    def about_program_action_handling(self):

        # This sets about tab to show this text. Used .join keep it from being one giant line.
        aboutProgramText = '\n'.join(("Welcome to the Cost-Benefit Analysis Tool. This tool was created ",
                                     "for use with a Nessus vulnerability scan export file and a database ",
                                      "of existing vulnerabilities. The Cost-Benefit Analysis Tool will",
                                      "compare against said database and will list the common vulnerabilites ",
                                      "along with their attributes, and will form reccomendations based",
                                      "on the resulting vulnerabilities.",
                                      "\nDeveloped By: Vibing Leopards (2022)",
                                      "Casey Staples, Nicholas Natale, Daniel Ortiz, Sean Davies, Luck Heck"))

        self.show_info_pop_up(aboutProgramText)

    # Action handling for the radio buttons.
    def small_business_radio_button_action_handling(self):
        self.businessSize = 1
    def medium_business_radio_button_action_handling(self):
        self.businessSize = 2
    def large_business_radio_button_action_handling(self):
        self.businessSize = 3
    def small_home_office_business_action_handling(self):
        self.businessType = 1
    def corporate_office_business_action_handling(self):
        self.businessType = 2
    def federal_office_business_action_handling(self):
        self.businessType = 3

    # Displays an error pop up with given text as the first parameter.
    def show_error_pop_up(self, errorMessage):
        msg = QtWidgets.QMessageBox()
        msg.setText(errorMessage)
        msg.setWindowTitle("File Explorer")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        x = msg.exec_()

    # Displays a information pop up with given text as the first parameter.
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
    app.setStyle("Windows")
    mainGUI = MainGUI()
    mainGUI.show()
    app.exec_()
