import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#to read the data from cloud
# Store data in firebase
import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyCtwVK_5xMbp_rUSbIbO-m8SOiMbtyRmCg",
    'authDomain': "face-recog-attend.firebaseapp.com",
    'projectId': "face-recog-attend",
    'storageBucket': "face-recog-attend.appspot.com",
    'messagingSenderId': "29205294227",
    'appId': "1:29205294227:web:a44a61729af58bcb9db166",
    'measurementId': "G-CPQEVH4YCJ",
    'databaseURL': "https://face-recog-attend-default-rtdb.firebaseio.com/"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# import face_recognition

path = 'attende'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    splited = os.path.splitext(cl)[0]
    classNames.append(os.path.splitext(splited)[0])
print(classNames)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(img)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        idList = []
        print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dtString}')
            print('Attendance stored locally')
            data = {
                'name': name,
                'date_time': dtString
            }
            db.push(data)
            print('Attendance stored in firebase')


encodeListKnown = findEncodings(images)
# print(len(encodeListKnown))

cap = cv2.VideoCapture(0)
flag=0
while flag==0:
    sucess, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        # print(faceDis)
        # print(matches)
        # print(matchIndex)
        # print(matchIndex)
        # if matchIndex<0:
        #     name = 'Unknow Face'
        #     # print(name)
        #     y1, x2, y2, x1 = faceLoc
        #     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        #     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        #     cv2.putText(img, name, (x1 + 12, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        #     print("Atendee is not registered, contact to admin")
        #     flag = 1
        #     break
        #
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+12, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            # if count >= 10:
            #     print("Attendend Success")
            #     break
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)

