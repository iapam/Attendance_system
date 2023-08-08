from tkinter import *
from tkinter import messagebox



def login():

    if userid.get()=="Apam" and password.get()=="ibm":
        window.destroy()
        import Operation


    else:
        messagebox.showerror("Invalid Login","Enter correct id or password")
window=Tk()
window.geometry('925x500+300+200')
window.resizable(False,False)
window.configure(bg="#fff")
window.title("Login")

img=PhotoImage(file='C:\\Users\I.B.M\Desktop\\login.png')
img1=PhotoImage(file="C:\\Users\I.B.M\Desktop\\user.png")
img2=PhotoImage(file="C:\\Users\I.B.M\Desktop\\lock.png")
Label(window,image=img,border=0,bg='#fff').place(x=50,y=90)
frame=Frame(window,width=280,height=400,bg="white")
frame.place(x=450,y=50)
heading=Label(frame,text="Login",fg="#57a1f8",bg="#fff",font=("Microsoft Yahei UI Light",24,"bold"))
heading.place(x=100,y=10)
#----------------------------------------------------------
def on_enter(e):
    userid.delete(0,'end')
def on_leave(e):
    if userid.get()=='':
        userid.insert(0,'Userid')
userid=Entry(frame,width=15,bg="#fff",fg="black",font=("Microsoft Yahei UI Light",15,"bold"),border=0)
userid.insert(0,"Userid")
userid.bind("<FocusIn>",on_enter)
userid.bind("<FocusOut>",on_leave)
userid.place(x=35,y=130)
Label(frame,image=img1,bg="#fff",border=0).place(x=0,y=130)
Frame(frame,bg="black",width=220,height=2).place(x=0,y=160)
#----------------------------------------------------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    if password.get()=='':
        password.insert(0,'password')
password=Entry(frame,width=15,bg="#fff",fg="black",font=("Microsoft Yahei UI Light",15,"bold"),show="*",border=0)
password.insert(0,"password")
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
password.place(x=35,y=220)
Label(frame,image=img2,bg="#fff",border=0).place(x=0,y=220)
Frame(frame,bg="black",width=220,height=2).place(x=0,y=250)

Button(frame,text="login",fg='#fff',font=("Microsoft Yahei UI Light",15,"bold"),bg='#57a1f8',width=10,height=1,command=login).place(x=15,y=280)
window.mainloop()
