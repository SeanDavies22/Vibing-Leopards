import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

# Main window for the Cost-Benefit Analysis Tool.
class MainWindow(QWidget):

    def __init__(self):  #Constructor to setup the main window. Will set up this way whenever called.
        super(MainWindow, self).__init__()

        # The main window is a vertical stack, meaning any added widgets will 
        # be added in a vertical fashion. 
        self.layout = QVBoxLayout()

        # Set up the main header label.
        self.header = QLabel("Cost-Benefit Analysis Tool")
        self.header.setFont(QFont('Helvetica', 20, QFont.Bold))
        self.header.setAlignment(QtCore.Qt.AlignHCenter)

        # Set up the exit button.
        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet("background-color: grey")

        # Set up the window style.
        self.setWindowTitle("Cost-Benefit Analysis Tool")
        self.setStyleSheet("background-color: cyan")
        self.setLayout(self.layout)
        
        # Closes the window when Exit button pressed.
        self.exitButton.clicked.connect(self.close)

        # Add these widgets to the main window after setup.
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.exitButton)
        
if __name__ == "__main__":  # If the file was run directly and not imported by another Python file.
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())