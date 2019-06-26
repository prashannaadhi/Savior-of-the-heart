from tkinter import *
import math
from random_forest import random_forest
from svr import SVR
import numpy as n


class Frames(object):
    
    def __init__(self):
        pass

    def main_frame(self, root):
        root.geometry('1360x768')
        root.title("SAVIOR OF THE HEART")

        self.age = StringVar()  # age
        self.sbp = StringVar()  # SBP
        self.hdl = StringVar()  # HDL
        self.tcl = StringVar()  # TCL
        self.hypertension = StringVar()  # hypertension
        self.hypertension.set(None)
        self.smoke = StringVar()  # smoking
        self.smoke.set(None)
        self.gender = StringVar()  # gender
        self.gender.set(None)
        self.diabetes = StringVar()  # diabetes
        self.diabetes.set(None)

        label_0 = Label(root, text="Savior of The Heart", width=38, font=("Calibri", 43), foreground='#8e160f')
        label_0.place(x=120, y=20)
        label_11 = Label(root, text="Machine learning approach for determining the risk of having ASCVD within 10 years ",
                         width=70, foreground='black', font=("Arial", 20))
        label_11.place(x=120, y=100)

        label_2 = Label(root, text="What is your Age? \n (applicable only for age range: 30-74)", width=30,
                        font=("bold", 12))
        label_2.place(x=405, y=150)

        entry_2 = Entry(root, textvariable=self.age, width=30)
        entry_2.place(x=695, y=160)

        label_3 = Label(root, text="Systolic Blood Pressure (SBP)\n in mmHg (normal range: 100-140)", width=30,
                        font=("bold", 12))
        label_3.place(x=405, y=210)

        entry_3 = Entry(root, textvariable=self.sbp, width=30)
        entry_3.place(x=695, y=220)

        label_4 = Label(root, text="HDL cholesterol level in mg/dl \n (normal range: 35-60)", width=30,
                        font=("bold", 12))
        label_4.place(x=405, y=270)

        entry_4 = Entry(root, textvariable=self.hdl, width=30)
        entry_4.place(x=695, y=280)

        label_5 = Label(root, text="TCL cholesterol level in mg/dl \n (normal range: 200-240)", width=30,
                        font=("bold", 12))
        label_5.place(x=405, y=330)
        entry_5 = Entry(root, textvariable=self.tcl, width=30)
        entry_5.place(x=695, y=340)

        label_6 = Label(root, text="Treatment for Hypertension", width=30, font=("bold", 12))
        label_6.place(x=380, y=390)

        Radiobutton(root, text="Yes", padx=5, value="1", variable=self.hypertension).place(x=735, y=390)
        Radiobutton(root, text="No", padx=20, value="0", variable=self.hypertension).place(x=790, y=390)

        label_7 = Label(root, text="Do you smoke?", width=30, font=("bold", 12))
        label_7.place(x=405, y=430)

        Radiobutton(root, text="Yes", padx=5, value="1", variable=self.smoke).place(x=735, y=430)
        Radiobutton(root, text="No", padx=20, value="0", variable=self.smoke).place(x=790, y=430)

        label_8 = Label(root, text="Gender", width=30, font=("bold", 12))
        label_8.place(x=405, y=470)
        Radiobutton(root, text="Male", padx=5, value="1", variable=self.gender).place(x=735, y=470)
        Radiobutton(root, text="Female", padx=20, value="0", variable=self.gender).place(x=790, y=470)

        label_9 = Label(root, text="Do you have Diabetes?", width=30, font=("bold", 12))
        label_9.place(x=405, y=510)
        Radiobutton(root, text="Yes", padx=5, value="1", variable=self.diabetes).place(x=735, y=510)
        Radiobutton(root, text="No", padx=20, value="0", variable=self.diabetes).place(x=790, y=510)

        label_10 = Label(root,
                         text="10 year risk prediction of having ASCVD is calculated using Random Forest Regression Algorithm \n using the data generated from 'Framingham Heart Study'",
                         width=150, font=("Arial", 10))
        label_10.place(x=10, y=610)

        Button(root, text='Submit', width=30, bg='brown', fg='white', command=self.result_frame1).place(x=550, y=550)

    def result_frame1(self, ):
        result = Toplevel()
        result.title('RESULT')
        result.geometry('1360x768')

        #  label = Label(result, text="Confirmation Page ", width=30, font=("bold", 20))

        smoke = int(self.smoke.get())
        age = int(self.age.get())
        HDL = int(self.hdl.get())
        TCL = int(self.tcl.get())
        SBP = int(self.sbp.get())
        TOH = int(self.hypertension.get())
        gender = int(self.gender.get())
        diabetes = int(self.diabetes.get())

        if gender == "1":
            gender1 = "Male"
        else:
            gender1 = "Female"

        if smoke == "1":
            smoke1 = "Yes"
        else:
            smoke1 = "No"

        if TOH == "1":
            TOH1 = "Yes"
        else:
            TOH1 = "No"

        if diabetes == "1":
            diabetes1 = "Yes"
        else:
            diabetes1 = "No"

        Label(result, text="Result", width=38, font=("Calibri", 43), foreground='#8e160f').pack()
        #Label(result, text="Machine learning approach for determining the risk of having ASCVD in 10 years ", width=64,
              #foreground='black', font=("Arial", 20), padx = 20).pack()
        Label(result, text='                Gender             :     ' + str(gender1), font=("Book Antiqua", 12),
              background='#dee098', padx = 10 ).pack()
        Label(result, text='                      Age             :          ' + str(age), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text='Systolic Blood Pressure (SBP) :' + str(SBP), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text='   HDL Cholesterol level    :      ' + str(HDL), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text='Total Cholesterol Level(TCL):' + str(TCL), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text=' Treatment of Hypertension  :' + str(TOH1), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text='    Smoking Status     :        ' + str(smoke1), font=("Book Antiqua", 12),
              background='#dee098').pack()
        Label(result, text='                Diabetes         :           ' + str(diabetes1), font=("Book Antiqua", 12),
              background='#dee098').pack()

        if 30 <= age < 75:  
            if TCL < HDL:   
                Label(result, text="!!! HDL cholesterol level can't be greater than Total Cholesterol level !!!",
                      font=("Arial", 16), background='yellow').pack()
            
            elif TCL == HDL:
                Label(result, text="!!! HDL cholesterol level can't be equal to Total Cholesterol level !!!",
                      font=("Arial", 16), background='yellow').pack()
            else:
                valueRand = random_forest(gender, age, SBP, TOH, smoke, diabetes, HDL, TCL)
                #valueSVR = SVR(gender, age, SBP, TOH, smoke, diabetes, HDL, TCL)

                valueRand = n.squeeze(valueRand)
                #valueSVR = n.squeeze(valueSVR)

                print(valueRand)
                #print(valueSVR)

            #if valueRand < float(valueSVR):
                #value = valueSVR
                #print("SVR prediction value is selected")
            #else:
                value = round(float(valueRand),2)
                
                print("Forest tree regression prediction value is selected")

                print(value)
                
                Label(result, text='Risk Score \n' + str(value) + '%', font=("Arial", 25), foreground='Green', padx = 60).pack()
                # value = n.squeeze(value)

                if value < 5:
                    Label(result, text="Safe", font=("MS Serif", 35), foreground='green').pack()
                    Label(result,
                          text="You don’t have much risk of heart disease in future 10 years if you can maintain this "
                               "life style \n if anyone in your family is suffering from ASCVD  you must see some "
                               "medical officials",
                          font=("Verdana", 14), foreground='black').pack()
                elif value < 10:
                    Label(result, text="!!! Alert !!!", font=("MS Serif", 35), foreground='blue').pack()
                    Label(result,
                          text="You have not so much of risk of having ASCVD in future 10 years, but it is better to "
                               "visit the doctor \n if someone in your family is suffering from ASCVD you must visit "
                               "doctor as soon as possible",
                          font=("Verdana", 14), foreground='black').pack()
                elif value < 20:
                    Label(result, text="!!! Caution !!!", font=("MS Serif", 35), foreground='yellow').pack()
                    Label(result,
                          text="You must change your lifestyle, exercising will definitely help, You must visit "
                               "doctor as soon as possible,\n things might get more serious if someone in your family "
                               "has suffered from ASCVD",
                          font=("Verdana", 14), width=100, foreground='black').pack()
                elif value < 30:
                    Label(result, text="!!! Warning !!!", font=("MS Serif", 35), foreground='orange').pack()
                    Label(result,
                          text="You must change your lifestyle, exercising and meditating will help, You must visit doctors immediately,\n Things might get more serious if someone in your family has suffered from ASCVD. You must start some medication immediately",
                          font=("Verdana", 14), foregroun='black').pack()
                else:
                    Label(result, text="!!! Danger !!!", font=("MS Serif", 35), foreground='red').pack()
                    Label(result, text="You are at very high risk of ASCVD, You must visit the doctor immediately",
                          font=("Verdana", 14), foreground='black').pack()
                    
                Button(result, text='Preventive Measures', width=30, font=("Arial",14),bg='blue', fg='white', command=self.result_frame2, padx = 10).pack()

        else:
            Label(result, text="!!! Predictor doesn't work for the age below 30 or above 75 !!!", font=("Arial", 16),
                  background='yellow').pack()

        # dataentry()
        
    def result_frame2(self):
        result = Toplevel()
        result.title('Prevention')
        result.geometry('1200x300')
        
        smoke = int(self.smoke.get())
        age = int(self.age.get())
        HDL = int(self.hdl.get())
        TCL = int(self.tcl.get())
        SBP = int(self.sbp.get())
        TOH = int(self.hypertension.get())
        gender = int(self.gender.get())
        diabetes = int(self.diabetes.get())
        
        Label(result, text="Preventive Measures", width=38, font=("Calibri", 43), foreground='#8e160f').pack()
        
        if smoke == "1":
                    Label(result, text="-> Stop smoking", font=("Times", 12)).pack()

        if diabetes == "1":
            Label(result,
                  text="-> Try to eat/drink food having minimal amount of sugar, Check up your sugar level periodically",
                  font=("Calibri", 14),padx = 15).pack()
        else:
            Label(result, text="-> Do not eat/drink food having a lot of sugar content",
                  font=("Calibri", 14),padx = 15).pack()

        if HDL < 40:
            Label(result,
                  text="-> Increase your HDL cholesterol level maintaining between 60-100mg/dl by Aerobic exercise for 30 -60 minutes per day,\n Do not smoke, Do medication and keep yourself in proper shape and visit your doctor",
                  font=("Calibri", 14),padx = 15).pack()
        elif HDL < 60:
            Label(result,
                  text="-> Increase your HDL cholesterol level maintaining between 60-100 mg/dl by Aerobic exercise for 30-60 minutes per day,\n Do not smoke, Do medication and keep yourself in proper shape. Visit doctor frequently",
                  font=("Calibri", 14),padx = 15).pack()
        elif HDL < 100:
            Label(result, text="->Try to maintain your HDL cholesterol level between 60- 100mg/dl",
                  font=("Calibri", 14),padx = 15).pack()
        elif HDL < 129:
            Label(result,
                  text="-> Reduce you HDL cholesterol level below 100mg/dl by consuming olive oil,\n Eat fatty fish, Follow low-carb or ketogenic diet",
                  font=("Calibri", 14),padx = 15).pack()
        else:
            Label(result,
                  text="-> Consume olive oil, eat fatty fish, follow low-arb and ketogenic diet,\n visit doctor immediately. Your HDL level is at maximum risk.",
                  font=("Calibri", 14),padx = 15).pack()

        if TCL < 120:
            Label(result,
                  text="-> Maintain your total cholesterol around 200mg/dl by reducing saturated meat avoiding red meat,\n avoid eating store-bought cookies since it contains vegetable oil,\n eating Omega-3 rich food like salmon, walnuts, increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples and\n immediately visit the doctor",
                  font=("Calibri", 14),padx = 15).pack()
        elif TCL < 180:
            Label(result,
                  text="-> Maintain your total cholesterol level around 200mg/dl by reducing saturated meat avoiding red meat,\n avoid eating store-bought cookies since it contains vegetable oil,\n eating Omega-3 rich food like salmon, walnuts, increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples and\n frequently visit doctor",
                  font=("Calibri", 14),padx = 15).pack()
        elif TCL < 200:
            Label(result,
                  text="-> Try to maintain your Total cholesterol level below 200mg/dl by having healthy life style",
                  font=("Calibri", 14),padx = 15).pack()
        elif TCL < 240:
            Label(result,
                  text="->Try to maintain your total cholesterol level below 200mg/dl by reducing saturated meat avoiding red meat,\n avoid eating store-bought cookies since it contains vegetable oil,\n eating Omega-3 rich food like salmon, walnuts, increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples",
                  font=("Calibri", 14),padx = 15).pack()
        else:
            Label(result,
                  text="->Try to maintain your total cholesterol level below 200mg/dl by reducing saturated meat avoiding red meat,\n avoid eating store-bought cookies since it contains vegetable oil,\n eating Omega-3 rich food like salmon, walnuts, increasing soluble fiber eating oatmeal, kidney beans, sprouts, apples and immediately visit doctor",
                  font=("Calibri", 14),padx = 15).pack()

        if SBP < 100:
            Label(result,
                  text="-> Try to maintain the Systolic blood pressure around 120mmHg by eating healthy diet,\n diet rich in fruits, vegetables, whole grains and low-fat dairy products and\n visit doctor frquently",
                  font=("Calibri", 14),padx = 15).pack()
        elif SBP < 120:
            Label(result,
                  text="-> Try to maintain the Systolic blood pressure around 120mmHg by eating healthy diet,\n diet rich in fruits, vegetables, whole grains and low-fat dairy products",
                  font=("Calibri", 14),padx = 15).pack()
        elif SBP < 140 and SBP == "0":
            Label(result, text="-> Try to cut down on salt, exercise a lot, treat for possible Hypertension",
                  font=("Calibri", 14),padx = 15).pack()
        elif SBP < 140 and SBP == "1":
            Label(result, text="-> Try to cut down on salt, exercise a lot, treat for Hypertension",font = ("Calibri", 15),padx = 10).pack()
        else:
            Label(result,
                  text="-> Cut down on salt, exercise a lot, immediately visit doctor before it gets too serious",
                  font=("Calibri", 15),padx = 10).pack()

root = Tk()
app = Frames()
app.main_frame(root)
root.mainloop()
