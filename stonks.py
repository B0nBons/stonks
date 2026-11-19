import random
from bank import Bank
# ok so i literally forgot to read filenames, so main now has all the main
# and stonks has the STONKS (dead meme im so sorry)

class StockMarket():
    def __init__(self):
        # stocks in this format
        # name : name, median_price : price, volatility (check spell) : 0.35 (percentage of possible change)
        self.stocks = {
            "POM" : { # to my sister, who made me buy the eggplants, and is addicted to pomegranate (she wont read this prolly) (she read it after locking me out of my)
                "name" : "Pomegranate Manguese Corporation",
                "median_cost" : 10.00,
                "volatility" : 1.50,
                "shares_purchased" : 0,
                "historical_prices" : [10.00]
            }, # people hate pomegranate revolution or som
            
            "MOW" : {
                "name" : "Meowhiffic Grocers",
                "median_cost" : 15.00,
                "volatility" : 1.75
                "shares_purchased" : 0,
                "Historical_prices" : [15.00]
            }, # insane scandal where the chefs are rats

            "BAW" : {
                "name" : "Bawling Companee", # french e at the end for francy (HAHA INSANE PUN)
                "median_cost" : 400.00,
                "volatility" : 5.50,
                "shares_purchased" : 0,
                "historical_prices" : [400.00] # idk ab scandal
            },

            "AVO" : {
                "name" : "Avo-onics Softwhere",
                "median_cost" : 5000.00,
                "volatility" : 1.5,
                "shares_purchased" : 0,
                "historical_prices" : [5000.00]
            } # super chill, until news event of child labor or som
        }
    def tick_prices(self):
        pass

    def buy_stock(self):
        pass
    
    def sell_stock(self): # forgot word for sell, was gonna put "steal" or "stop" or "relinquish", ts bad
        pass

    def news_event(self):
        pass