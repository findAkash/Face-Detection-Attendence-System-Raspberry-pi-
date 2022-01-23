import cv2
import os

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
    'databaseURL': ""
  }
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()




def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


attendee_name = input('enter attendee name: ')
attendee_id = input('enter attendee id: ')

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('I:\\5th sem\\IOT\\Indi\\haarcascade_frontalface_default.xml')
count = 0

assure_path_exists("I:\\5th sem\\IOT\\Indi\\Attende\\")
while (True):
    _, image_frame = cap.read()
    img_rgb = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
    faces = face_detector.detectMultiScale(img_rgb, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("I:\\5th sem\\IOT\\Indi\\Attende\\" + str(attendee_name) + '.' + str(attendee_id) + ".jpg", img_rgb[y:y + h, x:x + w])
        cv2.imshow('frame', image_frame)

        attendee_img ='attende/'+str(attendee_name) + '.' + str(attendee_id)+ ".jpg"

        print(attendee_img)
        storage.child(attendee_img).put(attendee_img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    elif count >= 1:
        print("Successfully Captured")
        break

cap.release()
cv2.destroyAllWindows()
