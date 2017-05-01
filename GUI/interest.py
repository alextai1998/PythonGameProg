# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interest.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("font: 57 18pt \"Helvetica Neue\";\n"
"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 341, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setBaseSize(QtCore.QSize(0, 0))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_2.setReadOnly(False)
        self.doubleSpinBox_2.setMaximum(10000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setBaseSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Principal:"))
        self.label_2.setText(_translate("Form", "Rate:"))
        self.doubleSpinBox.setSuffix(_translate("Form", "%"))
        self.label_3.setText(_translate("Form", "Years:"))
        self.label_4.setText(_translate("Form", "Amount"))
        self.doubleSpinBox_2.setPrefix(_translate("Form", "$"))
        self.comboBox.setItemText(0, _translate("Form", "1 year"))
        self.comboBox.setItemText(1, _translate("Form", "2 years"))
        self.comboBox.setItemText(2, _translate("Form", "3 years"))
        self.comboBox.setItemText(3, _translate("Form", "4 years"))
        self.comboBox.setItemText(4, _translate("Form", "5 years"))
        self.comboBox.setItemText(5, _translate("Form", "6 years"))
        self.comboBox.setItemText(6, _translate("Form", "7 years"))
        self.comboBox.setItemText(7, _translate("Form", "8 years"))
        self.comboBox.setItemText(8, _translate("Form", " 9 years"))
        self.comboBox.setItemText(9, _translate("Form", "10 years"))

