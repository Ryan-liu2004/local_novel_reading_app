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