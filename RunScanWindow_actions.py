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
import pandas as pd
import math
sys.path.append(os.getcwd())


class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, filePath, bussiness_size, business_type, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.filePath = filePath
        self.business_size = 0
        self.business_type = 0
        self.total_cost = 0
        self.file_extension = os.path.splitext(self.filePath)[1]
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)

        # Make Tab a shortcut to go down a row
        self.grabShortcut = QtWidgets.QShortcut(
            QtGui.QKeySequence("Tab"), self)
        self.grabShortcut.activated.connect(self.move_down_row)

        # Setup the table
        if (self.file_extension == '.xlsx'):
            self.load_saved_table(self.ui.dataTable, self.filePath)
        else:
            self.populate_new_table(self.ui.dataTable, self.filePath)
            self.business_size = bussiness_size
            self.business_type = business_type
            self.total_cost = self.get_total_cost()

        self.ui.dataTable.resizeColumnsToContents()
        self.ui.dataTable.resizeRowsToContents()

        # Setup the analysis labels.
        self.ui.totalCostLabel.setText(
            "The total cost for all vulnerabilities is: $" + str(self.total_cost))

        # Action handling methods.
        self.ui.dataTable.cellDoubleClicked.connect(
            self.cve_id_table_cell_pressed)
        self.ui.actionSave.triggered.connect(self.exporter)

    # This function allows the user to use tab to move down a row.
    def move_down_row(self):
        for cell in self.ui.dataTable.selectionModel().selectedIndexes():
            column = cell.column()
            row = cell.row() + 1
            self.ui.dataTable.setCurrentCell(row, column)

            # If column is comments, let the user edit the cell.
            if (column == 6):
                self.ui.dataTable.editItem(
                    self.ui.dataTable.item(row, column))

    # This function handles the cv_id table cell being pressed.
    # Shows a popup box with that cv_id vulnerability information
    # If the cell being clicked is the cv_id.
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
                num_rate = float(rate)
                print("inside cve_id_table_cell_pressed")
                print(self.business_size)
                print(self.business_type)
                total_cost = round(
                    (num_hours * num_rate * self.business_size * self.business_type), 2)

                self.show_info_pop_up("The pay rate for this vulnerability is: $" + str(rate) + " per hour." +
                                      "\n\nThe engineering hours required to fix this: " + str(hours) + " hrs." +
                                      "\n\nThe total cost for fixing this vulnerability is: $" + str(total_cost) +
                                      "\n\nThe severity of this vulnerability is: " + str(severity_full_text) + ".", cve_id=cve_id)

            # If column is comments, let the user edit the cell.
            elif (column == 6):
                row = cell.row()
                self.ui.dataTable.editItem(self.ui.dataTable.item(row, column))

    # Lets the user save the table to an excel file.
    def exporter(self, filename=None):
        if not filename:
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, 'Save File', " "'.xlsx', '(*.xlsx)')

        if filename[0]:
            print(filename[0])
            work_book = xlsxwriter.Workbook(filename[0])
            work_sheet = work_book.add_worksheet()
            bold = work_book.add_format({'bold': True})

            # Write the headers and set the column widths.
            for col in range(self.ui.dataTable.columnCount()):
                if self.ui.dataTable.horizontalHeaderItem(col).text() == "Comments":
                    work_sheet.set_column(col, col, 50)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "CVE ID":
                    work_sheet.set_column(col, col, 13.29)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Severity":
                    work_sheet.set_column(col, col, 7.57)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Rate per hr":
                    work_sheet.set_column(col, col, 10)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Engineering Hrs":
                    work_sheet.set_column(col, col, 14.29)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "Description":
                    work_sheet.set_column(col, col, 241)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)
                elif self.ui.dataTable.horizontalHeaderItem(col).text() == "OS":
                    work_sheet.set_column(col, col, 12.57)
                    work_sheet.write(
                        0, col, self.ui.dataTable.horizontalHeaderItem(col).text(), bold)

            # Reset the row and column to print out the table
            row = 0
            col = 0

            # Print out the table to the excel file.
            for col in range(self.ui.dataTable.columnCount()):
                for row in range(self.ui.dataTable.rowCount()):
                    try:
                        text = str(self.ui.dataTable.item(row, col).text())

                        # +1 to skip the header
                        if text.isnumeric():
                            work_sheet.write_number(row + 1, col, float(text))

                        elif text.replace('.', '', 1).isdigit():
                            work_sheet.write_number(row + 1, col, float(text))

                        else:
                            work_sheet.write(row + 1, col, text)
                    except AttributeError:
                        # If there is an Error, just move on instead of crashing the whole program.
                        pass

            # Write the rest of the info on the row after the table.
            # Most of this will be used to repopulate the table on reload.
            row = self.ui.dataTable.rowCount() + 1
            col = 0
            work_sheet.write(row, col, "Total Cost", bold)
            col += 1
            work_sheet.write(row, col, float(self.total_cost))
            col += 1
            work_sheet.write(row, col, "business size", bold)
            col += 1
            work_sheet.write(row, col, int(self.business_size))
            col += 1
            work_sheet.write(row, col, "business type", bold)
            col += 1
            work_sheet.write(row, col, int(self.business_type))

        work_book.close()

    def show_gui(self):
        self.rsg = RunScanGUI(
            self.filePath, self.business_size, self.business_type)
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

    # load the saved table from a excel file
    def load_saved_table(self, table, filepath):
        dataframe = pd.read_excel(filepath)
        dataframe = dataframe.fillna("")
        end_loop = False
        table.setRowCount(dataframe.shape[0])

        if (dataframe.count == 0):
            self.show_error_pop_up(
                "Source file has no elements.")

        # populate the table with the vuln info
        for row in range(dataframe.shape[0]):
            if end_loop:
                break
            for col in range(dataframe.shape[1]):

                # We've reached the end of the table and can repopulate total_info and business_info
                if (dataframe.iat[row, col] == "Total Cost"):
                    # We don't want to show 'total cost' in the table
                    table.setItem(row, col, QtWidgets.QTableWidgetItem(""))

                    # Actual value is always one to the right of "Total Cost" cell
                    self.total_cost = dataframe.iat[row, col + 1]
                    # Bussiness_size info
                    self.business_size = dataframe.iat[row, col + 3]
                    print("inside load_saved_table")
                    print(self.business_size)
                    # Bussiness_type info
                    self.business_type = dataframe.iat[row, col + 5]
                    print(self.business_type)
                    end_loop = True

                if not end_loop:
                    table.setItem(row, col, QtWidgets.QTableWidgetItem(
                        str(dataframe.iat[row, col])))
            if end_loop:
                break  # break out of loop so we don't print total_info and business_info to table

    # populate the table with matches from nesssus file

    def populate_new_table(self, table, filepath):
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
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Firefox"))
            elif "Safari" in vuln.description:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Safari"))
            elif "Edge" in vuln.description:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Edge"))
            elif "Windows" in vuln.description:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Windows"))
            elif "Linux" in vuln.description:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Linux"))
            elif "Mac" in vuln.description:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Mac"))
            else:
                table.setItem(row_counter, 4,
                              QtWidgets.QTableWidgetItem("Unknown"))

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
        try:

            for row in range(self.ui.dataTable.rowCount()):
                temp_sum += float(self.ui.dataTable.item(row, 1).text()) * \
                    float(self.ui.dataTable.item(row, 2).text())
            total_cost = temp_sum * self.business_size * self.business_type
        except ValueError:
            self.show_error_pop_up(
                "Error calculating total cost. Please check your data.")
            total_cost = 0
        return total_cost
