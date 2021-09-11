#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time, json
from time import sleep
import FTX_Class
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
check_coin = config['coinmover']['check_coin']
source_sub = config['coinmover']['source_sub']
dest_sub = config['coinmover']['dest_sub']
sleeptime = config['coinmover']['sleeptime']
maxmargin = config['coinmover']['maxmargin']

c = FTX_Class.FtxClient(api_key=, api_secret=,subaccount_name=source_sub)

check = c.get_wallet()
print("Balance of degen :")
print(check[0]['coin'], ' ', check[0]['total'])

for x in check:
	print(x['coin'], ' ', x['total'], ' ', x['free'])
	
#all_wallet = c.get_allwallet()
#print(all_wallet['main'][1]['coin'])
#print(all_wallet['main'])

#for id,coin in all_wallet.items():
#	print("wallet")
#	for coins in coin:
#		print(coins) 
