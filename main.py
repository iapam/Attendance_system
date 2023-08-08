
import os
import pickle

import cv2
import face_recognition
import numpy as np
import cvzone
import firebase_admin
import psycopg2
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import datetime as time
from datetime import datetime
from tkinter import *
from tkinter import messagebox

def Adetails():
    dat=date.get()
    ecla = classs.get()
    cou = course.get()

    return dat,ecla,cou

from tkinter import *
current_date_time = time.datetime.now()
formatted_date_time = current_date_time.strftime("%d/%m/%Y")
window = Tk()
window.geometry("640x400")
window.title("Attendance")


def class_box(choice):
    yclass = Entry(window, width=8, background="#fff", fg='black', border=0.7, bg='#fff', font=('Bold', 17))
    yclass.place(x=300, y=35)
    yclass.insert(0, classs.get())


label1 = Label(window, text="Select class:", font=('calibri', 20, 'bold'))
label1.place(x=100, y=35)

class_options = ['cs1', 'cs2', 'cs3', 'cs4']

classs = StringVar()
classs.set(class_options[0])
drop = OptionMenu(window, classs, *class_options,command=class_box)
drop.configure(bg="black", fg="white", font=('calibri', 18, 'bold'))
drop.pack(expand=True)
drop["menu"].config(bg="white")
drop.place(x=250, y=30)

def course_box(choice):
    ycourse = Entry(window, width=8, background="#fff", fg='black', border=0.7, bg='#fff', font=('Bold', 17))
    ycourse.place(x=325, y=105)
    ycourse.insert(0, course.get())


label2 = Label(window, text="Select Course:", font=('calibri', 20, 'bold'))
label2.place(x=100, y=105)

course_options = ['csm20', 'csm10', 'cs13', 'cs41']

course = StringVar()
course.set(course_options[0])
drop1 = OptionMenu(window, course, *course_options,command=course_box)
drop1.configure(bg="black", fg="white", font=('calibri', 18, 'bold'))
drop1.pack(expand=True)
drop1["menu"].config(bg="white")
drop1.place(x=280, y=100)

label3 = Label(window, text="Date:", font=('calibri', 20, 'bold'))
label3.place(x=100, y=180)

text2 = StringVar()
date = Entry(window, textvariable=text2, font=('calibri', 15), bd=3, width=10)
date.insert(0, formatted_date_time)
date.place(x=200, y=180)

def reset():
    conn = psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres",
                            password="Zingaro1")
    cur = conn.cursor()
    dat = date.get()
    ecla = classs.get()
    cou = course.get()
    cur.execute( """DELETE FROM students where date=""" + "\'" + formatted_date_time + "\'" + """ and class=""""\'" + ecla + "\'" + """ and course=""""\'" + cou + "\'")
    conn.commit()
    cur.close()
    conn.close()
    num()
