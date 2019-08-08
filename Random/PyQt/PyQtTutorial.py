from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class mainWindow(QMainWindow):                          # Inherit the QMainWindow functionality
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setGeometry(300, 300, 300, 300)             # xpos, ypos, width, height   
        self.setWindowTitle("PyQt5 Tutorial")            # set window title
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)                   # Create a label in the instance (self)
        self.label.setText("My First Label")                 # Set the label's text
        self.label.move(50,50)                               # Set the label's position

        self.b1 = QtWidgets.QPushButton(self)                 # Create button in win
        self.b1.setText("Click me")                          # Set button text
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def clicked():
    print("clicked")
    return


def window():
    app = QApplication(sys.argv)
    win = mainWindow()                             # Create a window

    #win.setGeometry(300, 300, 300, 300)             # xpos, ypos, width, height   
    #win.setWindowTitle("PyQt5 Tutorial")            # set window title

    #label = QtWidgets.QLabel(win)                   # Create a label in win
    #label.setText("My First Label")                 # Set the label's text
    #label.move(50,50)                               # Set the label's position

    #b1 = QtWidgets.QPushButton(win)                 # Create button in win
    #b1.setText("Click me")                          # Set button text
    #b1.clicked.connect(clicked)

    win.show()                                      # Show the window
    sys.exit(app.exec_())                           # Exit's when window's x is closed

window()                                            # Call the window function


