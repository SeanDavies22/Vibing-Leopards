# Author: Nicholas Natale, Casey Staples
# Created: 11/2/22
# Edited: 11/8/22

# This file is an action handler for the Run Analysis window of the
# Cost Benefit Analysis Tool.

from RunScanWindow import Ui_RunScanWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from handle_db import *


class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)

    def show_gui(self):
        self.rsg = RunScanGUI()
        self.rsg.show()

    def hide_gui(self):
        self.rsg = RunScanGUI
        self.rsg.hide()

    def parse_xml(self, filePath):
        file = open(filePath, "r")

        database_cost = []
        db_handler = HandleDB()

        self.rsg = RunScanGUI()
        self.rsg.show_gui()
        # Pull cve ids from the database, store into the array

        # This is suppose to create the tree thing so
        # that we can parse the nessus file
        tree = ET.ElementTree(file=file)
        root = tree.getroot()

        # This actually parses the nessus file
        # Prints out matches found in the nessus file
        msg = QtWidgets.QMessageBox()
        msgTxtString = "Match found: "
        for nessus_cve in root.iter('cve'):
            database_cost = db_handler.pull_cost_data(nessus_cve.text)
            msgTxtString = msgTxtString + " " + str(database_cost[0]) + " " + str(database_cost[1])
            
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(msgTxtString)
        msg.setWindowTitle("Database Check")
        x = msg.exec_()
