# DiscordPingChecker
Checks for discord ping and texts you
## About
I made this because I don't have a smart phone and rely on discord as a part of my job. So using a "self bot" this program will check to see if you, your roles, or everyone is mentioned on discord and send you a text using the twilio API
## Running
```
./init.sh
```
This script will ask you for your discord token and  twilio info as well as your send to phone number and recv from phone number and write it to a file
```
./main.py
```
This will run the program and it will now start texting you.
