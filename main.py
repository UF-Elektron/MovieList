import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

class AddEntry(QWidget):

    def __init__(self):
        super().__init__()

        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        # ...
        self.setLayout(vbox)

        # Set size of the window
        self.resize(400, 150)
        # Set position on the screen
        self.move(400, 400)
        self.setWindowTitle('New window')

        print('Counter window initialized')

    def test(self):
        print("Test")

class MainWindow(QWidget):
    sliderW = 0

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.dialog = AddEntry()

        # Set size of the window
        self.resize(600, 400)
        # Set window position on screen
        self.move(800, 500)
        self.setWindowTitle('Movie List')

        # Create pushbuttons
        #-------------------
        # Create pushbutton that closes the window
        btnAdd = QPushButton('Add', self)
        btnAdd.clicked.connect(self.addEntry)
        btnAdd.resize(btnAdd.sizeHint())

    #    newLabel = QStringList()
        newWidget = QTableWidget()
        newWidget.setRowCount(4)
        newWidget.setColumnCount(8)
        myList = ['Movie Title', 'Times watched', 'Genres']
        newWidget.setHorizontalHeaderLabels(myList)
        tableItem = QTableWidgetItem()
        tableItem.setText("This is my Movie")
        newWidget.setItem(0, 0, tableItem)

        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        vbox.addWidget(btnAdd)
        vbox.addWidget(newWidget)
        self.setLayout(vbox)

        # Show the already created window now on screen
        self.show()
        print('Main window initialized')

    def addEntry(self):
        self.dialog.test()

if __name__ == '__main__':

    # Create application object
    app = QApplication(sys.argv)
    ex = MainWindow()
    # Enter the app mainloop
    sys.exit(app.exec_())
