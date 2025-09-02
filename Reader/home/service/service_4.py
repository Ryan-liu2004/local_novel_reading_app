"""
Haochen Liu
hliu0010
540243105
"""
import os
from tools import other, permission
from tools.text import Text, User

#global variable to store user information (user name, vip_status)
user_info= [0,0]
MAX_LINE= other.MAX_LINE

def show_rank(rank: list):
    """
    Display the ranking list of bestselling stories.
    """

    #load all stories
    all_texts_info= Text.get_texts_info()
    tot_n= len(rank)
    start= 1

    #show rank list
    while(start <= tot_n):
        count= 0
        #show rank list
        print(
f"""**************************************************
{"Bestselling Story Rank": ^50}
**************************************************""")
        #maximum MAX_LINE text information at one page
        tmp=[]
        for i in range(start, tot_n+1):
            book= all_texts_info[rank[i-1][0]]
            tmp.append([f"{start+count:3}.", 
                        f"{book.get_text_name()}({book.get_index()})", 
                        rank[i-1][1]])
            count+= 1
            if count == MAX_LINE:
                break
        start+= MAX_LINE

        print(f"Top{' '*3}Story Name(Index Number){' '*10}View Count")
        for i in tmp:
            print(f"{i[0]: <6}{i[1]: <40}{i[2]: >4}")
        print("**************************************************")
        opt= input(
"""Press any key to turn to the next page,
or press Q to return: """)
        other.clear()
        if opt == 'Q' or opt == 'q':
            return

    #show rankings list again
    show_rank(rank)

def rankings(user: list):
    """
    Generate and display rankings based on user view counts for each story.
    """

    global user_info
    user_info= user
    
    #list all user files in the user directory
    all_user_list= os.listdir(f"{other.user_dir}")
    rank_dict= {} #dictionary to store story view counts

    #open each user file to retrieve view history
    for i in all_user_list:
        user_field= permission.get_file(
                        f"{other.user_dir}/{i}",
                        text= False)
        next(user_field)

        #load all reading history for this user
        tmp_set={User.init(line).get_index() for line in user_field}
        for i in tmp_set:
            rank_dict[i]= rank_dict.get(i, 0)+ 1
    
    #sort the rank_dict by view counts in descending order
    rank= sorted(rank_dict.items(), key= lambda item: item[1], reverse=True)

    show_rank(rank)

if __name__ == "__main__":
    pass
