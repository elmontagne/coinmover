#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Created by elmontagne
### author:  elmontagne
### discord: Daisy#2718
### site:    https://github.com/elmontagne/coinmover
### Changelog:
### * 


import requests
import time, json
import time
import FTX_Class
import configparser
import os.path

config = configparser.ConfigParser()
config.read('config.ini')
check_coin = config['coinmover']['check_coin']
source_sub = config['coinmover']['source_sub']
dest_sub = config['coinmover']['dest_sub']
sleeptime = config['coinmover']['sleeptime']
maxmargin = config['coinmover']['maxmargin']
apikey = config['coinmover']['apikey']
apisecret = config['coinmover']['apisecret']
percentage_move = config['coinmover']['percentage_move']
discord_webhook = config['coinmover']['discord_webhook']

sleeptime = int(sleeptime)*60



c = FTX_Class.FtxClient(api_key=apikey, api_secret=apisecret,subaccount_name=source_sub)

while True:
	currenttime = time.localtime()
	timenow = time.strftime("%I:%M:%S %p", currenttime)
	print(timenow," Checking...")
	file_exists = os.path.isfile('status')
	if file_exists:
		with open('status', 'r') as ff:
			old_balance=ff.readline()
	else:
		f = open("status","w")
		f.write("0")	
		old_balance=0
	
	print("Old balance: ",old_balance)	

	check = c.get_wallet()
	print("Balance of degen :")
	print(check[0]['coin'], ' ', check[0]['total'])

	if float(old_balance) != 0 and check[0]['total'] > float(old_balance):
		print("we made profit!")
		print(check[0]['total'] - float(old_balance))
		profit = check[0]['total'] - float(old_balance)
		transfer = float(profit) * float(percentage_move) / 100
		print("transferring: ",check_coin,transfer," to: ", dest_sub)
		move_funds = c.move_funds(check_coin, float(transfer), dest_sub)  
		status_message = "Transferred: " + check_coin + " " + str(transfer) + " to: " + dest_sub

	else:
		print("No profit this time")
		print(check[0]['total'] - float(old_balance))
		status_message = "No profit this time"
	
	data = {
    "content" : status_message
}
	if discord_webhook != '':
			result = requests.post(discord_webhook, json = data)

	for x in check:
		print(x['coin'], ' ', x['total'], ' ', x['free'])
	
	
	with open('status', 'w') as f:
		f.write(str(check[0]['total']))
	print("Sleeping for ",sleeptime,"seconds")
	time.sleep(sleeptime)
 

