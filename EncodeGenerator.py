import  cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
def encods():
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://database-72071-default-rtdb.firebaseio.com/",
        "storageBucket": "database-72071.appspot.com"
    })
    folderpath = 'images'
    path_list=os.listdir(folderpath)
    imglist = []
    studentid = []
    # importing images into a list
    for path in path_list:
        imglist.append(cv2.imread(os.path.join(folderpath,path)))
        # getting student id from it's name
        studentid.append(os.path.splitext(path)[0])

        fileName=f'{folderpath}/{path}'
        bucket=storage.bucket()
        blob=bucket.blob(fileName)
        blob.upload_from_filename(fileName)

    def findEncodings(imagesList):
        encodelist=[]
        for img in imagesList:
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encodelist.append(encode)


        return encodelist
    print("Encoding Started")
     # saving the encodings in a pickel file
    EncodeKnownlist=findEncodings(imglist)
    print(EncodeKnownlist)
    encodeListKnownIds=[EncodeKnownlist,studentid]
    print("Encoding complete")
    file=open("EncodeFile.p",'wb')
    pickle.dump(encodeListKnownIds,file)
    file.close()
    print("file save")
