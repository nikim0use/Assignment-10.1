import os

print('This is your current Directory Path: ')

current_dir = os.getcwd()
print (current_dir)


user_dir = input("What is the Directory Path you want? ")

file_name = input("What do you want to name your file? ")

does_dir_exist = os.path.exists(user_dir)

if not does_dir_exist:
    #creat directory
    os.makedirs(user_dir)
    print('You made a new Directory!')

#get user input for file input
user_name = input('What is your name?')
user_address = input('What is your address?')
user_phone = input('What is your phone number?')

try:
    with open(file_name, 'w') as file_object:
        file_object.write(user_name)
        file_object.write(user_address)
        file_object.write(user_phone)
except PermissionError:
    print('This file is already created')

with open(file_name, 'r') as file_object1:
    for line in file_object1:
        print("This is your program output")
        print(line.rstrip())