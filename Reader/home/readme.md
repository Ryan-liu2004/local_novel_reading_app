## Introduction

# A brief introduction

This is a novel reading app which can generate several novel texts and 
users along with reading history.

Users can browse books, purchase VIP membership, view annual and monthly reading statistics, 
check the bestselling stories list, and compare browsing history with other users.

# Usage instructions:

Located in the home folder, enter **python main.py** in the terminal.

Then, two users have been preset.
(username: akali, password: password, with VIP)
(username: karencat, password: password, without VIP)

Since SHA-256 encryption is used for verification,
if you need to view other usernames and passwords, 
please open "home/user_info_debug/password.txt" to find them.

Then, just follow the prompts displayed by the program.

-----------------------------------------------------------------------------------
## Advanced Concepts Implement

This project uses "Dictionary And Set Comprehension", "Generators", and "Decorators".
And it also uses "Class Inheritance" but without special methods or class variables.

# Dictionary And Set Comprehension

All story information extraction and complete user browsing history 
use dictionary and set operations. 

And using dictionary or set comprehension simplify the code.

For example, on line 83 in "home/service/service_5.py", load_user_history() 
is used to load a user's reading history. Using a set comprehension here can simplify the code. 
Since only the books that the user has read are needed, the set's uniqueness can be utilized 
to remove duplicates. Additionally, if the user chooses to compare common interests with others, 
this can be achieved using set intersection logic.

# Decorators

In "home/tools/permission.py", the decorator (@permission_check) 
is used to manage permissions, determining whether the current user has VIP status 
to access specific functions or content.

In "home/service/service_1.py", the decorator (@add_history)
is used to record the reading time and date after the user finishes reading a text,
and it adds the reading history to the user's file.

This approach avoids the need to add code after each "return" statement, 
making it cleaner, readable, and reusable.

# Generators 

In the "home/tools/permission.py", the function (_get_field) use generators 
to prevent memory crashes caused by reading very large files,
and permission has been checked by the decorator.

In this project, all text file opening operations call this function, 
and a generator is used to read the file based on its return.

For example, when reading a novel, lazy evaluation is used to 
load only the current page, improving efficiency.

-----------------------------------------------------------------------------------
## Other Advanced Concepts

# Numpy

Most operations in this project involve string manipulation rather than 
arithmetic operations on numbers. Only the reading history statistics and 
bestseller list functions involve numerical operations, and these are simple 
additions with a small data volume. Using NumPy would reduce code readability, 
and the required type conversions would decrease efficiency.

In artificial intelligence or data processing, there are extensive algebraic computation, 
including linear operations. Frequent calls, modifications, and computations can make lists inefficient, 
but using NumPy can improve runtime speed. 

In this project, for example, if a function is added for analyzing all users' reading behaviors, 
the statistical tools in NumPy might be necessary.

# Class Inheritance with Class Variables/Special Methods: 

This project uses class inheritance but does not use special methods or class variables. 
The Text and User classes are defined in "home/tools/text.py” to facilitate the conversion 
and storage of the loaded novel information and user browsing records. Since there is no need 
to track class states or information, class variables are unnecessary. 
Additionally, since there is no need for anything beyond instance-specific information, 
special methods are not required.

In large projects, such as shooting games, different types of guns might be used. 
Although they all have same properties like shooting range, hit detection area, 
and magazine capacity, the calculation methods for these properties vary, 
requiring different subclasses to apply specific methods. 
Additionally, certain operators may need to be overloaded, 
requiring the implementation of special methods.

-----------------------------------------------------------------------------------
## Function Introduction

# main.py

By calling generator.py, text and users are generated, and the user is prompted to log in. 
Upon successful login, the main interface is displayed.

In the init() function, 
You can adjust the parameters of "generator.generate_texts(number of texts, wordcount of texts)"
to control the amount and word count of generated text. 
You can also modify the parameters of "generator.generate_users(number of users)" 
to control the number of generated users.

# service/main_service

Classify operations.

# service/service_{1,2,3,4,5}.py

Corresponding to five different operation modes.
1. Display the text list and content
2. Purchase VIP
3. Show annual or monthly reading statistics,
including the longest reading time, highest word count, total reading time, and total word count.
4. Display the bestseller list, showing the book title and number of views.
5. VIP users can compare browsing history with other users.

# text_generator/markov.py

The code is sourced from Ed Lesson and uses Markov chains to generate text and titles.

# tools/generator.py

Using the generate_text() function, generate a certain amount of text and store the text 
information in the "info.in" file. These files are in "texts_database"
text information format: <index>,<text name>,<author>,<wordcount>,<vip>

Using the generate_users() function, generate usernames, passwords, VIP status, 
and reading history. These files are in "user_info".
user reading history format: 
<index>,<text name>,<author>,<wordcount>,<vip>,<duration(HH:MM:SS)>,<date(DD-MM-YYYY)>

# tools/permission.py

All operations that require permission verification.

# tools/password.py

Welcome user and verify password

# tools/text.py

The *Text* class and *User* class are used to simplify code related to 
reading text information and user history.

# tools/other.py

Other frequently called functions.

-----------------------------------------------------------------------------------
## Refenences

In home/text_generator, 
    the document "Romeo and Juliet.txt" is sourced from 
    the "www.gutenberg.org", provided by the Project Gutenberg.

    the "markov.py" is a example program
    from https://edstem.org/au/courses/18651/lessons/63631/slides/435530,
    and it is not my work.

In other program which has acknowledgement,
    Code is sourced from my previous work("Assignment B and C")
    https://edstem.org/au/courses/18651/lessons/61238/slides/414788
    https://edstem.org/au/courses/18651/lessons/62244/slides/421025
