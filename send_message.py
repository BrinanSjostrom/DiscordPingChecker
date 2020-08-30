from twilio.rest import Client

def send_message(client, from_number, to_number, message):
	client.messages.create(
			body=message,
			from_=from_number,
			to=to_number
		)