"""

This is a fancy dice app.
"""

from random import randrange

cash = 100.00
# Assume if user ran script, default play is Y/y.
play_again_prompt = 'y'


def roll_die():
    roll_dice1 = randrange(1,7)
    roll_dice2 = randrange(1,7)
    roll_total = roll_dice1 + roll_dice2
    return roll_total


def prompt_play():
    while True:
        play_again_prompt = raw_input("Do you wish play again? Y/y for yes, N/n for no. ")
        if play_again_prompt == "N" or play_again_prompt == "n":
            break
        if play_again_prompt == "Y" or play_again_prompt == "y":
            break
        if play_again_prompt != "N" or play_again_prompt != "n":
            print("User entered bad input.")
            continue
    return play_again_prompt


while True:
    print("Welcome to eddie's crap shoot. Here we go!!!")
    while True:
        if cash <= 0:
            break
        if cash > 0:
            print("cash balance is: ${0:,.2f}".format(cash))
            roll_total = roll_die()
        if play_again_prompt == "N" or play_again_prompt == "n":
            break
        if roll_total == 7 or roll_total == 11:
            print("you rolled a {0:d} on your 1st roll. You WIN!".format(roll_total))
            cash = cash + 10.00
            play_again_prompt = prompt_play()
            continue
        if roll_total == 2 or roll_total == 3 or roll_total == 12:
            print("you rolled a {0:d} on your 1st roll. You LOST!".format(roll_total))
            cash = cash - 10.00
            if cash > 0:
                play_again_prompt = prompt_play()
            continue
        while True:
            point_number = int(roll_total)
            print("You've rolled a POINT number - {0:d} , you must roll again!".format(roll_total))
            roll_total = roll_die()
            if roll_total == 7:
                print("you rolled a {0:d} on your POINT roll. You LOSE!".format(roll_total))
                cash = cash - 10.00
                if cash > 0:
                    play_again_prompt = prompt_play()
                break
            if roll_total == point_number:
                print("You rolled the POINT! POINT was {0:d}, you rolled {1:d}. You WIN!".format(point_number, roll_total))
                cash = cash + 10.00
                play_again_prompt = prompt_play()
                break
            else:
                print("You rolled a {0:d} and point was {1:d}, must roll again.".format(roll_total, point_number))
                continue
        if cash <= 0:
            break
        if play_again_prompt == "N" or play_again_prompt == "n":
            break
        if play_again_prompt == "y" or play_again_prompt == "Y":
            print("Rolling again!!!")
    if cash <= 0:
        print("You're out of funds. go home.")
        break
    if play_again_prompt == "N" or play_again_prompt == "n":
        print("Thanks for playing! Final cash balance is: ${0:,.2f}".format(cash))
        break
    else:
        print("Game over.")
        break
