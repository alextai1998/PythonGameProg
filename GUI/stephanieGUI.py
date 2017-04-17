# QLabel
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class Label(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('QLabel Demo')

        # --- add a label
        self.label1 = QLabel(self)
        self.label1.setText('Python Class')
        self.label1.move(390, 40)

        # --- add a label
        self.label2 = QLabel(self)
        self.label2.setToolTip('https://goo.gl/pB9kmb')
        self.label2.setText("<a href='https://goo.gl/pB9kmb'>Surprise URL</a>")
        self.label2.move(390, 90)
        self.label2.setOpenExternalLinks(True)

        # --- add a label
        self.label3 = QLabel(self)
        self.label3.move(80, 130)
        self.label3.setPixmap(QPixmap('hello.png'))

        self.show()


# --- main program
app = QApplication(sys.argv)
ex = Label()
sys.exit(app.exec_())
