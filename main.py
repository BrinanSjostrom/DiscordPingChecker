#!/usr/bin/python3
import discord
from print_m import print_m
from twilio.rest import Client as twilioClient
from time import sleep
twilioSID = "ACefd549321460e892adf13c8ac66d2bd1"
twilioToken = "bfa5203d9fbf908cca2e06efe56a3676"
client = discord.Client()
twilio_client = twilioClient(twilioSID, twilioToken)
from_number = "+12016769899"
to_number = "+15415705009"
#to_number = "+15419082150"

@client.event
async def on_message(message):
	update = "Server: " + str(message.guild) + "\n"
	update += "Author: " + str(message.author)+ "\n"
	update += "Message: " + str(message.content) + "\n"
	update += "Mentions: " + str(message.mentions) + "\n"
	update += "Role Mentions: " + str(message.role_mentions) + "\n"
	#print_m(update)
	#if(message.author == client.user):
	#	return
	if(message.mention_everyone):
		page = f"Ping: Everyone\n{message.author} ({message.guild}):\n{message.content}"
		print_m(page)
		twilio_client.messages.create(
			body=page,
			from_=from_number,
			to=to_number
		)
	elif(message.mentions != []):
		for mention in message.mentions:
			if(str(mention) == str(client.user)):
				page = f"Ping: By name\n{message.author} ({message.guild}):\n{message.content}"
				print_m(page)
				twilio_client.messages.create(
					body=page,
					from_=from_number,
					to=to_number
				)

	if(message.role_mentions != []):
		page = "Ping: By Role: "
		if_mentioned = 0
		for role in message.guild.me.roles:
			for role0 in message.role_mentions:
				if(role == role0):
					if_mentioned = 1
					page += "%s " % (str(role))
		if(if_mentioned):
			page += f"\n{message.author} ({message.guild}):\n{message.content}"
			print_m(page)
			twilio_client.messages.create(
				body=page,
				from_=from_number,
				to=to_number
			)



def main():
	token = "NjYzNTA4NjE4NzkxODc4NjU2.X0sGvA.ttzqahAo2MRq5TpRhIgAlFbTaXQ"
	print_m("Init token: " + token)
	client.run(token, bot=False)
main()