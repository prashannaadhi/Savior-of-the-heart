# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preventive_measures.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_preventive(object):
    def __init__(self, Age,SBP,HDL,TCL,Gender,Smoke,TOH,Diabetes, Risk,str_risk):
        self.Age = Age
        self.SBP = SBP
        self.HDL = HDL
        self.TCL = TCL
        self.Gender = Gender
        self.Smoke = Smoke
        self.TOH = TOH
        self.Diabetes = Diabetes
        self.final_risk = Risk
        self.dfinal_risk = str_risk
        
        if self.final_risk < 5:
            self.preventive ="Safe"
            self.preventive5 = "1.Since final risk score is less than 5%:\n  You don’t have much risk of having ASCVD in future 10 years, if you \n  can maintain this life style if anyone in your family is suffering\n  from ASCVD  you must see some medical officials."
            
        elif self.final_risk < 10:
            self.preventive ="!!! Alert !!!" 
            self.preventive5 = "1.Since final risk score is between 5 and 10%:\n  You don't have much risk of having ASCVD in future 10 years, but \n  it is better to visit doctors if someone in your family is suffering\n  from ASCVD you must visit doctors as soon as possible."

        elif self.final_risk < 20:
            self.preventive = "!!! Caution !!!"
            self.preventive5 = "1.Since final risk score is between 10 and 20%:\n  You must change your lifestyle, exercising might help, You must visit \n  doctor as soon as possible, things might get more serious if someone\n  in your family is suffered from ASCVD."

        elif self.final_risk < 30:
            self.preventive ="!!! Warning !!!"
            self.preventive5 = "1.Since final risk score is between 20 and 30%:\n  You must change your lifestyle, exercising and medicating might help,\n  you must visit doctors immediately, things might get more serious if\n  someone in your family is suffered from ASCVD so you must start some\n  medication immediately."
        
        else:
            self.preventive ="!!! Danger !!!"
            self.preventive5 = "1.Since final risk score is more than 30%:\n  You are at very high risk of ASCVD, You must visit doctor immediately."        
            
        
        if self.Smoke == 1:
            self.preventive1 ="2.Stop smoking."
        
        
        if self.Diabetes == 1:
            self.preventive1 ="2.Try to eat/drink food having minimal amount of sugar, Check up your \n  sugar level periodically."
        
        else:
            self.preventive1 ="2.Do not eat/drink food having a lot of sugar content." 
        
        
        if self.HDL < 40:
            self.preventive2 ="3.Since HDL choleterol is less than 40mg/dl:\n  Increase your HDL cholesterol level maintaining between 60-100mg/dl by\n  Aerobic exercise for 30 -60 minutes per day, Do medication\n  and keeping healthy weight."
                           
        elif self.HDL < 60:
            self.preventive2 ="3.Since HDL choleterol is between 40 and 60mg/dl:\n  Increase your Hdl cholesterol level maintaining between 60-100mg/dl by\n  Aerobic exercise for 30-60 minutes per day, Do medication\n  and keeping healthy weight."
                           
        elif self.HDL < 100:
            self.preventive2 ="3.Since HDL choleterol is between 60 and 100mg/dl:\n  Try to maintain your HDL cholesterol level same as current."
                           
        elif self.HDL < 129:
            self.preventive2 ="3.Since HDL choleterol is between 100 and 129mg/dl:\n  Reduce you HDL cholesterol level below 100mg/dl by consuming olive oil\n  Eat fatty fish, Follow low-carb or ketogenic diet."
                           
        else:
            self.preventive2 ="3.Since HDL choleterol is more than 129mg/dl:\n  Consume olive oil, eat fatty fish, follow low-arb and ketogenic diet.\n  Your HDL level is at maximum risk."
                           
        
        if self.TCL < 120:
            self.preventive3 ="4.Since TCL is less than 120mg/dl:\n  Maintain your total cholesterol around 200mg/dl by reducing saturated \n  meat avoiding red meat, avoid eating store-bought cookies since\n  it contains vegetable oil, eating Omega-3 rich food like salmon, walnuts,\n  increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples."
                           
        elif self.TCL < 180:
            self.preventive3 ="4.Since TCL is between 120 and 180mg/dl:\n  Maintain your total cholesterol around 200mg/dl by reducing saturated \n  meat avoiding red meat, avoid eating store-bought cookies since\n  it contains vegetable oil, eating Omega-3 rich food like salmon, walnuts,\n  increasing soluble fiber eating oatmeal, kidney beans, sprouts,apples."
                           
        elif self.TCL < 200:
            self.preventive2 ="4.Since TCL is between 180 and 200mg/dl:\n  Try to maintain your Total cholesterol below 200mg/dl by having healthy \n  life style."  
        
        elif self.TCL < 240:
            self.preventive3 ="4.Since TCL is between 200 and 240mg/dl:\n  Try to maintain your total cholesterol below 200mg/dl by reducing \n  saturated meat avoiding red meat, avoid eating store-bought cookies since\n  it contains vegetable oil, eating Omega-3 rich food like salmon, walnuts,\n  increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples."
                           
        else:
            self.preventive3 ="4.Since TCL is more than 240mg/dl:\n  Try to maintain your total cholesterol below 200mg/dl by reducing \n  saturated meat avoiding red meat, avoid eating store-bought cookies since \n  it contains vegetable oil, eating Omega-3 rich food like salmon, walnuts,\n  increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples."
                           
        
        if self.SBP < 100:
            self.preventive4 ="5.Since Systolic BP is less than 100mmHg:\n  Try to maintain the Systolic blood pressure around 120mmHg by eating\n  healthy diet, diet rich in fruits, vegetables, whole grains and\n  low-fat dairy products and visit doctor frquently."
                           
        elif self.SBP < 120:
            self.preventive4 ="5.Since Systolic BP is between 100 and 120mmHg:\n  Try to maintain the Systolic blood pressure around 120mmHg by eating\n  healthy diet, diet rich in fruits, vegetables, whole grains and\n  low-fat dairy products."
                           
        elif self.SBP < 140 and self.TOH == 0:
            self.preventive4 ="5.Since SBP is between 120 and 140mmHg and Hypertension is treated:\n  Try to cut down on salt, exercise a lot, treat for Hypertension."
                           
        elif self.SBP < 140 and self.TOH == 1:
            self.preventive4 ="5.Since SBP is between 120 and 140mmHg and Hypertension is not treated:\n  Try to cut down on salt, exercise a lot, treat for Hypertension."
        
        else:
            self.preventive4 ="5.Since Systolic BP is more than 140mmHg:\n  Cut down on salt, exercise a lot, immediately visit doctor."
        
          
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 768)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/heart.jpg);")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(270, 300, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(270, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(140, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(490, 40, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(220, 460, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(460, 160, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(920, 190, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 380, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(150, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(720, 130, 470, 100))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(920, 310, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 170, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(330, 420, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        '''self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 520, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")'''
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(270, 90, 861, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(220, 380, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 420, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 340, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(920, 430, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 460, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(300, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(500, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(500, 250, 710, 431))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        
        '''self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 500, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")'''

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_19.setText(_translate("Dialog", str(self.HDL)))
        self.label_20.setText(_translate("Dialog", str(self.TCL)))
        self.label_16.setText(_translate("Dialog", str(self.Age)))
        self.label_5.setText(_translate("Dialog", "<font color='red'>SAVIOR OF THE HEART</font>"))
        self.label_23.setText(_translate("Dialog", str(self.Diabetes)))
        self.label_4.setText(_translate("Dialog", "Gender :"))
        
        self.label_10.setText(_translate("Dialog", "Smoking Status :"))
        self.label_17.setText(_translate("Dialog", str(self.Gender)))
        self.label_2.setText(_translate("Dialog", self.dfinal_risk +"   "+ self.preventive))
        
        self.label.setText(_translate("Dialog", "Your risk score is:"))
        self.label_22.setText(_translate("Dialog", str(self.TOH)))
        #self.pushButton_3.setText(_translate("Dialog", "Back to form"))
        self.label_6.setText(_translate("Dialog", "Machine Learning approach for determining the risk of having ASCVD in 10 years"))
        self.label_21.setText(_translate("Dialog", str(self.Smoke)))
        self.label_14.setText(_translate("Dialog", "Treatment of Hypertension :"))
        self.label_9.setText(_translate("Dialog", "TCL Cholesterol Level :"))
        self.label_7.setText(_translate("Dialog", "Systolic Blood Pressure :"))
        
        self.label_3.setText(_translate("Dialog", "Age :"))
        self.label_15.setText(_translate("Dialog", "Diabetes Status :"))
        self.label_18.setText(_translate("Dialog", "120"))
        self.label_8.setText(_translate("Dialog", "HDL Cholesterol Level :"))
        self.label_24.setText(_translate("Dialog", "<font color = 'blue'>Preventive Measures</font>")) 
        
        #for displaying preventive measures
        self.total_prevent= self.preventive5+"\n"+self.preventive1+"\n"+self.preventive2+"\n"+self.preventive3+"\n"+self.preventive4
        #print(self.total_prevent)
        self.label_25.setText(_translate("Dialog", self.total_prevent))
#import heart_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_preventive()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
