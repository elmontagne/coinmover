#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time, json
from time import sleep
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

c = FTX_Class.FtxClient(api_key=apikey, api_secret=apisecret,subaccount_name=source_sub)

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
	transfer = check[0]['total'] - float(old_balance)
	print("transferring: ",transfer)
	move_funds = c.move_funds('USD', float(transfer), dest_sub)   
else:
	print("No profit this time")
	print(check[0]['total'] - float(old_balance))
	
for x in check:
	print(x['coin'], ' ', x['total'], ' ', x['free'])
	
	
with open('status', 'w') as f:
    f.write(str(check[0]['total']))

 
#all_wallet = c.get_allwallet()
#print(all_wallet['main'][1]['coin'])
#print(all_wallet['main'])

#for id,coin in all_wallet.items():
#	print("wallet")
#	for coins in coin:
#		print(coins) 
