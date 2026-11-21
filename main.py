import random
import os
import time
from bank import Bank
from stonks import StockMarket

bank = Bank()
stonk = StockMarket()

while True:
    try: # well my mother is mad at me for no reason so now i feel like crap
        choice = int(input("""
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
| Option | Type in the number of the option you pick! |  
|   1    | Check current account balance              |
|   2    | Check current stock prices                 |
|   3    | Purchase shares of a stock                 |
|   4    | Sell shares of a stock                     |
|   5    | Take a break (forward time)                |
|   6    | Visit the local, RNG probability location  |
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
        """))
        if choice == 1:
            time.sleep(0.1)
            print(f"Your investment account has {bank.check_balance("Investment")} dollars!")
            print(f"Your savings account has  {bank.check_balance("Savings")} dollars!")
            print(f"Your checking account has {bank.check_balance("Checking")} dollars!")
            garb = input("Press ENTER when ready to continue... ")

        elif choice == 2:
            print("- - - - - - - - - - - - - - - - - - -")
            for ticker in stonk.stocks:
                stock = stonk.stocks[ticker]
                print(ticker, stock['name'])
                print(f"{stock['current_cost']:.2f}")
            print("\n- - - - - - - - - - - - - - - - - - -")

            garb = input("Press ENTER when ready to continue...")
            
        elif choice == 3:
            # this is gonna just be a block that NEEDS to be run whenever buying stocks
            print("- - - - - - - - - - - - - - -")
            for ticker in stonk.stocks:
                print(ticker + ", ", end="") # i dont like how the last ticker also has a commo, but this is probably just something that must be dealt with
            print("\n")
            print("- - - - - - - - - - - - - - -")
            purchase = input("Which stock would you like to buy? ").strip().upper()
            amount_purchase = int(input(f"And how many shares of {purchase} are you purchasing? (1, 2, 3, etc) "))
            stonk.buy_stock(purchase, amount_purchase, bank)

        elif choice == 4: # i am hoping sm that theres no bugs for this part bc i dont wanna have to go bug hunting for 90 mins AGAIN
            print("- - - - - - - - - - - - - - -")
            for ticker in stonk.stocks:
                print(f"{ticker}: {stonk.stocks[ticker]['shares_purchased']} shares purchased")
            print("\n")
            print("- - - - - - - - - - - - - - -")
            selling = input("Which stock would you like to sell? (POM, AVO, etc) ").strip().upper()
            amount = int(input("And how many shares? "))
            stonk.sell_stock(selling, amount, bank)

        elif choice == 5:
            stonk.tick_prices()
            print("THE PRICES ARE CHANGING")
            for ticker in stonk.stocks:
                print(ticker, f"{stonk.stocks[ticker]['current_cost']:.2f}")
    except Error as e:
        pass

# NOTE NOTE NOTE NOTE
# THERE IS A BIG BIG BUG 
# WHEN BUY/SELL STOCKS, MONEY IS DUPLICATED