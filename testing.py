import telepot
import urllib.request
import json

BOTNAME = 'NewTestBot'
BOTTOKEN = '##########################################'
SERVER = 'https://api.telegram.org/bot'+BOTTOKEN+'/'
objUpdate = ''

print('Hello World!')
with urllib.request.urlopen(SERVER+'getUpdates') as response:
	update = json.loads(response.read())
	if update['ok'] is True:
		objUpdate = update['result']

	for needResp in objUpdate:
		if 'message' in needResp:
			print(needResp['message']['text'])




print(objUpdate)
