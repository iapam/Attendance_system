from tkinter import *
import signup

import view_attendace_history
from Report import reports
def a():
    import main

window = Tk()
window.title('Operations')
window.geometry('750x500+400+100')
window.configure(bg='#fff')
window.resizable(False, False)
frame=Frame(window,width=600,height=450,bg="#fff")
frame.place(x=20,y=20)
heading=Label(frame,text="Welcome Sir/Madam,\nplease select an operation to perform",
              font=("Microsoft Yahei UI Light",23,"bold"),fg="#57a1f8",bg="#fff")
heading.place(x=5,y=3)
Button(window,width=30,height=2,text="Register Student",fg="#fff",bg="green",font=("bold",15),command=signup.sign).place(x=170,y=130)
Button(window,width=30,height=2,text="Take Attendance",fg="#fff",bg="green",font=("bold",15),command=a).place(x=170,y=230)
Button(window, width=30, height=2, text="View Attendance", fg="#fff", bg="green", font=("bold",15), command=view_attendace_history.Vattendance).place(x=170, y=330)
Button(window,width=30,height=2,text="Generate Report",fg="#fff",bg="green",font=("bold",15),command=reports).place(x=170,y=430)

window.mainloop()