def num():
    imgstudent = []

    dat,ecla,cou=Adetails()
    print(dat,ecla,cou)
    window.destroy()
    conn = psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres",
                            password="Zingaro1")
    cur = conn.cursor()
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://database-72071-default-rtdb.firebaseio.com/",
        "storageBucket": "database-72071.appspot.com"
    })

    load_details=[]
    formatted_date_time = current_date_time.strftime("%d/%m/%Y")
    month = current_date_time.strftime("%m/%Y")
    status = 'absent'
    status = "\'" + status + "\'"
    month = "\'" + month + "\'"
    cour = "\'" + cou + "\'"
    dbids=1


    cur.execute("""SELECT * FROM students where date=""" + "\'" + formatted_date_time + "\'"+""" and class=""""\'" + ecla + "\'"+""" and course=""""\'" +cou+"\'")
    r = cur.fetchall()

    if len(r) !=0:
        messagebox.showerror("error","already taking attendance for totay")
    else:
        studentinfoa = db.reference('Student').get()
        for key,value in studentinfoa.items():
            man = db.reference(f'Student/{key}').get()
            dbname = "\'" + str(man['name']) + "\'"
            dbmajor = "\'" + str(man['program']) + "\'"
            dbyear = "\'" + str(man['Year']) + "\'"
            gender = "\'" + str(man['gender']) + "\'"
            dbdate = "\'" + formatted_date_time+ "\'"
            dbid = "\'" + key + "\'"
            print(dbid,dbname,dbmajor,dbyear,gender,dbdate,month,status,dbids)
            dbids+=1
            if dbmajor=="'"+ecla+"'":
                cur.execute("""INSERT INTO Students(name,Year,class,gender,date,id,month,status,course) VALUES(""" + dbname + ",""" + dbyear + ",""" + dbmajor + ",""" + gender + ",""" + dbdate + ",""" + dbid + ",""" + month + ",""" + status + ",""" + cour+ ")""")
                conn.commit()
                cur.close()
                conn.close()
                conn=psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres",
                                password="Zingaro1")
                cur=conn.cursor()



        bucket=storage.bucket()
        # opening the webcam
        cap=cv2.VideoCapture(0)
        # importing our mode images into a list
        imgbackground=cv2.imread('Resources/background.png')
        # setting webcam width and height
        cap.set(3,640)
        cap.set(4,480)
        folderModepath='Resources/Modes'
        pathModeList=os.listdir(folderModepath)
        imgModelist=[]
        # importin mode images into a list
        for path in pathModeList:
            # reading all the attendance mode
            imgModelist.append(cv2.imread(os.path.join(folderModepath,path)))
        # load the encoding file
        print("Loading encoded file")
        file=open("EncodeFile.p",'rb')
        encodeListKnownIds=pickle.load(file)
        file.close()
        # getting the image encodings and it id's
        EncodeKnownlist,studentid=encodeListKnownIds
        print(studentid)
        print(" encoded file loaded")
        modeType=0
        counter=0
        id=-1


        while True:

            success,img=cap.read()
            # getting the face from the image
            imgS=cv2.resize(img,(0,0),None,0.25,0.25)
            imgS=cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            # finding the location of the face
            faceCurFrame=face_recognition.face_locations(imgS)
            # encodind the face in the frame
            EncodingCurFrame=face_recognition.face_encodings(imgS,faceCurFrame)
            # specifying the starting point of the width and ending point of the height and putting it in the background graphic
            imgbackground[162:162 + 480, 55:55 + 640] = img
            imgbackground[44:44 + 633, 808:808 + 414] = imgModelist[modeType]
          # cv2.imshow("WebCam",img)
            if faceCurFrame:
                # comparing the face in the frame with the encoded face
                for encodeface, faceloc in zip(EncodingCurFrame, faceCurFrame):
                    # finding the matches
                    matches = face_recognition.compare_faces(EncodeKnownlist, encodeface)
                    # finding how near image matches
                    faceDis = face_recognition.face_distance(EncodeKnownlist, encodeface)
                    print("dis", faceDis)
                    matcheIndex = np.argmin(faceDis)

                    print(matcheIndex)
                    if matches[matcheIndex]:
                        # print("face Detected")
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                        cvzone.cornerRect(imgbackground, bbox, rt=0)
                        id = studentid[matcheIndex]
                        print(id)
                        studentinfo = db.reference(f'Student/{id}').get()

                    if studentinfo['program']!=ecla:
                        messagebox.showerror("class error","You are not in this class")

                    else:
                        if counter == 0:
                            cvzone.putTextRect(imgbackground,'Loading',(275,400))
                            cv2.imshow("Face Attendance", imgbackground)
                            cv2.waitKey(1)

                            counter = 1
                            modeType = 1
                if counter != 0:
                    if counter == 1:
                        # Getting user details from the database


                        imgbackground[44:44 + 633, 808:808 + 414] = imgModelist[modeType]

                        print(studentinfo)
                        # Getting the image from the storage
                        blob = bucket.get_blob(f'images/{id}.png')
                        array = np.frombuffer(blob.download_as_string(), np.uint8)
                        imgstudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                        # updating attendance
                        datetimeobject = datetime.strptime(studentinfo['last_attendance_time'], '%Y-%m-%d %H:%M:%S')
                        secondElapsed = (datetime.now() - datetimeobject).total_seconds()
                        print(secondElapsed)
                        if secondElapsed > 30:
                            ref = db.reference(f'Student/{id}')

                            studentinfo['Total_Attendance'] += 1
                            ref.child('Total_Attendance').set(studentinfo['Total_Attendance'])
                            ref.child('last_attendance_time').set(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        else:
                            modeType = 3
                            counter = 0
                            imgbackground[44:44 + 633, 808:808 + 414] = imgModelist[modeType]
                    if modeType != 3:
                        if 10 < counter < 20:
                            modeType = 2
                        imgbackground[44:44 + 633, 808:808 + 414] = imgModelist[modeType]

                        if counter <= 10:
                            cv2.putText(imgbackground, str(studentinfo['Total_Attendance']), (861, 125),
                                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                            cv2.putText(imgbackground, str(studentinfo['program']), (1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.4,
                                        (255, 255, 255), 1)
                            cv2.putText(imgbackground, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                            cv2.putText(imgbackground, str(studentinfo['Standing']), (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                                        (100, 100, 100), 1)
                            cv2.putText(imgbackground, str(studentinfo['Year']), (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                                        (100, 100, 100), 1)
                            cv2.putText(imgbackground, str(studentinfo['gender']), (1125, 625), cv2.FONT_HERSHEY_COMPLEX,
                                        0.6, (100, 100, 100), 1)
                            (w, h), _ = cv2.getTextSize(studentinfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                            offset = (414 - w) // 2
                            cv2.putText(imgbackground, str(studentinfo['name']), (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX,
                                        1, (50, 50, 50), 1)
                            imgbackground[175:175 + 216, 909:909 + 216] = imgstudent

                            if counter<=1:
                                cur.execute("""UPDATE students SET status="""+"'present'"+""" WHERE id=""""\'" + id + "\'"""" and class=""""\'" + ecla + "\'"+""" and course=""""\'" +cou+"\'")
                            #     current_date_time = time.datetime.now()
                            #     formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
                            #     dbname = "\'" + str(studentinfo['name']) + "\'"
                            #     dbmajor = "\'" + str(studentinfo['program']) + "\'"
                            #     dbyear = "\'" + str(studentinfo['Year']) + "\'"
                            #     dbtotalattendance = "\'" + str(studentinfo['Total_Attendance']) + "\'"
                            #     dbdate = "\'" + formatted_date_time+ "\'"
                            #     dbid = "\'" + id + "\'"
                            #
                            #     cur.execute("""INSERT INTO Students(name,
                            #     Year,Major,Total_attendance,
                            #     date,
                            #     id) VALUES(""" + dbname + ",""" + dbyear + ",""" + dbmajor + ",""" + dbtotalattendance + ",""" + dbdate + ",""" + dbid + ")""")
                            #     conn.commit()
                            #     cur.close()
                            #     conn.close()
                            # conn=psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres",
                            #                  password="Zingaro1")
                            # cur=conn.cursor()
                            conn.commit()
                            cur.close()
                            conn.close()
                        conn = psycopg2.connect(host="localhost", dbname="apam", port="5432", user="postgres",
                                                                  password="Zingaro1")
                        cur=conn.cursor()



                        counter += 1
                        if counter >= 20:
                            counter = 0
                            imgstudent = []
                            studentinfo = []
                            modeType = 0
                            imgbackground[44:44 + 633, 808:808 + 414] = imgModelist[modeType]

            else:
                counter=0
                modeType=0


            cv2.imshow("Face Attendance",imgbackground)

            key=cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

button1 = Button(window, text="PROCEED", font=('calibri', 20, 'bold'), bg="blue", fg="white", relief=RIDGE,command=num)
button1.place(x=100, y=270)

button2 = Button(window, text="RESET", font=('calibri', 20, 'bold'), bg="red", fg="white", relief=RIDGE,command=reset)
button2.place(x=270, y=270)


window.mainloop()
