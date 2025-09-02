"""
Haochen Liu
hliu0010
540243105
"""
import os, time
from tools import other, permission

#global variable to store user information (user name, vip_status)
user_info= [0,0]

def purchase_vip(user: list):
    """
    Function to handle VIP purchase for a user.
    """
    global user_info
    user_info= user

    if user_info[1]:
        print("You are already a VIP user.", "\U0001F604")
        time.sleep(3)
        return

    #define the path to the user file and a temporary file
    user_path= f"{other.user_dir}/{user_info[0]}.txt"
    tmp_path= f"{other.user_dir}/tmp.txt"

    user_field= permission.get_file(user_path, text= False)
    line= next(user_field)
    line=line.strip().split(',')[0]
    #rewrite user file
    with open(tmp_path, "w") as f:
        f.write(f"{line},{True}\n")
        for line in user_field:
            f.write(line)
    os.replace(f"{other.user_dir}/tmp.txt", user_path)
    user[1]= True
    print("Purchase successful! Thank you for your patronage.", "\U0001F604")
    time.sleep(3)
    return

if __name__ == "__main__":
    pass
