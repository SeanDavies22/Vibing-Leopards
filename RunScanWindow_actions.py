# Author: Nicholas Natale, Casey Staples
# Created: 11/2/22
# Edited: 11/15/22

# This file is an action handler for the Run Analysis window of the
# Cost Benefit Analysis Tool.


from RunScanWindow import Ui_RunScanWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from handle_db import HandleDB
from VulnInfo import VulnInfo
import os
import sys
import xlsxwriter
sys.path.append(os.getcwd())


class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, filePath, bussiness_info, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.filePath = filePath
        self.business_info = bussiness_info
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)
        self.ui.dataTable.setColumnCount(4)
        self.populate_table(self.ui.dataTable,
                            self.filePath, self.business_info)
        self.ui.dataTable.resizeColumnsToContents()
        self.ui.dataTable.resizeRowsToContents()
        self.ui.dataTable.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # The function below can be used to sort a certain column from highest at top to lowest. 
        # This example uses the Engineering Hrs column. 
        #self.ui.dataTable.sortByColumn(2, QtCore.Qt.DescendingOrder)

        self.ui.dataTable.cellDoubleClicked.connect(
            self.cve_id_table_cell_pressed)
        self.ui.actionSave.triggered.connect(self.exporter)

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

    def exporter(self, filename=None):
        if not filename:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, 'Save File', " "'.xlsx', '(*.xlsx)')

        if filename[0]:
            print(filename[0])
            work_book = xlsxwriter.Workbook(filename[0])
            work_sheet = work_book.add_worksheet()
            row = 0
            col = 0
            for i in range(self.ui.dataTable.columnCount()):
                for x in range(self.ui.dataTable.rowCount()):
                    try:
                        text = str(self.ui.dataTable.item(row, col).text())
                        work_sheet.write(row, col, str(text))
                        row += 1
                    except AttributeError:
                        row += 1
                row = 0
                col += 1
           # self.export(work_sheet)
        work_book.close()

    # def export(self, work_sheet):
        #row = 0
        #col = 0
        # for i in range(self.ui.dataTable.columnCount()):
        # for x in range(self.ui.dataTable.rowCount()):
        # try:
        #  text = str(self.ui.dataTable.item(row, col).text())
        #   work_sheet._write(row, col, str(text))
        #   row += 1
        # except AttributeError:
        #   row += 1
        #row = 0
        #col += 1

    def show_gui(self):
        self.rsg = RunScanGUI(self.filePath, self.business_info)
        self.rsg.show()

    def hide_gui(self):
        self.rsg = RunScanGUI
        self.rsg.hide()

    def parse_xml(self, filePath):
        file = open(filePath, "r")
        cve_id_nessus = []

        # Create parsing tree to for scanning Nessus file.
        tree = ET.ElementTree(file=file)
        root = tree.getroot()

        # Add the cve_ids found in the source file to a list.
        # Return the list.
        for child in root.iter('cve'):
            cve_id_nessus.append(child.text)

        return cve_id_nessus

    def populate_table(self, table, filepath, bussiness_info):
        cve_id_nessus = []
        cve_id_nessus = self.parse_xml(filepath)

        db_handler = HandleDB()
        vuln_list = []
        row_counter = 0 
        
        # create the list of vuln objects for each cve
        # id that is a match from the nessus file
        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                vuln_list.append(VulnInfo(cve, bussiness_info))

        # set row count to the number of vulns found
        table.setRowCount(vuln_list.__len__())

        # populate the table with the vuln info
        # for each vuln in the vuln list
        # Each item has to be a str for it to work
        for vuln in vuln_list:
            table.setItem(
                row_counter, 0, QtWidgets.QTableWidgetItem(str(vuln.cve_id)))
            table.setItem(
                row_counter, 1, QtWidgets.QTableWidgetItem(str(vuln.cost_hour)))
            table.setItem(
                row_counter, 2, QtWidgets.QTableWidgetItem(str(vuln.total_hours)))
            table.setItem(
                row_counter, 3, QtWidgets.QTableWidgetItem(vuln.description))
            row_counter += 1

        """
        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                description = db_handler.pull_description(
                    cve)  # pull matching description from db
                # pull matching cost from db
                cost_hours = db_handler.pull_cost_hrs(cve)
                total_hours = db_handler.pull_total_hrs(cve)
                table.setItem(row_counter_2, 0,
                              QtWidgets.QTableWidgetItem(cve))  # set first column to cve_id
                table.setItem(row_counter_2, 1,
                              QtWidgets.QTableWidgetItem(str(cost_hours[0])))  # set secound column to cost
                table.setItem(row_counter_2, 2,
                              QtWidgets.QTableWidgetItem(str(total_hours[0])))  # set third column to total hours
                # remove the brackets and the junk at the end from description
                description = description[2:-5]
                table.setItem(row_counter_2, 3,
                              QtWidgets.QTableWidgetItem(description))  # set third column to description
                row_counter_2 = row_counter_2 + 1
        """
