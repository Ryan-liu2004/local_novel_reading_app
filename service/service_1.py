"""
Haochen Liu
hliu0010
540243105
"""
import time
from tools import other, permission
from tools.text import Text, User

#global variable to store user information [user name, vip_status]
user_info= [0,0]
#maximum number of lines displayed per page
MAX_LINE= other.MAX_LINE


def add_history(func):
    """
    Add the current reading history, including duration and date.
    """
    def wrapper(*args, **kwargs):
        #Start timing.
        start= int(time.time())
        res= func(*args, **kwargs)
        end= int(time.time())

        if res:     #having permission to read this text
            user_history= User.init(
                f"{args[0].text_info()},\
{User.duration_converts(end-start)},\
{time.strftime('%d-%m-%Y', time.localtime(end))}")
            #append the reading history at the end of the user history file
            with open(
                f"{other.user_dir}/{user_info[0]}.txt",
                "a") as f:
                f.write('\n'+user_history.user_info())

        return res
    return wrapper

@add_history
def open_text(text: "Text"):
    """
    Function to open and display text content if the user has permission.
    """

    other.clear()
    #loading text and check permission
    text_field= permission.get_file(
                f"{other.text_dir}/{text.get_index()}.txt", 
                user= user_info[1],
                text= text.get_vip())
    other.clear()
    if text_field == None:    #need permission
        return False

    #show shory content
    print(f"story name: {text.get_text_name()}, \
author: {text.get_author()}, \
word count: {text.get_wordcount()}\n")
    count= MAX_LINE
    
    while(count == MAX_LINE):
        count= 0
        for line in text_field:
            print(line, end= '')
            count+= 1
            if count == MAX_LINE:
                break

        opt= input("\nPress any key to turn to the next page,\
or press Q to end reading: ")
        other.clear()
        if opt == 'Q' or opt == 'q':
            return True
    return True

def open_database(user: list):
    """
    Function to open the database and display texts list.
    """
    global user_info
    user_info= user
    path= other.text_dir
    #get all texts
    all_texts_info= Text.get_texts_info()
    tot_n=len(all_texts_info)
    start= 1

    #show texts list
    while(start <= tot_n):
        count= 0
        #show text list
        print(
f"""**************************************************
{"Story list": ^50}
**************************************************""")
        #maximum MAX_LINE text information at one page
        for i in range(start, tot_n+1):
            book= all_texts_info[i]
            vip_need= "Only vip" if book.get_vip() else "Free"
            print(f"{f'{book.get_index(): 3}. {book.get_text_name()}': ^50}")
            print(f"Author: {book.get_author():<20}      status: {vip_need: >}")
            count+= 1
            if count == MAX_LINE:
                break
        print("**************************************************")
        start+= MAX_LINE

        #ask option
        opt= input("""Press any key to turn to the next page,
or enter the corresponding story number to read,
or press Q to return: """)
        if other.opt_input(opt, 
            lambda opt: 1 <= opt and opt <= tot_n):
            opt= int(opt)
            open_text(all_texts_info[opt]) #open text
            break
        else:
            other.clear()
            if opt=='Q' or opt == 'q':
                return

    #show text list again
    open_database(user)

if __name__ == "__main__":
    pass
