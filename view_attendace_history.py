from tkinter import *
from tkinter import messagebox
import psycopg2
def Vattendance():
    conn=psycopg2.connect(host="localhost",dbname="apam",port="5432",user="postgres",password="Zingaro1")
    window=Tk()
    window.geometry('1200x700+100+10')
    window.resizable(False,False)
    window.configure(bg="#fff")
    window.title("attendance")
    heading=Label(window,text="Students Attendance History",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",24,"bold"))
    heading.place(x=300,y=10)
    Label(window,text="Students ID",fg="black",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=10,y=300)
    userid=Entry(window,width=15,bg="#fff",fg="black",font=("Microsoft Yahei UI Light",15,"bold"),border=0.5)
    userid.place(y=300,x=150)

    Label(window,text="Name",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=370,y=70)
    Label(window,text="Year",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=510,y=70)
    Label(window,text="Major",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=600,y=70)
    Label(window,text="ID",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=750,y=70)
    Label(window,text="Date",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=910,y=70)
    Label(window,text="TA",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",17,"bold")).place(x=1100,y=70)

    def getDetails():
        cur = conn.cursor()
        idd=userid.get()
        print(idd)
        total = Frame(window, width=50, height=400, bg="white")
        total.place(x=1110, y=110)
        nameF = Frame(window, width=50, height=400, bg="white")
        nameF.place(x=360, y=110)
        dateF = Frame(window, width=150, height=400, bg="white")
        dateF.place(x=830, y=110)
        IdF = Frame(window, width=150, height=400, bg="white")
        IdF.place(x=710, y=110)
        MajorF = Frame(window, width=150, height=400, bg="white")
        MajorF.place(x=580, y=110)
        YearF = Frame(window, width=50, height=400, bg="white")
        YearF.place(x=530, y=110)

        cur.execute("""SELECT * FROM students where id="""+ "\'" + idd + "\'")
        r = cur.fetchall()
        for i in r:
            Label(total, text=i[3], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            Label(nameF, text=i[0], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            Label(dateF, text=i[4], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            Label(IdF, text=i[5], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            Label(MajorF, text=i[2], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            Label(YearF, text=i[1], font=("Microsoft Yahei UI Light", 17, "bold"),bg="white").grid(pady=5)
            conn.commit()
            cur.close()
            conn.close()



    Button(window,command=getDetails,text="Generate ID",fg="#fff",bg="#57a1f8",width=15,height=2,font=('Microsoft Yahei UI Light',8,'bold')).place(x=150,y=350)


    window.mainloop()



