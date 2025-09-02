"""
Haochen Liu
hliu0010
540243105
USYD CODE CITATION ACKNOWLEDGEMENT
This file contains acknowledgements of code
"""

# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the majority of the following code has been taken
# from the website titled: "Assignment Part B - Submissions"
# and it is my previous work. 
#  
# Original URL
# https://edstem.org/au/courses/18651/lessons/61238/attempts?slide=414789
# Last access November, 2024

import os, time
from tools import other, generator
from tools.permission import get_firstline

user_name=""
password=""
vip_status=False

def check_password()-> bool:
    '''
    Verify the authentication of the user
    if <user_name>.txt does not exist, return False
    if password does not match the first line in <user_name>.txt, return False
    if password matches the first line in <user_name>.txt, return True
    
    @Parameters
    - user_name (str,global): the input username
    - password (str): the input password

    @Returns
    - bool: whether the password and username are correct
    '''
    global user_name, password, vip_status
    user_path=f"{generator.user_dir}/{user_name}.txt"
    if not os.path.isfile(user_path):
        print(f"No {user_name} found :((")    #username does not exist
        return False
    
    #read password and vip_status
    line= get_firstline(user_path)
    tmp= line.strip().split(',')
    file_password= tmp[0]
    vip_status= True if tmp[1] == "True" else False
    
    #do not match password
    if file_password!=other.encode_sha(password):
        print("Username and password do not match :((")
        return False
    #match password
    print("Login successful :))")
    if vip_status:
        print("Welcome, esteemed VIP user.")
    time.sleep(2)
    return True

def welcome() -> tuple:
    # Display the welcoming message
    print("Welcome to USYD Story Reader!")

    # Prompting for username and password
    global user_name, password, vip_status 
    user_name= input("Enter your username: ")
    password= input("Enter your password: ")
    # Check whether 3 limited attempts has been reached
    cnt= 0   #set up a counter to represent the number of attempts
    while(not check_password()):
        cnt+= 1
        if cnt == 3:
            break
        user_name= input("Enter your username: ")
        password= input("Enter your password: ")

    if cnt == 3:    #3 attempts has been reached.
        print("\nMaximum of 3 attempts has been reached.\nYou will be temporarily disabled from logging in :((")
        return None
    other.clear()
    return (user_name, vip_status)

if __name__ == '__main__':
    welcome()
