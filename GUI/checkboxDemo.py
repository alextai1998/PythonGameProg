import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QSpinBox, QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('CheckBox Demonstration')

        # --- add a checkbox
        self.check = QCheckBox('This is a checkbox!', self)
        self.check.resize(250, 30)
        self.check.move(100, 90)
        self.check.stateChanged.connect(self.dosth)

        self.show()

    def dosth(self):
        self.setWindowTitle('The checkbox was checked!')


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
