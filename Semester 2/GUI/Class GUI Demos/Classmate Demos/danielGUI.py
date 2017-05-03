# QProgressBar
import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal


class Thread(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.update.emit(100)
        for index in range(1, 101):
            self.update.emit(index)
            time.sleep(0.01)


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.thread = Thread()
        self.thread.set_max.connect(self.set_max)
        self.thread.update.connect(self.set_value)


    def setupUI(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('ProgressBar')

        # --- add a start button
        self.button_start = QPushButton("Start", self)
        self.button_start.resize(150, 40)
        self.button_start.move(50, 50)
        self.button_start.clicked.connect(self.start)

        # --- add a stop button
        self.button_stop = QPushButton("End", self)
        self.button_stop.resize(150, 40)
        self.button_stop.move(50, 90)
        self.button_stop.clicked.connect(self.stop)

        # --- add a progress bar
        self.pb = QProgressBar(self)
        self.pb.resize(150, 100)
        self.pb.move(50, 130)

        self.show()

    def start(self):
        self.thread.start()

    def stop(self):
        self.thread.terminate()

    def set_max(self, data):
        self.pb.setMaximum(data)

    def set_value(self, data):
        self.pb.setValue(data)


# --- main program
app = QApplication(sys.argv)
ex = ProgressBar()
ex.show()
sys.exit(app.exec_())
