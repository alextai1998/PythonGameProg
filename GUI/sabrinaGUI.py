# QCalendarWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate


class Cal(QWidget):
    def __init__(self):
        super(Cal, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Calender Demo')

        # --- add a start button
        self.cal1 = QCalendarWidget(self)
        self.cal1.setGridVisible(True)
        self.cal1.move(20, 40)
        self.cal1.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = self.cal1.selectedDate()
        self.label.setText(date.toString())
        self.label.move(20, 20)

        self.show()

    def showDate(self, date):
        self.label.setText(date.toString())



# --- main program
app = QApplication(sys.argv)
ex = Cal()
ex.show()
sys.exit(app.exec_())
