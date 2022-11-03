# Author: Nicholas Natale
# Created: 11/2/22
# Edited: 11/3/22

# This file is an action handler for the Run Analysis window of the
# Cost Benefit Analysis Tool. 

from RunScanWindow import Ui_RunScanWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET

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
        
        tree = ET.parse(filePath)
        root = tree.getroot()
        elementList = []

        # Append each element tag in the tree to the list.
        for element in tree.iter():
            elementList.append(element.tag)

        # Sort the list for multiple occurences. 
        elementList = list(set(elementList))

        # Putting this here temporarily. 
        # Print XML elements to pop up window. Will be changed.
        # Done like this for demo. 
        elementString = ""
        for i in elementList:
            elementString = elementString + i + ", "

        msg = QtWidgets.QMessageBox()
        msg.setText("Elements Found: " + elementString)
        msg.setWindowTitle("File Explorer")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
