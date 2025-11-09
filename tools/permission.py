"""
Haochen Liu
hliu0010
540243105
"""

#This module use Decorator to manage all "Permission Management" for vip users
#including read file, vip function
import time
from typing import Generator, Optional
function_permission= True
user_permission= False

def permission_check(func):
    """
    Determine if user have access to a resource based on 
    whether or not user have a vip
    """
    def wrapper(*args, **kwargs):
        #Determine whether or not user have permission
        if function_permission and not user_permission:
            print("Sorry, you do not have permission \
to use this function, please purchase vip")
            time.sleep(3)
            return None
        res=func(*args, **kwargs)
        return res
    return wrapper

#Using Decorators to check permission
@permission_check
def _get_field(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line

def get_file(filepath: str, user: bool = False, *, text: bool = True) -> Optional[Generator]:
    """
    Read the file and perform a permission check.

    Parameters:
    - filepath (str): The path to the text file.
    - user (bool): Whether the user has permission to access the file.
    - text (bool): Whether the file requires permission to read.

    Returns:
    - Optional[Generator]: A generator yielding file content if permissions are granted, otherwise None.
    """

    global function_permission, user_permission
    user_permission= user
    function_permission= text
    return _get_field(filepath)

def get_firstline(filepath: str):
    """
    Only return the first line of text, no permissions required.
    """
    field=get_file(filepath, text= False)
    line=next(field)
    field.close()
    return line

#Using Decorators to check permission
@permission_check
def _check_permission():
    return True

def check(*, user: bool = False, func: bool = True) -> bool | None:
    """
    Perform a permission check.

    Parameters:
    - user (bool): Whether the user has permission to access the function.
    - func (bool): Whether the function requires permission.

    Returns:
    - True | None: Return True if user has permission, otherwise None.
    """

    global function_permission, user_permission
    user_permission= user
    function_permission= func
    return _check_permission()

if __name__ == "__main__":
    pass
