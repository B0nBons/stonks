import random
import os
import time
from bank import Bank
from stonks import StockMarket

bank = Bank()
stonk = StockMarket()

while True:
    choice = int(input("1 to check balance, 2 to view stocks, 3 to buy stocks, 4 to sell stocks, 5 progress time, and 6 to quit "))
    if choice == 1:
        bank.check_balance("Investment")
        bank.check_balance("Savings")
        bank.check_balance("Checking")

    elif choice == 2:
        for ticker in stonk.stocks:
            stock = stonk.stocks[ticker]
            print(ticker, stock['name'])
            print(stock['historical_prices'][-1])
    elif choice == 3:
        # chat im cooked
        # i had to skip school bc i got a fever
        # its the last day before thanksgiving break
        # and i have a french quiz, math TEST, and politics paper
        # js put the fries in the bag
        # this is gonna just be a block that NEEDS to be run whenever buying stocks
        for ticker in stonk.stocks:
            print(ticker + ", ", end="") # i dont like how the last ticker also has a commo, but this is probably just something that must be dealt with
        print("\n")
        purchase = input("Which stock would you like to buy? ").strip().upper()
        amount_purchase = int(input(f"And how many shares of {purchase} are you purchasing? (1, 2, 3, etc) "))
        stonk.buy_stock(purchase, amount_purchase, bank)

    elif choice == 5:
        stonk.tick_prices()
        print("THE PRICES ARE CHANGING")
        for ticker in stonk.stocks:
            print(ticker, f"{stonk.stocks[ticker]['current_cost']:.2f}")
    # guys i just realised why it wasnt working
    # i feel so dumb
    # i made the choice 5 and then kept typing in 5 and being mad why it wasnt working when it was literally me
    # this is VERY embarassing