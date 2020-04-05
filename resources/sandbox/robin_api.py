#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:19:59 2020

@author: chengyu

simple test for robinhood connection 

API documentation
http://www.robin-stocks.com/en/latest/functions.html#logging-in-and-out
"""

import robin_stocks as r
from cred_util import load_cred


real_buy_cell = False


#%%
########## info require login #############
cred = load_cred('../../credential/ini.json')
login = r.login(cred['robinhood']['username'],cred['robinhood']['password'])

## get all you current position
positions_data = r.get_current_positions()

## simple function to get all holdings
my_stocks = r.build_holdings()

# get some user profile data 
profile_info = r.profiles.load_account_profile()
print(profile_info['crypto_buying_power'])

## load portfolio info
portfolio = r.profiles.load_portfolio_profile()
print(portfolio['last_core_portfolio_equity'])

##get stock information 
stock = r.stocks.find_instrument_data('tesla')
stock_sym = stock[0]['symbol']
print('Symbol:{} \nName:{}\n'.format(stock[0]['symbol'],stock[0]['simple_name']))

## get last price
stock_price=r.stocks.get_latest_price([stock_sym,'AAPL'])
print(stock_price)

## placing and canceling orders
all_orders = r.orders.get_all_crypto_orders()
if real_buy_cell:
    cancel_info = r.orders.cancel_all_crypto_orders()

## buy ans cess crypto
if real_buy_cell:
    order_info = r.orders.order_buy_crypto_limit('ETH',quantity=0.01,price=142.0)
    print(order_info)
