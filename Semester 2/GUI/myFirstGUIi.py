import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Second GUI')

        # --- add a push button
        self.btn1 = QPushButton('My First Button', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(200, 20)
        self.btn1.move(50, 50)

        # --- add a text box with default text
        self.text1 = QTextEdit(self)
        self.text1.resize(200, 40)
        self.text1.move(50, 80)
        self.text1.setPlaceholderText("This is a EditText Widget")

        # --- add a numeric-input box
        self.num = QDoubleSpinBox(self)
        self.num.setMaximum(200)
        self.num.setMinimum(10)
        self.num.setSuffix(" cm")
        self.num.resize(200, 30)
        self.num.move(50, 130)

        self.show()

# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
