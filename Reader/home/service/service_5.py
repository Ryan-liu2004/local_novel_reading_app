"""
Haochen Liu
hliu0010
540243105
USYD CODE CITATION ACKNOWLEDGEMENT
This file contains acknowledgements of code
"""

# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the majority of the following code has been taken
# from the website titled: "Assignment Part C - Submissions"
# and it is my previous work. 
#  
# Original URL
# https://edstem.org/au/courses/18651/lessons/62244/attempts?slide=421025
# Last access November, 2024

import os
from tools import other, permission
from tools.text import Text, User

#global variable to store user information (user name, vip_status)
user_info= [0,0]
MAX_LINE= other.MAX_LINE

def select_user() -> str | None:
    """
    Display a list of all users and prompt to select one.
    Returns the selected user, or None if the user chooses to exit.
    """

    #list all user files in the user directory
    all_user_list= os.listdir(f"{other.user_dir}")
    tot_n= len(all_user_list)
    start= 1

    #show user list
    while(start <= tot_n):
        count= 0

        #show user list
        print(
f"""**************************************************
{"USYD Story Reader User List": ^50}
**************************************************""")

        #maximum MAX_LINE text information at one page
        for i in range(start, tot_n+1):
            user= all_user_list[i-1][:-4]
            print(f"{start+count:3}. {user}")
            count+= 1
            if count == MAX_LINE:
                break
        print("**************************************************")
        start+= MAX_LINE

        opt= input(
"""Press any key to turn to the next page,\n\
or enter the corresponding user number to compare,\n\
or press Q to return: """)
        other.clear()
        if other.opt_input(opt, 
            lambda opt: 1 <= opt and opt <= tot_n):
            opt= int(opt)
            return all_user_list[opt-1][:-4]
        else:
            if opt=='Q' or opt == 'q':
                return None

    #show user list again
    return select_user()

def load_user_history(user_path: str) -> set["Text"]:
    """
    Load the reading history of a user from their file.
    Returns a set of "Text" objects
    """

    user_field= permission.get_file(user_path, text= False)
    next(user_field)

    #load all reading history for this user
    return {User.init(line).get_index() for line in user_field}

def select_mode(target_user: str) -> int:
    """
    Display mode options for comparing reading history with another user.
    Returns the selected mode as an integer.
    """

    flag=0
    while(True):
        #display options for comparing reading histories
        opt= input(
f"""**************************************************
{"USYD Story Reader Comparing Mode Operation": ^50}
**************************************************
Comparing with: {target_user}
1. Find combined interests. (Seen by one person)
2. Find common interests. (Seen by both)
3. Only I have read.
4. Only {target_user} has read.
5. Query similarity score.

Please enter a{' valid' if flag else ''} operation number: """)
        flag=1
        other.clear()
        if other.opt_input(opt, 
            lambda opt: 1 <= opt and opt <= 5):
            return int(opt)

def combined(user1: set, user2: set) -> set:
    """
    Find stories read by either user1 or user2 (combined interests).
    """
    return user1 | user2
def common(user1: set, user2: set) -> set:
    """
    Find stories read by both user1 and user2 (common interests).
    """
    return user1 & user2
def unique(user1: set, user2: set) -> set:
    """
    Find stories only read by user1 and not by user2.
    """
    return user1 - user2
def similarity_score(user1: set, user2: set) -> float:
    """
    Calculate a similarity score
    """
    return round(5*len(user1 & user2)/
                 (len(user1 | user2)+ len(user1 ^ user2)),2)

def show_ans(ans: set):
    """
    Display query results (a set of stories).
    """

    ans=list(ans)
    tot_n=len(ans)
    start= 1

    #show result list
    while(start <= tot_n):
        count= 0

        #show result list
        print(
f"""**************************************************
{"Query Results": ^50}
**************************************************""")

        #maximum MAX_LINE text information at one page
        for i in range(start, tot_n+1):
            book=ans[i-1]
            print(
f"{start+count:3}. {book.get_text_name()}, By {book.get_author()}")
            count+= 1
            if count == MAX_LINE:
                break
        print("**************************************************")
        start+= MAX_LINE

        #ask option
        opt= input("""Press any key to turn to the next page,
or press Q to return: """)
        other.clear()
        if opt=='Q' or opt == 'q':
            return
    #show results again
    show_ans(ans)

def comparing(user: list):
    """
    Main function to compare the reading history of the current user with another user.
    """

    global user_info
    user_info= user
    
    if permission.check(user= user_info[1], func= True) == None:    #need vip
        return
    
    target_user= select_user()
    if target_user == None:
        return

    #load reading histories of both users
    user_history= load_user_history(f"{other.user_dir}/{user_info[0]}.txt")
    target_history= load_user_history(f"{other.user_dir}/{target_user}.txt")
    all_texts_list= Text.get_texts_info()
    user_history= {all_texts_list[i] for i in user_history}
    target_history= {all_texts_list[i] for i in target_history}

    #select comparison mode
    opt= select_mode(target_user)
    if opt == 1:
        ans= combined(user_history, target_history)
    elif opt == 2:
        ans= common(user_history, target_history)
    elif opt == 3:
        ans= unique(user_history, target_history)
    elif opt == 4:
        ans= unique(target_history, user_history)
    else:
        ans= similarity_score(user_history, target_history)
        print(
f"""**************************************************
{"Query Results": ^50}
**************************************************
Your similarity score: {ans}
**************************************************\n""")
        input("Press any key to return  ")
        return

    if opt != 5:
        show_ans(ans)

if __name__ == "__main__":
    pass
