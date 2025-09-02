"""
Haochen Liu
hliu0010
540243105
"""
import time
from tools import other, permission
from tools.text import Text, User

#global variable to store user information (user name, vip_status)
user_info= [0,0]
year= 2024
month= 1

def search_history(judge_func) -> dict["Text", int]:
    """
    Search and filter the user's reading history

    Returns a dictionary 
    with "Text" objects as keys and reading durations as values.
    """
    
    #open user's reading history file
    user_field= permission.get_file(
                    f"{other.user_dir}/{user_info[0]}.txt",
                    text= False)
    next(user_field)

    #initialize a dictionary to store results
    dict_ans: dict["Text", int]= {}
    for line in user_field:
        user_history= User.init(line)
        #filter by specify the month and year
        if judge_func(user_history.get_date_month(),
                      user_history.get_date_year()):
            dict_ans[user_history]= dict_ans.get(user_history, 0)+\
                                    user_history.get_duration()
    
    return dict_ans

def statistics(user: list):
    """
    Display reading statistics for the user 
    based on reading duration and word count

    The user can choose to filter by month or by year.
    """

    while(True):
        #prompt user to choose between monthly or yearly statistics
        opt= input("""Which would you like to view?
1. Monthly reading history
2. Annual reading history

Please enter the corresponding number (1 or 2): """)

        if other.opt_input(opt, lambda opt: opt == 1 or opt == 2):
            opt= int(opt)
            break
        else:
            other.clear()
            print("Please enter a valid number!\n")
    other.clear()

    global user_info, year, month
    user_info= user
    if opt == 1:
        #prompt for specified month
        while(True):
            month=input("Specify the month (1-12) that you want to display: ")
            if other.opt_input(month, lambda opt: 1 <= opt and opt <= 12):
                month= int(month)
                break
            else:
                print("Please enter a valid number!\n")

    if opt == 1 or opt == 2:
        #prompt for specified year
        while(True):
            year= input("Specify the year (2010-2024) that you want to display: ")
            if other.opt_input(year, lambda opt: 2010 <= opt and opt <= 2024):
                year= int(year)
                break
            else:
                print("Please enter a valid number!\n")
    other.clear()

    if opt == 1:
        func= lambda m, y: m == month and y == year
    elif opt == 2:
        func= lambda m, y: y == year 
    #find the reading history for the corresponding time.
    reading_dict= search_history(func)
    if len(reading_dict) == 0:
        print("No reading history found.","\U0001F61F")
        time.sleep(3)
        return
    duration_dict= {value: key for key,value in reading_dict.items()}
    wordcount_dict= {key.get_wordcount(): key for key in reading_dict.keys()}

    #find the story with the longest reading time.
    max_duration= duration_dict.get(max(duration_dict))
    #find the story with the largest word count.
    max_wordcount= wordcount_dict.get(max(wordcount_dict))
    #find total reading time
    tot_duration= sum(duration_dict)
    #find total reading word count
    tot_wordcount= sum(wordcount_dict)

    #display statistics
    print(
f"""**************************************************
{'Reading History Statistics': ^50}
**************************************************""")
    #display top stories by reading time and word count
    tmp= [["Top", "Story Name", "", ""],
          ["Reading Time", max_duration.get_text_name(), max_duration.get_author(),
           User.duration_converts(reading_dict.get(max_duration))],
          ["Word Count", max_wordcount.get_text_name(), max_wordcount.get_author(),
           f"{max_wordcount.get_wordcount()} words"]]
    for i in tmp:
        print(f"{i[0]: <14}{i[1]: <24}{i[3]: >12}")
        if i[0] != "Top":
            print(f"{' '*14}By: {i[2]}")
    print("**************************************************")

    #display total reading count, time, and word count
    tmp= [["Total Reading Count:",f"{len(reading_dict)} text(s)"],
          ["Total Reading Time:",
           f"{tot_duration//86400:02}:{User.duration_converts(tot_duration%86400)}"],
          ["Total Word Count:",f"{tot_wordcount} words"]]
    for i in tmp:
        print(f"{i[0]: <25}{i[1]: >25}")
    print("**************************************************")
    #finish display
    input("Press any key to return  ")

if __name__ == "__main__":
    pass
