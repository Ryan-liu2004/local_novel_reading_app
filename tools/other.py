"""
Haochen Liu
hliu0010
540243105
"""

#This file contain other useful function
import os, hashlib

#pathway to texts and user database
text_dir= "texts_database"
user_dir= "user_info"
MAX_LINE= 5

#perform SHA-256 encryption.
def encode_sha(password: str) -> str:
    hash_object= hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def clear():
    os.system("clear")

#validate the legality of the input option.
def opt_input(opt: str, func) -> bool:
    try:
        opt= int(opt)
        if func(opt):
            return True
        raise Exception
    except Exception:
        return False

if __name__ == "__main__":
    pass
