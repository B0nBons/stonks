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
            "money" : 1000.00
        }}
        # for now, I think im only going to implement investment
        # ok im actually crying guys, i made a ton of bugs bc the goofy ahh defauly light mode was too hard for my eyes to see
    
    def deposit(self, amount_money, account_name): # I LITERALLY FORGOT WHAT IT WAS CALLED WHEN YOU PUT IN MONEY
        if account_name in self.accounts:
                if amount_money > 0:
                    self.accounts[account_name]["money"] += amount_money
                    print(f"You deposited {amount_money} in your {account_name} account.")
                    # i think we dont use print statements since we want this to be in pygame???????? idk NO, WE HATE PYGAME, FAH
                else:
                    print("You aren't able to deposit negative money.")
        else:
            print("That account isn't real.")
            dream = random.randint(1, 100)
            if dream >= 90:
                print("And it never will be.")

# after that bug, im now going through EVERYTHING bc im a dumbahs

    # NOTE NOTE NOTE REDO THIS ENTIRE FUNC IT LOWKEY SUCSK
    def withdraw(self, amount_money, account_name):
        if account_name in self.accounts: # im adding this because theres a decent chance im gonna have the user type it in rather than just typing a number or something
            if amount_money > self.accounts[account_name]["money"]:
                print(f"You do not have enough money in {account_name} to withdraw {amount_money} dollars.") # you dont even have enough money lol
                for account in self.accounts:
                    print(account)
                    if self.accounts[account]['money'] >= amount_money:
                        print(f"The {account} account has {self.accounts[account]['money']} dollars, which is enough for your transaction of {amount_money}")
                        print("Try withdrawing some money from that account, and depositing it into your INVESTMENT account.")
                return False

            if amount_money <= 0:
                print("You can't withdraw negative money.")
                return False
            
            self.accounts[account_name]["money"] -= amount_money
            self.accounts["Checking"]["money"] += amount_money # OMFG WhAT IF WE WITHDRAW FROM OUR CHECKING ACCOUNT
            print(f"You withdrew {amount_money} dollars. It is now in your checking account.")
            return True
        else:
            print("That account isn't real.")
            false = random.randint(1,100)
            if false <= 5:
                print("Or is it?")
                print("It's not. I checked.")
            return False
        # i just realised that this money kinda just disappears, so its just going to the checking
        # ok so after realising, i realised that the money system kinda sucks arse
    
    def check_balance(self, account_name):
        if account_name in self.accounts:
            print(f"You have {self.accounts[account_name]['money']} dollars in your {account_name}")

    # func for interest since i want specific events to trigger interest (end of day, major news, new acc waiting period)
    def add_interest(self): # this is not very INTERESTing haha that was so bad
        self.accounts["Savings"]["money"] = self.accounts["Savings"]["money"] * (1 + self.accounts["Savings"]["interest"])
        # ALWAYS KEEP INTEREST BELOW 1 TOTAL OR ELSE THE PLAYER WILL BE RICH NOTE NOTE NOTE

bank = Bank()