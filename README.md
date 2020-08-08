# Slacker
 An automatic slack pining tool which sends a message every 29 minutes, monday through friday, 9am to 5pm from yourself to yourself
 
 ## Arguments:
 ### --domain: the domain for your slack workspace
 ### --username: your slack email address
 --password: the password for your slack account (needed for logging in)
 
 ## Notes:
 ### 1. For this program to run, it requires its own terminal allowed to run all of the time in the background. My best recommendation for this application is to run it on a raspberry pie and leave it alone.
 ### 2. To maintain your online status, it will send a message from you, to you of the word 'Ping' so do not be surpised to see large amounts of ping messages.
 ### 3. Currently desinged for Chrome Browser version 84, if you have a different version of chrome, you must get the appropriate web browser driver for it.
 
 ## Setup
 ### 1. run `pip3 install -r requirements.txt` 
 ### 2. run `python slacker.py` with the approriate arguments.
 ### 3. Sit Back and Enjoy
