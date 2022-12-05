# Author: Nicholas Natale, Casey Staples
# Created: 11/2/22
# Edited: 11/28/22

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
import math
sys.path.append(os.getcwd()) 


class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, filePath, bussiness_size, business_type, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.filePath = filePath
        self.business_size = bussiness_size
        self.business_type = business_type
        self.total_cost = 0
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)
        self.populate_table(self.ui.dataTable, self.filePath)
        self.ui.dataTable.resizeColumnsToContents()
        self.ui.dataTable.resizeRowsToContents()
        self.total_cost = self.get_total_cost()

        # Setup the analysis labels.
        self.ui.totalCostLabel.setText("The total cost for all vulnerabilities is: $" + str(self.total_cost))

        # Action handling methods.
        self.ui.dataTable.cellDoubleClicked.connect(
            self.cve_id_table_cell_pressed)
        self.ui.actionSave.triggered.connect(self.exporter)


    # allow the column to be edited by user
    def cve_id_table_edit_comment(self):
        for cell in self.ui.dataTable.selectionModel().selectedIndexes():
            column = cell.column()
            if (column == 4):
                self.ui.dataTable.editItem(self.ui.dataTable.item(cell.row(), cell.column()))
                

    def cve_id_table_cell_pressed(self):
        for cell in self.ui.dataTable.selectionModel().selectedIndexes():
            column = cell.column()
            if (column == 0):
                row = cell.row()
                cve_id = self.ui.dataTable.item(row, 0).text()
                rate = self.ui.dataTable.item(row, 1).text()
                hours = self.ui.dataTable.item(row, 2).text()
                severity = self.ui.dataTable.item(row, 3).text()
                if severity == 'H':
                    severity_full_text = "High"
                elif severity == "M":
                    severity_full_text = "Medium"
                elif severity == "L":
                    severity_full_text = "Low"

                num_hours = float(hours)
                num_rate = int(rate)
                business_size = float(self.business_size)
                business_type = float(self.business_type)
                total_cost = round((num_hours * num_rate * business_size * business_type), 2)

                self.show_info_pop_up("The pay rate for this vulnerability is: $" + str(rate) + " per hour." + 
                                      "\n\nThe engineering hours required to fix this: " + str(hours) + " hrs." +  
                                      "\n\nThe total cost for fixing this vulnerability is: $" + str(total_cost) + 
                                      "\n\nThe severity of this vulnerability is: " + str(severity_full_text) + ".", cve_id=cve_id) 
            elif (column == 6):
                row = cell.row()
                self.ui.dataTable.editItem(self.ui.dataTable.item(row, column))

    # Let's the user save the table to an excel file.     
    def exporter(self, filename=None):
        if not filename:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, 'Save File', " "'.xlsx', '(*.xlsx)')

        if filename[0]:
            print(filename[0])
            work_book = xlsxwriter.Workbook(filename[0])
            work_sheet = work_book.add_worksheet()
            bold = work_book.add_format({'bold': True})
            for col in range(self.ui.dataTable.columnCount()):
                if self.ui.dataTable.horizontalHeaderItem(col).text() == "Comments":
                    work_sheet.set_column(col, col, 50)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "CVE ID":
                    work_sheet.set_column(col, col, 55)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Severity":
                    work_sheet.set_column(col, col, 30)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Rate per hr":
                    work_sheet.set_column(col, col , 30)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Engineering Hrs":
                    work_sheet.set_column(col, col ,30)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Description":
                    work_sheet.set_column(col, col ,200)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "OS":
                    work_sheet.set_column(col, col, 30)
                    work_sheet.write(0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
            row = 1
            col = 0
            for i in range(self.ui.dataTable.columnCount()):
                for x in range(self.ui.dataTable.rowCount()):
                    try:
                        text = str(self.ui.dataTable.item(row, col).text())
                        work_sheet.write(row, col, str(text))
                        row += 1
                    except AttributeError:
                        row += 1
                row = 1
                col += 1
            row = self.ui.dataTable.rowCount() + 1
            col = 2
            try :
                work_sheet.write(row, col, "Total Cost", bold)
            except AttributeError:  
                pass
            row += 1
            try :
                work_sheet.write(row, col, str(self.total_cost))
            except AttributeError:
                pass
        work_book.close()

    def show_gui(self):
        self.rsg = RunScanGUI(self.filePath, self.business_size, self.business_type)
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

    def populate_table(self, table, filepath):
        cve_id_nessus = []
        cve_id_nessus = self.parse_xml(filepath)

        db_handler = HandleDB()
        vuln_list = []
        row_counter = 0 
        
        # create the list of vuln objects for each cve
        # id that is a match from the nessus file
        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                vuln_list.append(VulnInfo(cve))

        # set row count to the number of vulns found
        table.setRowCount(vuln_list.__len__())


        if (len(vuln_list) == 0):
            self.show_error_pop_up(
                "Source file has no elements.")

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
                row_counter, 3, QtWidgets.QTableWidgetItem(str(vuln.severity)))
            table.setItem(
                row_counter, 5, QtWidgets.QTableWidgetItem(vuln.description))
            if "Chrome" in vuln.description:
                table.setItem(
                    row_counter, 4, QtWidgets.QTableWidgetItem("Chromuim"))
            elif "FireFox" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Firefox"))
            elif "Safari" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Safari"))
            elif "Edge" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Edge"))
            elif "Windows" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Windows"))
            elif "Linux" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Linux"))
            elif "Mac" in vuln.description:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Mac"))
            else:
                table.setItem(row_counter, 4, QtWidgets.QTableWidgetItem("Unknown"))

            table.setItem(row_counter, 6, QtWidgets.QTableWidgetItem(None))
            row_counter += 1
            

    def show_error_pop_up(self, errorMessage):
            msg = QtWidgets.QMessageBox()
            msg.setText(errorMessage)
            msg.setWindowTitle("File Explorer")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            x = msg.exec_()

    def show_info_pop_up(self, infoMessage, cve_id):
            msg = QtWidgets.QMessageBox()
            msg.setText(infoMessage)
            msg.setWindowTitle(cve_id)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            x = msg.exec_()

    def get_total_cost(self):
        temp_sum = 0
        for row in range(self.ui.dataTable.rowCount()):
            temp_sum += float(self.ui.dataTable.item(row, 1).text()) * float(self.ui.dataTable.item(row, 2).text())
        total_cost = temp_sum * self.business_size * self.business_type

        return total_cost
