# discordbots

## LinkedIn Connector  
The purpose of this script is to have a bot that will automatically connect users in a Discord channel on LinkedIn.  
Rather than saving everyone's usernames and passcodes in a very cryptographically unsafe manner, we've split it up into
a server-side script and a user-side script.

linkedin_bot.py runs on the server side. It currently monitors a specific channel for new users, and records each new one.  

Currently working on the following:  
* Having bot send a private message to each new user requesting their linkedin profile address (this is in the format https://www.linkedin.com/in/[name]-[identifier/)
* LinkedIn profile address stored on a database (online SQL most likely)
* Bot will then send the user the user-side python script

User-side python script will first ask the user for their LinkedIn username and password. Upon receipt, it will use selenium to
access LinkedIn, login to the page, pull every address from the online database, access each of these pages, connect with the user
if not already connected, and then logout of LinkedIn.
