import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton



def clicked():
        print("Button clicked!")


class MainWindow(QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.layout = QVBoxLayout()
        self.label = QLabel("My text is being displayed here without any problems. Finally.")

        self.b1 = QPushButton()
        self.b1.setText("Click Me!")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.b1)
        self.setWindowTitle("Cost-Benefit Analysis Tool")
        self.setLayout(self.layout)
        

        self.b1.clicked.connect(clicked)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())