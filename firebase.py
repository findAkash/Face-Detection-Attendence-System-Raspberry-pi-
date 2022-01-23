import pyrebase
import urllib

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
# auth=firebase.auth()
# storage = firebase.storage()
#
# storageRef = firebase.storage().ref("attende/")

# a =storageRef.listAll()
# print(a)

# storage:
# filename=input("Enter the name of the file you want to upload")
# a=storage.child('attende/').get_all()
# f = urllib.request.urlopen(a).read()
#
# print(f)

# fb = firebase.FirebaseApplication("https://fda-system-default-rtdb.firebaseio.com/", None)
#
data = {
    'Name': 'Akash Karmacharya',
    'date_time': '1990/01/02, 303221'
}
db.push(data)
#
# a=firebase.post('fda-system-default-rtdb/Attendance:', data)
# print(a)