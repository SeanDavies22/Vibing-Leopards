import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from handle_db import *
import xml.etree.ElementTree as ET


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        filepath = "C:\\Users\\Casey\\Documents\\Github\\Vibing-Leopards\\My_Basic_Network_Scan.nessus"
        file = open(filepath, "r")
        cve_id_nessus = []
        self.tableWidget = QTableWidget()

        # This is suppose to create the tree thing so
        # that we can parse the nessus file
        tree = ET.ElementTree(file=file)
        root = tree.getroot()

        # add the cve_ids found in the file to a list
        # return that list
        cve_id_nessus = []
        db_handler = HandleDB()
        total_cost = []
        description = []
        counter_2 = 0  # counter for what row we are on.. might not need
        counter = 0  # counter for # of columns.. was going to try setRow here but didn't do anything

        for child in root.iter('cve'):
            cve_id_nessus.append(child.text)

        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                counter = counter + 1

       # for cve in cve_id_nessus:
        #    print(cve)

        self.tableWidget.setRowCount(counter)
        self.tableWidget.setColumnCount(3)

        for cve in cve_id_nessus:
            if db_handler.check_cve_id(cve):
                description = db_handler.pull_description(
                    cve)  # pull matching description from db
                # total_cost = db_handler.pull_cost(
                # cve)  # pull matching cost from db
                self.tableWidget.setItem(counter_2, 0,
                                         QTableWidgetItem(cve))  # set first column to cve_id
                self.tableWidget.setItem(counter_2, 1,
                                         QTableWidgetItem(10))  # set secound column to cost
                self.tableWidget.setItem(counter_2, 2,
                                         QTableWidgetItem(description))  # set third column to description
                counter_2 = counter_2 + 1
            else:  # on no match just set the cve_id coulmn to test.. to see if we can print anything
                self.tableWidget.insertRow(counter_2)
                self.tableWidget.setItem(counter_2, 0,
                                         QTableWidgetItem("test"))
                counter_2 = counter_2 + 1

        self.tableWidget.show()

       # self.tableWidget = QTableWidget()
     #   self.tableWidget.setRowCount(4)
      #  self.tableWidget.setColumnCount(2)
      #  self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
     #   self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
      #  self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
      #  self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
      #  self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
      #  self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
      #  self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
     #  self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
       # self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
