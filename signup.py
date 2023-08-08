import datetime
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
import random

import cv2
import firebase_admin
from firebase_admin import credentials, db
import EncodeGenerator

def sign():

    def inserid():
        id = str(random.randint(222222, 333333))
        studentid_E.insert(0,id)
    def register():
        mymajor= classs.get()
        yourname = name.get()
        current_date_time = datetime.datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Current Date and Time:", formatted_date_time)
        gende = clas.get()

        Youryear = year.get()
        yourid = studentid_E.get()
        print("hello",gende)
        EncodeGenerator.encods()
        ref = db.reference("Student")
        data = {
            "" + yourid + "":
                {
                    "name": yourname,
                    "program": mymajor,
                    "gender": gende,
                    "Total_Attendance": 0,
                    "Standing": "G",
                    "Year": Youryear,
                    "last_attendance_time": formatted_date_time
                }

        }

        for key, value in data.items():
            ref.child(key).set(value)


    window=Tk()
    window.title('Signup')
    window.geometry('925x500+200+100')
    window.configure(bg='#fff')
    window.resizable(False,False)
    studentid_L=Label(window, text="Student id",font=('Microsoft Yahei UI Light',15,'bold'),bg="#fff")
    studentid_L.place(x=200,y=140)
    studentid_E = Entry(window, width=25,background="#fff",fg='black', border=0.7, bg='#fff', font=('Microsoft Yahei UI Light', 12))
    studentid_E.place(x=200,y=180)
    Button(window,text="Generate ID",fg="#fff",bg="#57a1f8",width=15,height=2,command=inserid,font=('Microsoft Yahei UI Light',8,'bold')).place(x=200,y=220)
    Label(window,text="NOTE! Make sure to rename your ",fg="red" ,bg="#fff").place(x=200,y=270)
    Label(window, text="216x216 image with this ID.png and save it in this ",fg="red" ,bg="#fff").place(x=200, y=290)
    Label(window, text="path(C:/Users/I.B.M/PycharmProjects/Attendance/images",fg="red" ,bg="#fff").place(x=170, y=310)
    Label(window, text="before submitting the registration ",fg="red" ,bg="#fff").place(x=200, y=330)
    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    heading=Label(window,text='Registration Portal',fg="#57a1f8",bg='#fff',font=('Microsoft Yahei UI Light',20,'bold'))
    heading.place(x=300,y=5)
    def on_enter(e):
        name.delete(0,'end')
    def on_leave(e):
        if name.get()=='':
            name.insert(0,'Name')

    name=Entry(frame,width=25,fg='black',border=0,bg='#fff',font=('Microsoft Yahei UI Light',11))
    name.place(x=30,y=80)
    name.insert(0,'Name')
    name.bind("<FocusIn>",on_enter)
    name.bind("<FocusOut>",on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    #---------------------------------------------------------------------------------------------
    def on_enter(e):
        classs.delete(0,'end')
    def on_leave(e):
        if classs.get()=='':
            classs.insert(0,'program/class')

    def class_box(choice):
        yclass = Entry(frame, width=8, background="#fff", fg='black', border=0.7, bg='#fff', font=('Bold', 17))
        yclass.place(x=210, y=155)
        yclass.insert(0, classs.get())

    label1 = Label(frame, text="Select class :", font=("arial", 15, "italic bold"))
    label1.place(x=15, y=155)
    class_options = ['cs1', 'cs2', 'cs3', 'cs4']
    classs = StringVar()
    classs.set(class_options[0])
    drop = OptionMenu(frame, classs, *class_options,command=class_box)
    drop.pack(expand=True)
    drop.configure(fg="white", font=("arial", 15, "italic bold"))
    drop["menu"].config(bg="white")
    drop.place(x=160, y=150)


    #---------------------------------------------------------------------------------------------
    def sex_box(choice):
        ysex=Entry(frame,width=15,background="#fff",fg='black', border=0.7, bg='#fff', font=('Bold', 17))
        ysex.place(x=120,y=225)
        ysex.insert(0,clas.get())
    label1 = Label(frame, text="Sex :", font=("arial", 15, "italic bold"))
    label1.place(x=15, y=225)
    class_option = ['male', 'female']
    clas = StringVar()
    clas.set(class_options[0])
    drop1 = OptionMenu(frame, clas, *class_option,command=sex_box)
    drop1.pack(expand=True)
    drop1.configure( fg="white", font=("arial", 15, "italic bold"))
    drop1["menu"].config(bg="white")
    drop1.place(x=70, y=220)

    # var=StringVar()
    #
    # gender = Radiobutton(frame, text="male", variable=var, value="male", font=("arial", 15, "bold"),command=sex)
    # va=StringVar()
    # va.set('female')
    # gender.place(x=30, y=220)
    # gen = Radiobutton(frame, text="female", variable=var, value="female", font=("arial", 15, "bold"),command=sex)
    #
    # gen.place(x=130, y=220)

    #----------------------------------------------------
    def on_enter(e):
        year.delete(0,'end')
    def on_leave(e):
        if year.get() == '':
            year.insert(0,'Year')

    year = Entry(frame, width=25, fg='black', border=0, bg='#fff', font=('Microsoft Yahei UI Light', 11))
    year.place(x=30, y=280)
    year.insert(0,'Year')
    year.bind("<FocusIn>", on_enter)
    year.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=307)
    # ----------------------------------------------------
    Button(frame,width=39,pady=7,text="Register",bg='#57a1f8',fg="#fff",border=0,command=register).place(x=35,y=340)

    window.mainloop()


