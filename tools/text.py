"""
Haochen Liu
hliu0010
540243105
"""
from tools.permission import get_file
from tools import generator

class Text:
    def __init__(self, index: int, text_name: str, author_name: str, 
                 wordcount: int, vip_status: str):
        """
        Initializes a Text object with essential attributes, including index, name, author, word count, 
        VIP status, duration, and date.

        Parameters:
        - index (int): A unique identifier for the text.
        - text_name (str): The name of the text.
        - author_name (str): The name of the author of the text.
        - wordcount (int): The total number of words in the text.
        - vip_status (str): Indicates whether the text is for VIP users only; 
                            True if VIP, False if not.

        Attributes:
        - index (int): Stores the unique identifier for the text.
        - text_name (str): Stores the name or title of the text.
        - author_name (str): Stores the author's name.
        - wordcount (int): Stores the word count of the text.
        - vip_status (bool): Indicates whether the text requires VIP access.
        """
        self.index= int(index)
        self.text_name= text_name
        self.author_name= author_name
        self.wordcount= int(wordcount)
        if type(vip_status) == bool:
            self.vip_status=vip_status
        else:
            self.vip_status= True if vip_status == "True" else False
    
    #getter for all instances
    def get_index(self):
        return self.index
    def get_text_name(self):
        return self.text_name
    def get_author(self):
        return self.author_name
    def get_wordcount(self):
        return self.wordcount
    def get_vip(self):
        return self.vip_status

    #another init function
    def init(info: str) -> "Text":
        tmp=info.strip().split(',')
        return Text(*tmp)

    #print text information
    def text_info(self):
        return f"{self.index},{self.text_name},\
{self.author_name},{self.wordcount},{self.vip_status}"

    def get_texts_info() -> dict[int: "Text"]:
        info_field= get_file(f"{generator.text_dir}/info.in", text= False)
        next(info_field)
        return {Text.init(line).index: Text.init(line) for line in info_field}

class User(Text):
    def __init__(self, index: int, text_name: str, author_name: str, wordcount: int, 
                 vip_status: str, duration: str, date: str):
        """
        Initializes a User object with essential attributes, including index, name, author, word count, 
        VIP status, duration, and date.

        Parameters:
        - duration (str): The reading or playback duration of the text in the format "HH:MM:SS". 
                        Defaults to "00:00:00".
        - date (str): The publication or creation date of the text in the format "DD-MM-YYYY". 
                    Defaults to "31-10-2024".

        Attributes:
        - duration (str): Stores the duration in "HH:MM:SS" format after conversion.
        - date (str): Stores the date in "DD-MM-YYYY" format.
        """
        super().__init__(index, text_name, author_name, wordcount, vip_status)
        self.duration= User._duration_converts(duration)
        self.date= date
    
    #getter for all instances
    def get_duration(self):
        return self.duration
    def get_date(self):
        return self.date
    def get_date_year(self):
        return int(self.date[-4:])
    def get_date_month(self):
        return int(self.date[3:5]) 

    #another init function
    def init(info: str) -> "User":
        tmp=info.strip().split(',')
        return User(*tmp)
        
    #return Text information
    def get_Text(self) -> "Text":
        return Text(self.index, self.text_name, 
            self.author_name, self.wordcount, self.vip_status)

    #print user information
    def user_info(self):
        return super().text_info()+ f",{User.duration_converts(self.duration)},{self.date}"

    #convert(duration) str to int
    def _duration_converts(duration: str) -> int:
        tmp= duration.split(':') #format hh:mm:ss
        h= int(tmp[0])
        m= int(tmp[1])   #minutes
        s= int(tmp[2])   #seconds
        return h*3600+m*60+s
    
    #convert(duration format) int to str
    def duration_converts(duration: int) -> str:
        return f"{duration//3600:02}:{duration//60%60:02}:{duration%60:02}"

if __name__ == '__main__':
    pass
