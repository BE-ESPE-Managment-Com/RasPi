# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project_GUI_V6.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1256, 600)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 120, 881, 421))
        self.label.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Sans-titre-2.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.Battery_level = QtGui.QProgressBar(Form)
        self.Battery_level.setGeometry(QtCore.QRect(320, 550, 261, 31))
        self.Battery_level.setProperty("value", 24)
        self.Battery_level.setObjectName(_fromUtf8("Battery_level"))
        self.logo_INSA_4 = QtGui.QLabel(Form)
        self.logo_INSA_4.setGeometry(QtCore.QRect(810, 260, 71, 41))
        self.logo_INSA_4.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Num3.png);"))
        self.logo_INSA_4.setText(_fromUtf8(""))
        self.logo_INSA_4.setObjectName(_fromUtf8("logo_INSA_4"))
        self.logo_INSA_2 = QtGui.QLabel(Form)
        self.logo_INSA_2.setGeometry(QtCore.QRect(810, 110, 71, 41))
        self.logo_INSA_2.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Num1.png);"))
        self.logo_INSA_2.setText(_fromUtf8(""))
        self.logo_INSA_2.setObjectName(_fromUtf8("logo_INSA_2"))
        self.logo_INSA_5 = QtGui.QLabel(Form)
        self.logo_INSA_5.setGeometry(QtCore.QRect(810, 340, 71, 41))
        self.logo_INSA_5.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Num4.png);"))
        self.logo_INSA_5.setText(_fromUtf8(""))
        self.logo_INSA_5.setObjectName(_fromUtf8("logo_INSA_5"))
        self.logo_INSA_6 = QtGui.QLabel(Form)
        self.logo_INSA_6.setGeometry(QtCore.QRect(810, 420, 71, 41))
        self.logo_INSA_6.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Num5.png);"))
        self.logo_INSA_6.setText(_fromUtf8(""))
        self.logo_INSA_6.setObjectName(_fromUtf8("logo_INSA_6"))
        self.logo_INSA_3 = QtGui.QLabel(Form)
        self.logo_INSA_3.setGeometry(QtCore.QRect(810, 190, 71, 41))
        self.logo_INSA_3.setStyleSheet(_fromUtf8("image: url(:/newPrefix/Num2.png);"))
        self.logo_INSA_3.setText(_fromUtf8(""))
        self.logo_INSA_3.setObjectName(_fromUtf8("logo_INSA_3"))
        self.state_ld_3 = QtGui.QLabel(Form)
        self.state_ld_3.setGeometry(QtCore.QRect(880, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.state_ld_3.setFont(font)
        self.state_ld_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.state_ld_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_ld_3.setObjectName(_fromUtf8("state_ld_3"))
        self.state_ld_1 = QtGui.QLabel(Form)
        self.state_ld_1.setGeometry(QtCore.QRect(880, 110, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.state_ld_1.setFont(font)
        self.state_ld_1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.state_ld_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_ld_1.setObjectName(_fromUtf8("state_ld_1"))
        self.state_ld_4 = QtGui.QLabel(Form)
        self.state_ld_4.setGeometry(QtCore.QRect(880, 340, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.state_ld_4.setFont(font)
        self.state_ld_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.state_ld_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_ld_4.setObjectName(_fromUtf8("state_ld_4"))
        self.state_ld_2 = QtGui.QLabel(Form)
        self.state_ld_2.setGeometry(QtCore.QRect(880, 190, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.state_ld_2.setFont(font)
        self.state_ld_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.state_ld_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_ld_2.setObjectName(_fromUtf8("state_ld_2"))
        self.state_ld_5 = QtGui.QLabel(Form)
        self.state_ld_5.setGeometry(QtCore.QRect(880, 420, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.state_ld_5.setFont(font)
        self.state_ld_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.state_ld_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_ld_5.setObjectName(_fromUtf8("state_ld_5"))
        self.batt_charg = QtGui.QLabel(Form)
        self.batt_charg.setGeometry(QtCore.QRect(300, 390, 61, 21))
        self.batt_charg.setObjectName(_fromUtf8("batt_charg"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 270, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Title = QtGui.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(380, 60, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.logo_INSA = QtGui.QLabel(Form)
        self.logo_INSA.setGeometry(QtCore.QRect(530, -20, 211, 101))
        self.logo_INSA.setStyleSheet(_fromUtf8("image: url(:/newPrefix/logo_insa_toulouse.png);"))
        self.logo_INSA.setText(_fromUtf8(""))
        self.logo_INSA.setObjectName(_fromUtf8("logo_INSA"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(980, 310, 241, 181))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Production_graphs = QtGui.QLabel(self.groupBox_2)
        self.Production_graphs.setGeometry(QtCore.QRect(20, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Production_graphs.setFont(font)
        self.Production_graphs.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(161, 241, 0);\n"
"border-color: rgb(0, 85, 0);"))
        self.Production_graphs.setAlignment(QtCore.Qt.AlignCenter)
        self.Production_graphs.setObjectName(_fromUtf8("Production_graphs"))
        self.Today_Button = QtGui.QPushButton(self.groupBox_2)
        self.Today_Button.setGeometry(QtCore.QRect(70, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Today_Button.setFont(font)
        self.Today_Button.setObjectName(_fromUtf8("Today_Button"))
        self.week_Button = QtGui.QPushButton(self.groupBox_2)
        self.week_Button.setGeometry(QtCore.QRect(70, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.week_Button.setFont(font)
        self.week_Button.setObjectName(_fromUtf8("week_Button"))
        self.Month_Button = QtGui.QPushButton(self.groupBox_2)
        self.Month_Button.setGeometry(QtCore.QRect(70, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Month_Button.setFont(font)
        self.Month_Button.setObjectName(_fromUtf8("Month_Button"))
        self.View_Button = QtGui.QPushButton(Form)
        self.View_Button.setGeometry(QtCore.QRect(770, 470, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.View_Button.setFont(font)
        self.View_Button.setObjectName(_fromUtf8("View_Button"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 320, 251, 181))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Production = QtGui.QLabel(self.groupBox_3)
        self.Production.setGeometry(QtCore.QRect(40, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Production.setFont(font)
        self.Production.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(161, 241, 0);\n"
"border-color: rgb(0, 85, 0);"))
        self.Production.setAlignment(QtCore.Qt.AlignCenter)
        self.Production.setObjectName(_fromUtf8("Production"))
        self.Prod_power = QtGui.QLabel(self.groupBox_3)
        self.Prod_power.setGeometry(QtCore.QRect(10, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Prod_power.setFont(font)
        self.Prod_power.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 0);"))
        self.Prod_power.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Prod_power.setObjectName(_fromUtf8("Prod_power"))
        self.Prod_current = QtGui.QLabel(self.groupBox_3)
        self.Prod_current.setGeometry(QtCore.QRect(10, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Prod_current.setFont(font)
        self.Prod_current.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Prod_current.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Prod_current.setObjectName(_fromUtf8("Prod_current"))
        self.Prod_voltage = QtGui.QLabel(self.groupBox_3)
        self.Prod_voltage.setGeometry(QtCore.QRect(10, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Prod_voltage.setFont(font)
        self.Prod_voltage.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Prod_voltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Prod_voltage.setObjectName(_fromUtf8("Prod_voltage"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(200, 140, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(200, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(200, 60, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(980, 120, 241, 181))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.Cons_power = QtGui.QLabel(self.groupBox_4)
        self.Cons_power.setGeometry(QtCore.QRect(20, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cons_power.setFont(font)
        self.Cons_power.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 0);"))
        self.Cons_power.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cons_power.setObjectName(_fromUtf8("Cons_power"))
        self.Cons_voltage = QtGui.QLabel(self.groupBox_4)
        self.Cons_voltage.setGeometry(QtCore.QRect(20, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cons_voltage.setFont(font)
        self.Cons_voltage.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Cons_voltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cons_voltage.setObjectName(_fromUtf8("Cons_voltage"))
        self.Cons_current = QtGui.QLabel(self.groupBox_4)
        self.Cons_current.setGeometry(QtCore.QRect(20, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cons_current.setFont(font)
        self.Cons_current.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Cons_current.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cons_current.setObjectName(_fromUtf8("Cons_current"))
        self.Consumption = QtGui.QLabel(self.groupBox_4)
        self.Consumption.setGeometry(QtCore.QRect(30, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Consumption.setFont(font)
        self.Consumption.setStyleSheet(_fromUtf8("border-color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 170, 0);"))
        self.Consumption.setAlignment(QtCore.Qt.AlignCenter)
        self.Consumption.setObjectName(_fromUtf8("Consumption"))
        self.label_24 = QtGui.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(200, 140, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(200, 60, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(200, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(520, 270, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.batt_discharg = QtGui.QLabel(Form)
        self.batt_discharg.setGeometry(QtCore.QRect(300, 390, 61, 21))
        self.batt_discharg.setObjectName(_fromUtf8("batt_discharg"))
        self.batt_overcharg = QtGui.QLabel(Form)
        self.batt_overcharg.setGeometry(QtCore.QRect(490, 450, 111, 31))
        self.batt_overcharg.setObjectName(_fromUtf8("batt_overcharg"))
        self.batt_undercharg = QtGui.QLabel(Form)
        self.batt_undercharg.setGeometry(QtCore.QRect(490, 480, 131, 31))
        self.batt_undercharg.setObjectName(_fromUtf8("batt_undercharg"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(490, 510, 181, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.state_ld_3.setText(_translate("Form", "EDF", None))
        self.state_ld_1.setText(_translate("Form", "EDF", None))
        self.state_ld_4.setText(_translate("Form", "EDF", None))
        self.state_ld_2.setText(_translate("Form", "EDF", None))
        self.state_ld_5.setText(_translate("Form", "EDF", None))
        self.batt_charg.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">&gt;&gt;&gt;&gt;</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">&gt;&gt;&gt;&gt;</span></p></body></html>", None))
        self.Title.setText(_translate("Form", "Smart Power Management System", None))
        self.Production_graphs.setText(_translate("Form", "Production graphs", None))
        self.Today_Button.setText(_translate("Form", "Today", None))
        self.week_Button.setText(_translate("Form", "This week", None))
        self.Month_Button.setText(_translate("Form", "This month", None))
        self.View_Button.setText(_translate("Form", "More about loads", None))
        self.Production.setText(_translate("Form", "Production", None))
        self.Prod_power.setText(_translate("Form", "0", None))
        self.Prod_current.setText(_translate("Form", "0", None))
        self.Prod_voltage.setText(_translate("Form", "24", None))
        self.label_23.setText(_translate("Form", "VA", None))
        self.label_22.setText(_translate("Form", "A", None))
        self.label_21.setText(_translate("Form", "V", None))
        self.Cons_power.setText(_translate("Form", "0", None))
        self.Cons_voltage.setText(_translate("Form", "0", None))
        self.Cons_current.setText(_translate("Form", "0", None))
        self.Consumption.setText(_translate("Form", "Consumption", None))
        self.label_24.setText(_translate("Form", "VA", None))
        self.label_25.setText(_translate("Form", "V", None))
        self.label_26.setText(_translate("Form", "A", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">&gt;&gt;&gt;&gt;</span></p></body></html>", None))
        self.batt_discharg.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">&lt;&lt;&lt;&lt;</span></p></body></html>", None))
        self.batt_overcharg.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Overcharge !</span></p></body></html>", None))
        self.batt_undercharg.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Undercharge !</span></p></body></html>", None))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Over Temperature !</span></p></body></html>", None))

import xz_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
