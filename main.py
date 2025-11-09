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


import os, shutil
from tools import other, generator, password
from service import main_service as s
from tools.text import Text, User
#from text_generator.markov import generate_story

user_info= [0,0]

#show main service interface
def main_interface() -> int:
    """
    Display the main service menu and prompt the user for input.
    Returns the selected service option as an integer.
    """

    other.clear()
    flag=0
    while(True):
        opt= input(
f"""**************************************************
{"USYD Story Reader Service": ^50}
**************************************************
Please select from the following services 
by entering the service number (0-5). 
Enter 0 to exit.

1. Enter reading mode, and open the library.
2. Purchase VIP membership.
3. Annual or monthly reading history statistics.
4. Bestselling story rankings
5. Compare reading history with other users 
   to find similarities and differences. (Only VIP)

Please enter a{' valid' if flag else ''} service number: """)
        flag=1
        if other.opt_input(opt, 
            lambda opt: 0 <= opt and opt <= 5):
            return int(opt)

def main():
    """
    Main application loop. Handles user login, displays the main interface,
    and routes the user to the selected service.
    """

    global user_info

    #welcome user and log in
    user_info= password.welcome()
    if user_info == None:
        return
    user_info= [user_info[0], user_info[1]]

    while(True):
        opt= main_interface()
        other.clear()
        if opt == 0:
            print("Thank you for using our service. See you next time!")
            return
        #loading service function in service/main_service.py
        else:
            s.service(user_info, opt)

def init():
    """
    Randomly generate multiple stories and users, 
    and add users' browsing history.

    If the environment does not exist, 
    the environment is automatically generated
    """
    if not os.path.exists(f"{generator.text_dir}"):
        os.makedirs(f"{generator.text_dir}")

        #generate 20 texts and each text with approaximately 50000 words
        generator.generate_texts(20, 50000)

    if not os.path.exists(f"{generator.user_dir}"):
        os.makedirs(f"{generator.user_dir}")
        
        #generate 20 users with reading history
        generator.generate_users(20)

def remove_environment():
    """
    Remove all text and user file
    """
    if os.path.exists(f"{generator.text_dir}"):
        shutil.rmtree(f"{generator.text_dir}")
    if os.path.exists(f"{generator.user_dir}"):
        shutil.rmtree(f"{generator.user_dir}")
    if os.path.exists("user_info_debug"):
        shutil.rmtree("user_info_debug")

if __name__=="__main__":
    remove_environment()
    init()
    main()
    #remove_environment()

