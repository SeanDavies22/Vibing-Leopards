# Author: Nicholas Natale, Casey Staples
# Created: 11/2/22
# Edited: 11/15/22

# This file is an action handler for the Run Analysis window of the
# Cost Benefit Analysis Tool.


from RunScanWindow import Ui_RunScanWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from handle_db import HandleDB
import os
import sys
sys.path.append(os.getcwd())


class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, filePath, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.filePath = filePath
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)
        self.ui.dataTable.setColumnCount(4)
        self.populate_table(self.ui.dataTable, self.filePath)
        self.ui.dataTable.resizeColumnsToContents()

        self.ui.dataTable.cellDoubleClicked.connect(self.cve_id_table_cell_pressed)

    def cve_id_table_cell_pressed(self):
        for cell in self.ui.dataTable.selectionModel().selectedIndexes():
            row_number = cell.row()
            column_number = cell.column()
            if (column_number == 0):
                msg = QtWidgets.QMessageBox()
                msg.setText("You pressed a certain CVE ID. Good job.")
                msg.setWindowTitle("File Explorer")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                x = msg.exec_()

    def show_gui(self):
        self.rsg = RunScanGUI(self.filePath)
        self.rsg.show()

    def hide_gui(self):
        self.rsg = RunScanGUI
        self.rsg.hide()

    def parse_xml(self, filePath):
        file = open(filePath, "r")

        cve_id_nessus = []

        #self.rsg = RunScanGUI()
        # self.rsg.show_gui()

        # This is suppose to create the tree thing so
        # that we can parse the nessus file
        tree = ET.ElementTree(file=file)
        root = tree.getroot()

        # add the cve_ids found in the file to a list
        # return that list
        for child in root.iter('cve'):
            cve_id_nessus.append(child.text)

        return cve_id_nessus

    def populate_table(self, table, filepath):
        cve_id_nessus = []
        cve_id_nessus = self.parse_xml(filepath)
        db_handler = HandleDB()
        total_cost = []
        description = []
        counter_2 = 0  # counter for what row we are on.. might not need
        counter = 0  # counter for # of columns.. was going to try setRow here but didn't do anything

        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                counter += 1

        table.setRowCount(counter)

        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                description = db_handler.pull_description(
                    cve)  # pull matching description from db
                # pull matching cost from db
                cost_hours = db_handler.pull_cost_hrs(cve)
                total_hours = db_handler.pull_total_hrs(cve)
                table.setItem(counter_2, 0,
                              QtWidgets.QTableWidgetItem(cve))  # set first column to cve_id
                table.setItem(counter_2, 1,
                              QtWidgets.QTableWidgetItem(str(cost_hours[0])))  # set secound column to cost
                table.setItem(counter_2, 2,
                              QtWidgets.QTableWidgetItem(str(total_hours[0])))  # set third column to total hours
                # remove the brackets and the junk at the end from description
                description = description[2:-5]
                table.setItem(counter_2, 3,
                              QtWidgets.QTableWidgetItem(description))  # set third column to description
                counter_2 = counter_2 + 1

# Code that does the parsing for the database information .....

        # This actually parses the nessus file
        # Prints out matches found in the nessus file
        #msg = QtWidgets.QMessageBox()
        #msgTxtString = "Match found: "
        # for nessus_cve in root.iter('cve'):
        #database_cost = db_handler.pull_cost_data(nessus_cve.text)
        #msgTxtString = msgTxtString + " " + str(database_cost[0]) + " " + str(database_cost[1])

        # msg.setIcon(QtWidgets.QMessageBox.Information)
        # msg.setText(msgTxtString)
        #msg.setWindowTitle("Database Check")
        #x = msg.exec_()
