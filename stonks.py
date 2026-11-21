import random
from bank import Bank
# ok so i literally forgot to read filenames, so main now has all the main
# and stonks has the STONKS (dead meme im so sorry)
# NOTE: CAN SPEND 5.5 HOURS ON ART

class StockMarket():
    def __init__(self):
        # stocks in this format
        # name : name, median_price : price, volatility (check spell) : 0.35 (percentage of possible change)
        self.stocks = {
            "POM" : { # to my sister, who made me buy the eggplants, and is addicted to pomegranate (she wont read this prolly) (she read it after locking me out of my)
                "name" : "Pomegranate Manguese Corporation",
                "current_cost" : 10.00,
                "volatility" : 0.35,
                "shares_purchased" : 0,
                "historical_prices" : [10.00],
                "BASE" : 10.00
            }, # people hate pomegranate revolution or som
            
            "MOW" : {
                "name" : "Meowhiffic Grocers",
                "current_cost" : 15.00,
                "volatility" : .25,
                "shares_purchased" : 0,
                "historical_prices" : [15.00],
                "BASE" : 15.00
            }, # insane scandal where the chefs are rats

            "BAW" : {
                "name" : "Bawling Companee", # french e at the end for francy (HAHA INSANE PUN)
                "current_cost" : 400.00,
                "volatility" : .15,
                "shares_purchased" : 0,
                "historical_prices" : [400.00],
                "BASE" : 400.00
            },

            "AVO" : {
                "name" : "Avo-onics Softwhere",
                "current_cost" : 5000.00,
                "volatility" : .20,
                "shares_purchased" : 0,
                "historical_prices" : [5000.00],
                "BASE" : 5000.00
            } # super chill, until news event of child labor or som
        }

        self.headlines = {
            "POM" : [
                ["JUST IN: Pomegranate Revolution breaks out within the nation. POM drops 35%.", 0.65]
                    ],
            "MOW" : [
                ["BREAKING: Meowhiffic internal report reveals the chefs are rats. MOW crashes 40%.", 0.60]
                    ],
            "BAW" : [
                ["EXCLUSIVE: Bawling Companee revealed MASSIVE quarterly growths! BAW up 75%.", 1.75]
            ],
            "AVO" : [
                ["MAJOR SCANDAL: Avo-onics Softwhere engineers photographed coding in LIGHT MODE. AVO drops 65%.", 0.35]
            ]
        }

    def tick_prices(self):
        # manually ticking prices is NOT fun, but well see how it works
        for tickname in self.stocks: # insane throwback to items.items
            stock = self.stocks[tickname]
            LIMIT = int(stock['volatility'] * 100) # this will be a PERCENT, also insane verity
            change_boundaries = (random.randint(-LIMIT + 20, LIMIT - 5) / 100) # to get back to percent
            # noticed a general downward trend, we usually want stocks to grow and not just go into a downward spiral, so i added a small boost to general cost
            # ok so that made everythhing go nuts. instead, it gets boost of 20 only to negative
            # comment bc i found this weird to code
            # we first get LIMIT to be an INTEGER percent (30percent) ex
            # then we choose a random integer between (-30, 30) to decide if it goes UP or DOWN, divide by 100 to get the DECIMAL to mult
            current_price = self.stocks[tickname]['historical_prices'][-1] # insane rare negative index referenced
            new_price = current_price * (1 + change_boundaries)
            if new_price >= self.stocks[tickname]["BASE"] * 2:
                spike = new_price
                while new_price >= self.stocks[tickname]["BASE"]:
                    demote = random.randint(1,100) / 100
                    new_price *= demote

            if new_price <= 0:
                new_price = 1
                new_price = f"{new_price:.2f}"
            self.stocks[tickname]['historical_prices'].append(new_price)
            self.stocks[tickname]['current_cost'] = new_price

            # i feel like im insane, this should be working???

    def buy_stock(self, tickname, amount, bank): # either amount will be for buying in bulk, or it can just be buying one at a time to promote spam clicking
        # use investment acc, checking is gonna be for gambling and expenses, saving might just be non existent or to achievements
        if tickname in self.stocks and amount >= 1:
            current_price = self.stocks[tickname]['historical_prices'][-1] # ts hurts my hqnds
            cost = amount * current_price
            cost = f"{cost:.2f}"
            cost = float(cost)
            if bank.withdraw(cost, "Investment") == True:
                self.stocks[tickname]["shares_purchased"] += amount
                print(f"You purchased {amount} {tickname} for {cost}!")
                return True
        if tickname not in self.stocks:
            print(f"You cannot buy {tickname}, as it doesn't exist.") # changed this message bc it is NOT descriptive
    
    def sell_stock(self, tickname, amount, bank): # forgot word for sell, was gonna put "steal" or "stop" or "relinquish", ts bad
        if tickname in self.stocks and amount >= 1:
            if self.stocks[tickname]['shares_purchased'] >= amount:
                earnings = self.stocks[tickname]['historical_prices'][-1] * amount
                self.stocks[tickname]['shares_purchased'] -= amount
                bank.deposit(earnings, "Investment")
                print(f"You sold {amount} {tickname}, for a total of {earnings}!")
        return False

    def news_event(self):
        tickers = ["POM", "MOW", "BAW", "AVO"]
        tickname = tickers[random.randint(0, (len(tickers) - 1))]
        events = self.headlines[tickname]
        chosen = events[random.randint(0, (len(events) - 1))]
        return chosen # idk if we return or not