# Author: Nicholas Natale
# Created: 11/2/22
# Edited: 11/2/22

# This file is an action handler file for the Run Scan window of the
# Cost Benefit Analysis Tool. 

from RunScanWindow import Ui_RunScanWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class RunScanGUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setup the UI for the Run Analysis window
        self.ui = Ui_RunScanWindow()
        self.ui.setupUi(self)

    def show_gui(self):
        self.rsg = RunScanGUI()
        self.rsg.show()