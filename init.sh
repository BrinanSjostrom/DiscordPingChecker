#!/bin/bash
read -p "What is your discord account token: " DISCORD_TOKEN
read -p "What is you twilio account SID: " TWILIO_SID
read -p "What is your twilio auth token: " TWILIO_TOKEN
read -p "What is your twilio from number(+XXXXXXXXXXX): " FROM_NUMBER
read -p "What is your twilio to number(+XXXXXXXXXXX): " TO_NUMBER

echo $DISCORD_TOKEN > discord_token.dat
echo $TWILIO_SID > twilio_info.dat
echo $TWILIO_TOKEN >> twilio_info.dat
echo $FROM_NUMBER >> twilio_info.dat
echo $TO_NUMBER >> twilio_info.dat
