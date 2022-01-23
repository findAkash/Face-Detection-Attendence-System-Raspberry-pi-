import os
print('Welcome to face recognition attendence system')
print('Choose your choice')
print('Press 1 for New Registration')
print('Press 2 for Make attendence')
option = input('Enter your choice: ')
if option=='1':
    os.system('python generate_dataset.py')

elif option=='2':
    os.system('python attendance.py')
