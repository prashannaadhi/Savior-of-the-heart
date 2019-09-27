# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from risk_score import Ui_Risk_window



class Ui_MainWindow(object):
    def open_risk_window(self):
        self.window = QtWidgets.QDialog()
        self.Age = int(self.age.toPlainText())
        self.Sbp = int(self.SBP.toPlainText())
        self.Hdl = int(self.HDL.toPlainText())
        self.Tcl = int(self.TCL.toPlainText())
        if self.GMale.isChecked():
            self.Gender = 0
            self.dGender = "Male"
        else:
            self.Gender = 1
            self.dGender = "Female"

        if self.SYes.isChecked():
            self.Smoke = 1
            self.dSmoke = "Yes" 
        else:
            self.Smoke = 0
            self.dSmoke = "No"

        if self.HYes.isChecked():
            self.Toh = 1
            self.dToh = "Yes"
        else:
            self.Toh = 0
            self.dToh = "No"
        if self.DYes.isChecked():
            self.Diabetes = 1
            self.dDiabetes = "Yes"
        else:
            self.Diabetes = 0
            self.dDiabetes = "No"
    
        self.ui = Ui_Risk_window(self.Age, self.Sbp, self.Hdl, self.Tcl, self.Gender, self.Smoke, self.Toh,
                                 self.Diabetes,self.dGender, self.dSmoke, self.dToh,self.dDiabetes)
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/heart.jpg);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SBP = QtWidgets.QTextEdit(self.centralwidget)
        self.SBP.setGeometry(QtCore.QRect(380, 250, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SBP.setFont(font)
        self.SBP.setObjectName("SBP")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 160, 41, 321))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 90, 861, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.SYes = QtWidgets.QRadioButton(self.centralwidget)
        self.SYes.setGeometry(QtCore.QRect(620, 270, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.SYes.setFont(font)
        self.SYes.setCheckable(True)
        self.SYes.setObjectName("SYes")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.SYes)
        self.Age = QtWidgets.QLabel(self.centralwidget)
        self.Age.setGeometry(QtCore.QRect(40, 150, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.Age.setFont(font)
        self.Age.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Age.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Age.setObjectName("Age")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.GMale = QtWidgets.QRadioButton(self.centralwidget)
        self.GMale.setGeometry(QtCore.QRect(620, 180, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.GMale.setFont(font)
        self.GMale.setCheckable(True)
        self.GMale.setObjectName("GMale")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.GMale)
        self.SNo = QtWidgets.QRadioButton(self.centralwidget)
        self.SNo.setGeometry(QtCore.QRect(750, 270, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.SNo.setFont(font)
        self.SNo.setCheckable(True)
        self.SNo.setObjectName("SNo")
        self.buttonGroup_2.addButton(self.SNo)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(920, 270, 401, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.TCL = QtWidgets.QTextEdit(self.centralwidget)
        self.TCL.setGeometry(QtCore.QRect(380, 430, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TCL.setFont(font)
        self.TCL.setObjectName("TCL")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 40, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.NYes = QtWidgets.QRadioButton(self.centralwidget)
        self.NYes.setGeometry(QtCore.QRect(750, 360, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.NYes.setFont(font)
        self.NYes.setCheckable(True)
        self.NYes.setObjectName("NYes")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.NYes)
        self.tcl = QtWidgets.QLabel(self.centralwidget)
        self.tcl.setGeometry(QtCore.QRect(50, 420, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.tcl.setFont(font)
        self.tcl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tcl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tcl.setObjectName("tcl")
        self.DNo = QtWidgets.QRadioButton(self.centralwidget)
        self.DNo.setGeometry(QtCore.QRect(750, 450, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.DNo.setFont(font)
        self.DNo.setCheckable(True)
        self.DNo.setObjectName("DNo")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.DNo)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 420, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.DYes = QtWidgets.QRadioButton(self.centralwidget)
        self.DYes.setGeometry(QtCore.QRect(620, 450, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.DYes.setFont(font)
        self.DYes.setCheckable(True)
        self.DYes.setObjectName("DYes")
        self.buttonGroup_4.addButton(self.DYes)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(890, 160, 20, 321))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(920, 380, 401, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(920, 170, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(600, 520, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.calculate.setFont(font)
        self.calculate.setObjectName("calculate")
        #to show risk window when clicked
        self.calculate.clicked.connect(self.open_risk_window)
        
        self.age = QtWidgets.QTextEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(380, 160, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.age.setFont(font)
        self.age.setPlaceholderText("")
        self.age.setObjectName("age")
        self.sbp = QtWidgets.QLabel(self.centralwidget)
        self.sbp.setGeometry(QtCore.QRect(40, 240, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.sbp.setFont(font)
        self.sbp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sbp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sbp.setObjectName("sbp")
        self.hdl = QtWidgets.QLabel(self.centralwidget)
        self.hdl.setGeometry(QtCore.QRect(40, 330, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.hdl.setFont(font)
        self.hdl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.hdl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hdl.setObjectName("hdl")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 330, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.HYes = QtWidgets.QRadioButton(self.centralwidget)
        self.HYes.setGeometry(QtCore.QRect(620, 360, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.HYes.setFont(font)
        self.HYes.setCheckable(True)
        self.HYes.setObjectName("HYes")
        self.buttonGroup_3.addButton(self.HYes)
        self.FMale = QtWidgets.QRadioButton(self.centralwidget)
        self.FMale.setGeometry(QtCore.QRect(750, 180, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.FMale.setFont(font)
        self.FMale.setCheckable(True)
        self.FMale.setObjectName("FMale")
        self.buttonGroup.addButton(self.FMale)
        self.HDL = QtWidgets.QTextEdit(self.centralwidget)
        self.HDL.setGeometry(QtCore.QRect(380, 340, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HDL.setFont(font)
        self.HDL.setObjectName("HDL")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(920, 290, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(620, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(920, 390, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SBP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Machine Learning approach for determining the risk of having ASCVD in 10 years"))
        self.SYes.setText(_translate("MainWindow", "Yes"))
        self.Age.setText(_translate("MainWindow", "What is your age?\n"
"(Applicable for age range: 30-74)"))
        self.pushButton_3.setText(_translate("MainWindow", "Cancel"))
        self.GMale.setText(_translate("MainWindow", "Male"))
        self.SNo.setText(_translate("MainWindow", "No"))
        self.label_8.setText(_translate("MainWindow", "Do you smoke?"))
        self.TCL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<font color='red'>SAVIOR OF THE HEART</font>"))
        self.NYes.setText(_translate("MainWindow", "No"))
        self.tcl.setText(_translate("MainWindow", "TCL Cholesterol Level\n"
"(in mg/dl, Normal range: < 200)"))
        self.DNo.setText(_translate("MainWindow", "No"))
        self.label_10.setText(_translate("MainWindow", "Do you have Diabetes?"))
        self.DYes.setText(_translate("MainWindow", "Yes"))
        self.label_11.setText(_translate("MainWindow", "This calculator is based on Framingham Heart Study\n"
" Find out more on:\n"
"https://www.framinghamheartstudy.org/"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.age.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.sbp.setText(_translate("MainWindow", "Systolic Blood Pressure (SBP)\n"
"(in mmHg, Normal range: < 140)"))
        self.hdl.setText(_translate("MainWindow", "HDL Cholesterol Level\n"
"(in mg/dl, Normal range: > 40)"))
        self.label_9.setText(_translate("MainWindow", "Treatment of Hypertension?"))
        self.HYes.setText(_translate("MainWindow", "Yes"))
        self.FMale.setText(_translate("MainWindow", "Female"))
        self.HDL.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Validation of Framingham Heart Study for\n"
" Asian Population\n"
"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2465638/"))
        self.label_7.setText(_translate("MainWindow", "Gender"))
        self.label_12.setText(_translate("MainWindow", "Know how individual parameter affects the risk score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
