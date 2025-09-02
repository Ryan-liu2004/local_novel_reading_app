"""
Haochen Liu
hliu0010
540243105
USYD CODE CITATION ACKNOWLEDGEMENT
This file contains acknowledgements of code
"""


# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the majority of the following code has been taken
# from the website titled: "Example: A program generating text (Advanced)"
# and it is not my own work. 
#  
# Original URL
# https://edstem.org/au/courses/18651/lessons/63631/slides/435530
# Last access November, 2024

from tools.permission import get_file
import sys, os, random

def generate_story(filename= "Romeo and Juliet.txt", wordcount= 300, linelength= 15):
    """
    Generates a story based on the text in a specified file using a Markov chain model.

    Parameters:
    - filename (str): The path to the text file to use as the source.
    - wordcount (int): The number of words to generate in the story.
    - linelength (int): The maximum number of words per line for readability.

    Returns:
    - tuple: The story name and a generated story based on the input text.
    """

    allwords = []
    model = {}
    text_path = os.path.join(f"text_generator/{filename}")
    _makemodel(text_path, allwords, model)
    return _generate(allwords, model, wordcount, linelength)

def _makemodel(text_path, allwords, model):
    # read the words
    for line in get_file(text_path, text=False):
        allwords += [w for w in line[:-1].split() if w[0].isalpha()]
    # generate the model
    for count in range(len(allwords)-2):
        prefix = (allwords[count], allwords[count+1])
        follower = allwords[count+2]
        if prefix not in model:
            model[prefix] = [follower]
        else:
            model[prefix] += [follower]

def _generate(allwords, model, wordcount, linelength):
    startwords = (allwords[0], allwords[1])
    ans=""
    #generate story
    for wordcount in range(1, wordcount+1):
        word = model[startwords][random.randrange(0, len(model[startwords]))]
        if (wordcount%linelength) == 0:
            ans+=f"{word}\n"
        else:
            ans+=f"{word} "
        startwords = (startwords[1], word)
    ans+="\n"
    #generate story name
    story_name=""
    n=random.randint(2,5)
    tmp=random.randint(0,len(allwords)-10)
    startwords= (allwords[tmp], allwords[tmp+1])
    for i in range(1, n+1):
        startwords=(startwords[1], model[startwords][random.randrange(0, len(model[startwords]))])
        story_name+= f"{startwords[1]} "
    story_name=story_name.replace(",", "")
    return (story_name[:-1],ans)

if __name__=="__main__":
    print(generate_story())


