'''
Akshay Gupta
Groupme Chat Bot
'''

import requests as req
import time

reqParams = {"token": "1J8fEUW8xUVS0WnnA2GydGec0Pc9LR9aqELmT8rx"}

lastID = -1

cmds = dict()
cmds["help"] = "All Commands Must Start With /"
cmds["info"] = "Groupme Bot Made By Akshay Gupta"
cmds["website"] = "akshay.us"

while True:
	msgs = req.get("https://api.groupme.com/v3/groups/42706729/messages", 
		params = reqParams).json()['response']['messages']
	#newest --> oldest

	for msg in msgs:
		if msg['id'] == lastID: 
			#stops iterating through when it hits the last read message
			break

		msgTxt = msg["text"]
		if msgTxt.startswith("/"): #if user is giving a command
			command = msgTxt[1:]

			for key, value in cmds.items(): #iterates through all commands
				cmdLength = len(key) 
				if command[:cmdLength] == key: 
					#if the user command is that command executes that
					postParams = { 'bot_id' : 'ecc70db33eeba1f990cc870839', 
						'text': value }

					req.post('https://api.groupme.com/v3/bots/post', 
							params = postParams)

	lastID = msgs[0]["id"] #saves the id of the newest message that was read
	time.sleep(2.5)

