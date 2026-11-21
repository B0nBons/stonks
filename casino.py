# since mostly everything from bank and stonks work
# im now going to work on some fun lil NOT gambling games
# these ARENT gambling, theyre lucked based rng simulators >:D
import random

class Casino():
    def __init__(self):
        pass
        # lowkey i think this is just gonna be a big class thats filled with the activities

    def jackblack(self):
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
            bet = int(input("How much are you willing to bet?"))
        except ValueError:
            print("That isn't a number!")
            return False

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
                print("Well then! You may leave, with no reward.")
                break
            else:
                if guess == "H":
                    if mysterious > known:
                        print(f"You got it! The number was {mysterious}")
                        known = random.randint(1, 100)
                        streak += 1
                        risk = ((random.randint((mysterious - known), 100)) / 100) + 1
                        mult = (streak * 0.85) * risk # this is a very bad risk val for mult calc, but idek how else to do it
                        continue
                    elif mysterious < known:
                        print(f"You guessed wrong... The number was {mysterious}")
                        known = random.randint(1, 100)
                        streak = 0
                        mult = 1
                        print(f"You lost your bet of {bet}")

                elif guess == "L":
                    if mysterious < known:
                        print(f"You got it! The number was {mysterious}")
                        knoqn = random.randint(1, 100)
                        streak += 1
                        risk = ((random.randint((known - mysterious), 100)) / 100) + 1
                        mult = streak * risk
                        continue
                    elif mysterious > known:
                        print(f"You guessed wrong... The number was {mysterious}")
                        known = random.randint(1,100)
                        streak = 0
                        mult = 1
                        print(f"You lost your bet of {bet}")
                        break


    def slots(self):
        pass
    
    def mines(self):
        pass
        # minesweeper
    def horse(self):
        pass # 
        # horse rng game

    def fish(self):
        pass