from tkinter import IntVar
from tkinter import *

def find():
    gent=""
    if var.get()==1:
        gent='male'
    if var.get()==2:
        gent='female'

    print(gent)

window = Tk()
var = IntVar()
gender = Radiobutton(window, text="male", variable=var, value=1, font=("arial", 15, "bold"))

gender.place(x=0,y=0)
gn= Radiobutton(window, text="female", variable=var, value=2, font=("arial", 15, "bold"))

gn.place(x=40,y=5)
Button(window,text="submit",command=find).place(x=100,y=100)

window.mainloop()