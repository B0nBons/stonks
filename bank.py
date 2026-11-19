# wohoo we got this

class Bank():
    def __init__(self):
        # no init money bc we can just call method to do that
        self.accounts = {
        "Savings" : {
            "interest" : 0.03, # 3 percent seems pretty ok to me
            "money" : 0.00}, # dollars. INSANE fumble right here
        "Investment" : {
            "money" : 0.00}, 
        "Checking" : {
            "money" : 0.00
        }}
        # for now, I think im only going to implement investment
        # ok im actually crying guys, i made a ton of bugs bc the goofy ahh defauly light mode was too hard for my eyes to see
    
    def deposit(self, amount_money, account_name): # I LITERALLY FORGOT WHAT IT WAS CALLED WHEN YOU PUT IN MONEY
        if amount_money > 0:
            self.accounts[account_name]["money"] += amount_money
            return True
            # i think we dont use print statements since we want this to be in pygame???????? idk
        return False # if you deposit -2178 or wtv the overflow is, dont give infinite money

    def withdraw(self, amount_money, account_name):
        if amount_money > self.accounts[account_name]["money"]:
            return False # you dont even have enough money lol
        if amount_money <= 0:
            return False
        self.accounts[account_name]["money"] -= amount_money
        return True
    
    def check_balance(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name]['money']

    # func for interest since i want specific events to trigger interest (end of day, major news, new acc waiting period)
    def add_interest(self): # this is not very INTERESTing haha that was so bad
        self.accounts["Savings"]["money"] = self.accounts["Savings"]["money"] * (1 + self.accounts["Savings"]["interest"])
        # ALWAYS KEEP INTEREST BELOW 1 TOTAL OR ELSE THE PLAYER WILL BE RICH NOTE NOTE NOTE