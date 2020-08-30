#!/usr/bin/python3
import discord
from print_m import print_m
from twilio.rest import Client as twilioClient
from getTwilioInfo import *
from send_message import *

client = discord.Client()

twilioInfo = getTwilioInfo()
twilioSID = twilioInfo[0]
twilioToken = twilioInfo[1]
from_number = twilioInfo[2]
to_number = twilioInfo[3]
twilio_client = twilioClient(twilioSID, twilioToken)


@client.event
async def on_message(message):
	update = "Server: " + str(message.guild) + "\n"
	update += "Channel: " + str(message.channel) + "\n"
	update += "Author: " + str(message.author)+ "\n"
	update += "Message: " + str(message.content)# + "\n"
	#update += "Mentions: " + str(message.mentions) + "\n"
	#update += "Role Mentions: " + str(message.role_mentions) + "\n"
	#print_m(update)
	#if(message.author == client.user):
	#	return

	if(message.mention_everyone):
		page = f"Ping: @everyone\n" + update
		send_message(twilio_client, from_number, to_number, print_m(page))
	elif(message.mentions != []):
		for mention in message.mentions:
			if(str(mention) == str(client.user)):
				page = f"Ping: By name\n" + update
				send_message(twilio_client, from_number, to_number, print_m(page))

	if(message.role_mentions != []):
		page = "Ping: "
		if_mentioned = 0
		for role in message.guild.me.roles:
			for role0 in message.role_mentions:
				if(role == role0):
					if_mentioned = 1
					page += "@%s " % (str(role))
		if(if_mentioned):
			page += f"\n" + update
			send_message(twilio_client, from_number, to_number, print_m(page))



def main():
	discordFile = open("discord_token.dat", "r")
	token = discordFile.read()
	discordFile.close()
	print_m("Init token: " + token)
	client.run(token, bot=False)
main()