import sys
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QSpinBox, QComboBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Grade Converter')

        # --- add a text box with default text
        self.text1 = QLineEdit(self)
        self.text1.resize(250, 40)
        self.text1.move(50, 70)
        self.text1.textChanged.connect(self.convert)
        self.text1.setPlaceholderText('Enter grade 0-100')
        self.text1.setValidator(QIntValidator(0, 100, self))

        # --- add a text box with default text
        self.text2 = QLineEdit(self)
        self.text2.resize(250, 40)
        self.text2.move(50, 130)
        self.text2.setPlaceholderText('Letter Grade')


        self.show()

    def convert(self):
        text = int(self.text1.text())
        letters = {'A+': range(97, 101), 'A': range(93, 97),  'A-': range(90, 93), 'B+': range(87, 90),
                   'B':  range(83, 87),  'B-': range(80, 83), 'C+': range(77, 80), 'C':  range(77, 73),
                   'C-': range(70, 73),  'D+': range(67, 70), 'D': range(63, 67),  'D-': range(60, 63),
                   'F': range(0, 60)}
        for j, i in letters.items():
                if text in i:
                    self.text2.setText(j)


# --- main program
app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
