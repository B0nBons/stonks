import random
import os
import time
from bank import Bank
from stonks import StockMarket

bank = Bank()
stonk = StockMarket()

while True:
    choice = int(input("1 to check balance, 2 to view stocks, 3 to buy stocks, 4 to sell stocks, 5 to quit"))
    if choice == 1:
        bank.check_balance("Investment")
        bank.check_balance("Savings")
        bank.check_balance("Checking")

    elif choice == 2:
        for ticker in stonk.stocks:
            stock = stonk.stocks[ticker]
            print(ticker, stock['name'])
            print(stock['historical_prices'][-1])
        
