# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findReplaceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self):
        self.lyrics = """[Verse 1: Zara Larsson]
I’ve been hearing symphonies
Before all I heard was silence
A rhapsody for you and me
And every melody is timeless
Life was stringing me along
Then you came and you cut me loose
Was solo singing on my own
Now I can’t find the key without you

[Pre-Chorus: Zara Larsson]
And now your song is on repeat
And I’m dancin' on, to your heartbeat
And when you’re gone, I feel incomplete
So if you want the truth

[Chorus: Zara Larsson]
I just wanna be part of your symphony
Will you hold me tight and not let go?
Symphony
Like a love song on the radio
Will you hold me tight and not let go?"""

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(552, 232)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 527, 206))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainBox.setContentsMargins(0, 0, 0, 0)
        self.mainBox.setObjectName("mainBox")
        self.leftSide = QtWidgets.QVBoxLayout()
        self.leftSide.setObjectName("leftSide")
        self.lineEdits = QtWidgets.QHBoxLayout()
        self.lineEdits.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.lineEdits.setObjectName("lineEdits")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.find_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.find_lb.setFont(font)
        self.find_lb.setObjectName("find_lb")
        self.verticalLayout_4.addWidget(self.find_lb)
        self.replace_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.replace_lb.setObjectName("replace_lb")
        self.verticalLayout_4.addWidget(self.replace_lb)
        self.lineEdits.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.find_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.find_le.setWhatsThis("")
        self.find_le.setAccessibleName("")
        self.find_le.setInputMask("")
        self.find_le.setText("")
        self.find_le.setFrame(False)
        self.find_le.setPlaceholderText("")
        self.find_le.setClearButtonEnabled(True)
        self.find_le.setObjectName("find_le")
        self.verticalLayout_3.addWidget(self.find_le)
        self.replace_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.replace_le.setObjectName("replace_le")
        self.verticalLayout_3.addWidget(self.replace_le)
        self.lineEdits.addLayout(self.verticalLayout_3)
        self.leftSide.addLayout(self.lineEdits)
        self.checkboxes = QtWidgets.QHBoxLayout()
        self.checkboxes.setObjectName("checkboxes")
        self.checkbox1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkbox1.setObjectName("checkbox1")
        self.checkboxes.addWidget(self.checkbox1)
        self.checkbox2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkbox2.setObjectName("checkbox2")
        self.checkboxes.addWidget(self.checkbox2)
        self.leftSide.addLayout(self.checkboxes)
        self.comboBoxes = QtWidgets.QHBoxLayout()
        self.comboBoxes.setObjectName("comboBoxes")
        self.syntax_lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.syntax_lb.sizePolicy().hasHeightForWidth())
        self.syntax_lb.setSizePolicy(sizePolicy)
        self.syntax_lb.setObjectName("syntax_lb")
        self.comboBoxes.addWidget(self.syntax_lb)
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.comboBoxes.addItem(spacerItem)
        self.litreg_combo = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.litreg_combo.setObjectName("litreg_combo")
        self.litreg_combo.addItem("")
        self.litreg_combo.addItem("")
        self.comboBoxes.addWidget(self.litreg_combo)
        self.leftSide.addLayout(self.comboBoxes)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.leftSide.addItem(spacerItem1)
        self.mainBox.addLayout(self.leftSide)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainBox.addWidget(self.line)
        self.rightSide = QtWidgets.QVBoxLayout()
        self.rightSide.setObjectName("rightSide")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.find)
        self.rightSide.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.replace)
        self.rightSide.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.replaceAll)
        self.rightSide.addWidget(self.pushButton_3)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rightSide.addItem(spacerItem2)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.rightSide.addWidget(self.pushButton_4)

        self.mainBox.addLayout(self.rightSide)
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.find_lb.setText(_translate("Form", "Find what:"))
        self.replace_lb.setText(_translate("Form", "Replace with:"))
        self.checkbox1.setText(_translate("Form", "Case sensitive"))
        self.checkbox2.setText(_translate("Form", "Whole words"))
        self.syntax_lb.setText(_translate("Form", "Syntax:"))
        self.litreg_combo.setItemText(0, _translate("Form", "Literal Text"))
        self.litreg_combo.setItemText(1, _translate("Form", "Regular Expression"))
        self.pushButton.setText(_translate("Form", "Find"))
        self.pushButton_2.setText(_translate("Form", "Replace"))
        self.pushButton_3.setText(_translate("Form", "Replace All"))
        self.pushButton_4.setText(_translate("Form", "Close"))

    def find(self):
        word = self.find_le.text()
        textlist = self.lyrics.split()
        self.results = []
        for idx, w in enumerate(textlist):
            if w == word:
                self.results.append(idx)
        print(self.results)

    def replaceAll(self):
        self.lyrics = self.lyrics.replace(self.find_le.text(), self.replace_le.text())
        print(self.lyrics)

    def replace(self):
        self.lyrics = self.lyrics.replace(self.find_le.text(), self.replace_le.text(), 1)
        print(self.lyrics)
