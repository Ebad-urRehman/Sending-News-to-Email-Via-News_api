# About Project
This is an news api project which take 20 news from newsapi website about a paticular topic and send them to email provided
# Main File
First we have to store news api key in environment variables (watch from internet)

now os.getenv("KEY") is syntax for getting api key or any password from environment variables


In main file os library is imported and used to get the API key from environment variables of our system

Then we import request library. 

requests() method it imports news from the url provided of news api 
about specific topic (python in this case)

after importing the response variable type is now ('requests.models.Response)

we have to convert it into json for more readable format
content = response.json()

! first print out the format to see whats going on in file we convert to jason print(content)


[{'source': {'id': None, 'name': 'Stackoverflow.com'}, 'author': 'Stack Overflow', 'title': 'i am getting following error when i tried to create a django project ? i am using python 3.11 with pip 23.2.1 ? Any help is appreciated', 'description': 'i am trying to create a django project but i am not able to create it.\n$ django-admin startproject web\nFatal 

file name is content and we need only title, desciption and url key to send it as email to user

so we get them by syntax

content["title"] it gives first news title for first time and so on

thus we write it in for loop

from [0:20] means 0 to 19 so 20 news are stored in body variable with that message at first  

f"Subject: Today's News from NewsAPI\n" \
            f"from NewsAPI\n" \
            f"Topic {topic}\

message = body.encode('utf8')
converting into utf8 format

calling the send email function

# Send Email Function

in send email function 
port = 465 which is gmail port it remains same in your code
host = "smtp.gmail.com" host is also that for gmail

password is also stored and get by virtual environment variables
Note : use application password for security
sender email is the email which password is stored in it
reciever email where u want to send emails


the below syntax is used to send emails via SMPT servers

# Creating Image File
this file is not a part of project and its syntax of coping image and creating new image using python