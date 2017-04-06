import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QSpinBox, QComboBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Vietnamese Spring Roll Calories Converter')

        # --- add a numeric-input box
        self.num = QSpinBox(self)
        self.num.resize(250, 30)
        self.num.setSuffix(" rolls")
        self.num.move(55, 90)

        # --- add a push button
        self.btn1 = QPushButton('Convert', self)
        self.btn1.setToolTip('Click to convert into calories!')
        self.btn1.resize(250, 20)
        self.btn1.move(55, 140)
        self.btn1.clicked.connect(self.convert)

        # --- add a text box with default text
        self.text1 = QTextEdit(self)
        self.text1.resize(250, 40)
        self.text1.move(55, 180)
        self.text1.setPlaceholderText("Answers will display here!")

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Rice Paper Spring Rolls w/ Shrimp")
        self.comboBox.addItem("Deep Fried Spring Rolls")
        self.comboBox.move(50, 50)

        self.show()

    def convert(self):
        rolls = int(self.num.value())
        # Condition here to determine calories per roll
        #
        # if self.comboBox == "Rice Paper Spring Rolls w/ Shrimp":
        #     calories = rolls * 81
        # else:
        #     calories = rolls * 178
        self.text1.insertPlainText(str(self.comboBox))
        # str(calories) + " calories! "


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
