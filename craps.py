"""

This is a fancy dice app.
"""

from random import randrange

roll_count = 1000000
roll_7_count = 0
roll_2_count = 0
literal_rolls = 0
roll_2_percent = 0
roll_7_percent = 0
point_rolls = 0
cash = 100.00
play_again_prompt = 'Y'

def roll_die():
    roll_dice1 = randrange(1,7)
    roll_dice2 = randrange(1,7)
    roll_total = roll_dice1 + roll_dice2
    return roll_total

while True:
    if literal_rolls == 0:
        print("Welcome to eddie's crap shoot. Here we go!!!")
        print("Rolling now.....")
        literal_rolls += 1
        for i in range(1,roll_count,1):
            if cash < 0:
                break
            if cash > 0:
                print("cash balance is: ${0:,.2f}".format(cash))
                roll_total = roll_die()
                if play_again_prompt == "N" or play_again_prompt == "n":
                    break
                if roll_total == 2:
                    roll_2_count += 1
                if roll_total == 7:
                    roll_7_count += 1
                if literal_rolls == 1:
                    if roll_total == 7 or roll_total == 11:
                        print("you rolled a {0:d} on your {1:d}st roll. You WIN!".format(roll_total, literal_rolls))
                        cash = cash + 10.00
                        play_again_prompt = raw_input("Do you wish play? Y/y for yes, N/n for no. ")
                        while True:
                            play_again_prompt = raw_input("Do you wish play? Y/y for yes, N/n for no. ")
                            if play_again_prompt == "y" or play_again_prompt == "Y":
                                break
                            if play_again_prompt == "N" or play_again_prompt == "n":
                                break
                            else:
                                continue
        	        continue
                    if roll_total == 2 or roll_total == 3 or roll_total == 12:	        
                        print("you rolled a {0:d} on your {1:d}st roll. You LOST!".format(roll_total, literal_rolls))
                        cash = cash - 10.00
                        play_again_prompt = raw_input("Do you wish play? Y/y for yes, N/n for no. ")
                        while True:
                            play_again_prompt = raw_input("Do you wish play? Y/y for yes, N/n for no. ")
                            if play_again_prompt == "y" or play_again_prompt == "Y":
                                break
                            if play_again_prompt == "N" or play_again_prompt == "n":
                                break
                            else:
                                continue
                        continue
                print("You've rolled a POINT number - {0:d} , you must roll again!".format(roll_total))
                point_number = int(roll_total)
                while True:
                    roll_total = roll_die()
                    point_rolls += 1
                    if roll_total == 7:
                       roll_7_count += 1
                       print("you rolled a {0:d} on your POINT roll. You LOSE!".format(roll_total))
                       cash = cash - 10.00
                       break
                    if roll_total == point_number:
                       print("You rolled the POINT! You win! POINT was {0:d} and you rolled {1:d}".format(point_number, roll_total))
                       cash = cash + 10.00
                       break
                    else:
                       print("You rolled a {0:d} and point was {1:d}, must roll again.".format(roll_total, point_number))
                       continue
            if cash < 0:
                break
            while True:
                play_again_prompt = raw_input("Do you wish play? Y/y for yes, N/n for no. ")
                if play_again_prompt == "y" or play_again_prompt == "Y":
                    break
                if play_again_prompt == "N" or play_again_prompt == "n":
                    break
                else:
                    continue
        if cash < 0:
            print("You out of cash. go home.")
            break
        if play_again_prompt == "N" or play_again_prompt == "n":
            break
        if play_again_prompt == "y" or play_again_prompt == "Y":
            print("Rolling again!!!")
            continue
        else:
             break
    if cash < 0:
        break
    if play_again_prompt == "N" or play_again_prompt == "n":
        print("thanks for playing. Final cash balance is: ${0:,.2f}".format(cash))
        print("You played a total of {0:d} games".format(literal_rolls))
        break
    else:
        print("Game over.")
        break
