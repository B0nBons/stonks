# since mostly everything from bank and stonks work
# im now going to work on some fun lil NOT gambling games
# these ARENT gambling, theyre lucked based rng simulators >:D
import random
import time

class Casino():
    def __init__(self):
        pass
        # lowkey i think this is just gonna be a big class thats filled with the activities

    def jackblack(self): # this is to be implemnted later, perhaps at a later point, it will simply be too much for my brainpower right now
        # dealer draws to 16, stands on 17
        # shows one, hides the other card
        cards = {
            "KING" : 4,
            "QUEEN" : 4,
            "JACK" : 4,
            "TEN" : 4,
            "NINE" : 4,
            "EIGHT" : 4,
            "SEVEN" : 4,
            "SIX" : 4,
            "FIVE" : 4,
            "FOUR" : 4,
            "THREE" : 4,
            "TWO" : 4,
            "ONE" : 4
        }
        # i dont think suite/colour matters???
        # side note: it would be cool to have little pictures of the cards

        player_hand = []
        dealer_hand = []
        game_on = True
        winner = None

        while game_on == True:
            pass
        # no way in hell am i gonna be able to finish this lol
        # no jack black ;(

    def roulette(self):
        pass
        # i dont actually know how roulette works
        # that is why it is being paused

    def higher_lower(self, bank):
        # this one is easy so im starting with it lol
        account = "Investment" # hardcoding this in because i havent actually added money transfers and stuff to bank yet, which is obv kinda important, but not game breaking
        try:
            bet = int(input("How much are you willing to bet? "))
        except ValueError:
            print("That isn't a number!")
            return False

        if bank.withdraw(bet, account):
            pass
        else:
            return False # not enough money i believe

        known = random.randint(1, 100)
        mult = 1.0
        streak = 0
        print("""
        __________________________________________
        |              HOW TO PLAY               |
        |________________________________________|
        | > A number will be rolled, "mystery"   |
        | > A number will be rolled, "known"     |
        | > Guess if mystery is higher or lower  |
        | > More danger = higher multiplier      |
        |________________________________________|\n""")
        # the way this works is that theres a mystery number, then we have a random number that wem ust decide is higher or lower than mystery number (i learned this from super linguine gambling sim on steam, its free and love it (not paid endorsement i swear))
        while True:
            mysterious = random.randint(1, 100)
            while mysterious == known:
                mysterious = random.randint(1,100)
            print(f"The current number is {known}")
            guess = input("Will the next number be higher (H) or lower (L)? \n[ONLY TYPE H or L, THE RNG RING IS LOOKING FOR ANY WAY TO KICK PEOPLE OUT] ").strip().upper()
            if guess != "H" and guess != 'L':
                check = input("Do you really want to leave and cash out? (y/n) ").strip().lower()
                if check == "y":
                    print("...\nTHEN GET OUTTA HERE, AND BACK TO INVESTING!!!")
                    if streak == 0:
                        print("You've had your bet refunded.")
                        bank.deposit(bet, account)
                        break
                    else:
                        win = bet * mult
                        bank.deposit(win, account)
                        print(f"You've cashed out {win} dollars!")
                        break

                elif check == "n" :
                    continue
            else:
                if guess == "H":
                    if mysterious > known:
                        streak += 1
                        risk = ((random.randint((mysterious - known), 100)) / 100) + 1
                        known = random.randint(1, 100) # calc risk before known
                        mult = (streak * 0.85) * risk # this is a very bad risk val for mult calc, but idek how else to do it
                        print(f"You got it! The number was {mysterious} (multiplier of {mult})")
                        continue
                    elif mysterious < known:
                        print(f"You guessed wrong... The number was {mysterious} (multiplier of {mult} lost)")
                        known = random.randint(1, 100)
                        streak = 0
                        mult = 1
                        print(f"You lost your bet of {bet}")
                        break # we just kick them out to make logic easy

                elif guess == "L":
                    if mysterious < known:
                        streak += 1
                        risk = ((random.randint((known - mysterious), 100)) / 100) + 1
                        mult = streak * risk
                        known = random.randint(1, 100)
                        print(f"You got it! The number was {mysterious} (multiplier of {mult})")
                        continue
                    elif mysterious > known:
                        print(f"You guessed wrong... The number was {mysterious} (multiplier of {mult} lost)")
                        known = random.randint(1,100)
                        streak = 0
                        mult = 1
                        print(f"You lost your bet of {bet}")
                        break # kick out


    def slots(self):
        pass
    
    def mines(self):
        pass
        # minesweeper
    def horse(self, bank):
        horses = { # formatted as name : win_chance, multiplier, icon
            "|  Imagine Losing |" : [0.02, 1000, "I"],
            "|   Woe Is You    |" : [0.15, 6, "W"],
            "|   Hard Worker   |" : [0.25, 2, "H"],
            "|   Dragonfruit   |" : [0.21, 2.5, "D"],
            "|   Gold Finder   |" : [0.29, 1.5, "G"],
            "|  Lucky Breaker  |" : [0.08, 100, "L"]
        }
         
        print("- - - HORSE RACING - - -")
        print("|    HORSE NAME   | WIN CHANCE |  MULT")
        for name in horses:
            print(f"{name}    {horses[name][0]}    | {horses[name][1]}") # for some reason instead of horse, i wrote hormones?? bio IS getting to me ig

    def fish(self):
        pass