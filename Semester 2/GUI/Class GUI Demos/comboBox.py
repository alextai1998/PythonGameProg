import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QSpinBox, QComboBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('ComboBox')

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Rice Paper Spring Rolls w/ Shrimp 10k")
        self.comboBox.addItem("Deep Fried Spring Rolls 200k")
        self.comboBox.addItem("Fried Calamari 50k")
        self.comboBox.addItem("S'mores 12k")
        self.comboBox.move(30, 55)

        self.show()


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
