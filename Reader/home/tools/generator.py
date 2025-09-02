"""
Haochen Liu
hliu0010
540243105
"""

import os, random, time
from tools import other, permission
from text_generator.markov import generate_story
from tools.text import Text

#There are normal name for generate author name
first_names= [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Paul", "Ashley",
    "Steven", "Kimberly", "Andrew", "Donna", "Kenneth", "Emily", "George", "Michelle",
    "Joshua", "Carol", "Kevin", "Amanda", "Brian", "Dorothy", "Edward", "Melissa",
    "Ronald", "Deborah"]
last_names= [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts"]

text_dir=other.text_dir
user_dir=other.user_dir

#generate random name
def _generate_name():
    return f"{first_names[random.randint(0, len(first_names)-1)]} \
{last_names[random.randint(0, len(last_names)-1)]}"

def generate_texts(num:int = 100, wordcount:int = 3000) -> None:
    """
    In the file ("texts_database"), auto-generate text.
    The file names are sequentially numbered, with specific information in "info.in". 
    The configuration file "info.in" format:
    - start with the total document count
    - followed by each line containing story information
      (<index number>,<text name>,<author name>,<wordcount>,<whether or not need vip>)
    
    Parameters:
    - num (int): Total number generated
    - wordcount (int): Generate text with a length within a range of ±10%.
    """

    if not os.path.isfile(f"{text_dir}/info.in"):
        with open(f"{text_dir}/info.in", "w") as f:
            f.write("0")

    #Use the generator to read in the "info.in" configuration file
    info_field= permission.get_file(f"{text_dir}/info.in", text=False)
    tot_n= int(next(info_field))
    texts_info= []
    for i in range(num):
        #Generate text with a length within a range of ±10%.
        text_wordcount= wordcount+ random.randint(-(wordcount//10),(wordcount//10))
        #get story name and content
        tmp= generate_story(wordcount= text_wordcount)
        filename= tmp[0]
        content= tmp[1]
        #get random author name
        author_name= _generate_name()
        #get whether or not need vip
        vip_status= "False" if random.randint(0,4) else "True"
        texts_info.append(
            Text(tot_n+i+1,filename,author_name,text_wordcount,vip_status))
        #output story file
        with open(f"{text_dir}/{i+tot_n+1}.txt", "w") as f:
            f.write(content)
    
    #update the configuration file "info.in"
    with open(f"{text_dir}/tmp.in", "w") as f:
        f.write(f"{tot_n+num}\n")
        for line in info_field:
            f.write(line)
        for i in texts_info:
            f.write(i.text_info()+"\n")
    os.replace(f"{text_dir}/tmp.in", f"{text_dir}/info.in")

#generate random password
def _generate_password(length):
    characters= "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890.-_?"
    return ''.join(random.choice(characters) for i in range(length))

#generate reading date list
def _generate_datetime(num) -> list:
    start_time= time.mktime((2010, 1, 1, 0, 0, 0, 0, 0, 0))
    end_time= time.mktime((2024, 10, 31, 23, 59, 59, 0, 0, 0))

    #randomly generated timestamps
    random_time= [random.randint(int(start_time), int(end_time)) for i in range(num)]
    random_time= sorted(random_time)
    #formatted as a date
    return [time.strftime("%d-%m-%Y", time.localtime(i)) for i in random_time]

#generate reading time
def _generate_time():
    return f"{random.randint(0,5):02}:\
{random.randint(0,59):02}:\
{random.randint(0,59):02}"

def generate_users(num:int = 10):
    """
    In the file ("user_info"), auto-generate users.
    The user file format:
    - start with "<password>,<whether or not need vip>"
    - followed by each line containing story history
      (<story information(5)>,<reading duration>,<last reading date>)

    Parameters:
    - num (int): Total number generated
    """

    num= max(num,5)
    #read total number of texts
    tot_n= int(permission.get_firstline(f"{text_dir}/info.in"))

    #generate user information and two users are preset
    all_users= {(_generate_name(),     #user name
                _generate_password(random.randint(8,16)),  #password
                "False" if random.randint(0,5) else "True"   #vip_status
                ) for i in range(num-2)}
    all_users.add(("akali", "password", "True"))
    all_users.add(("karencat", "password", "False"))

    #provide all users information to debug 
    os.makedirs("user_info_debug")
    with open("user_info_debug/password.txt", "w") as f:
        for user in all_users:
            f.write(f"{user[0]},{user[1]},{'VIP' if user[2] == 'VIP' else 'Not VIP'}\n")

    #read all text information
    all_text= Text.get_texts_info()

    #generate the user file and the reading history
    for user in all_users:
        read_num= random.randint(10,100)
        read_time= _generate_datetime(read_num)
        with open(f"{user_dir}/{user[0]}.txt", "w") as f:
            #write encoded password and vip_status
            f.write(f"{other.encode_sha(user[1])},{user[2]}")
            for i in range(read_num):
                index=random.randint(1, tot_n)
                f.write("\n"+ all_text[index].text_info()+ ","+
                        _generate_time()+ ","+
                        read_time[i])

if __name__ == "__main__":
    pass
