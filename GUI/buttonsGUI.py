import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QSpinBox, QComboBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Buttons')


        # --- add a push button
        self.btn1 = QPushButton('Button A', self)
        self.btn1.setToolTip('This is Button A!')
        self.btn1.resize(250, 90)
        self.btn1.move(55, 30)
        self.btn1.clicked.connect(self.change2a)

        # --- add a push button
        self.btn2 = QPushButton('Button B', self)
        self.btn2.setToolTip('This is Button B!')
        self.btn2.resize(250, 100)
        self.btn2.move(55, 130)
        self.btn2.clicked.connect(self.change2b)

        self.show()

    def change2a(self):
        self.setWindowTitle('Button A clicked!')

    def change2b(self):
        self.setWindowTitle('Button B clicked!')


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
