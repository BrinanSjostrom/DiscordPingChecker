def getTwilioInfo():
	twilioFile = open("twilio_info.dat", "r")
	info = []
	for line in twilioFile.readlines():
		info.append(line)
	twilioFile.close()
	return info