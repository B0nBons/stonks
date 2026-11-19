# we dont got this
# currently gonna make everything print instead of returning vals
# bc not using pygame now
# ong bro, 14 hours left, and out of them, 8 are for rent and 6 are for eggplants
# therefore, i should do 4 hours today, 

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
            print(f"You deposited {money} in your {account_name} account.")
            # i think we dont use print statements since we want this to be in pygame???????? idk NO, WE HATE PYGAME, FAH
        print("You aren't able to deposit negative money.")

    def withdraw(self, amount_money, account_name):
        if amount_money > self.accounts[account_name]["money"]:
            print(f"You do not have enough money in {account_name} to withdraw {amount_money} dollars.") # you dont even have enough money lol
        if amount_money <= 0:
            print("You can't withdraw negative money.")
        self.accounts[account_name]["money"] -= amount_money
        self.accounts["Checking"]["money"] += amount_money
        print(f"You withdrew {amount_money} dollars. It is now in your checking account.")
        # i just realised that this money kinda just disappears, so its just going to the checking
    
    def check_balance(self, account_name):
        if account_name in self.accounts:
            print(self.accounts[account_name]['money'])

    # func for interest since i want specific events to trigger interest (end of day, major news, new acc waiting period)
    def add_interest(self): # this is not very INTERESTing haha that was so bad
        self.accounts["Savings"]["money"] = self.accounts["Savings"]["money"] * (1 + self.accounts["Savings"]["interest"])
        # ALWAYS KEEP INTEREST BELOW 1 TOTAL OR ELSE THE PLAYER WILL BE RICH NOTE NOTE NOTE