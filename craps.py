"""

This is a fancy dice app.
"""

from random import randrange

roll_count = 2
roll_7_count = 0
roll_2_count = 0
literal_rolls = 0
roll_2_percent = 0
roll_7_percent = 0
point_rolls = 0

def roll_die():
	    roll_dice1 = randrange(1,7)
	    roll_dice2 = randrange(1,7)
	    roll_total = roll_dice1 + roll_dice2
	    return roll_total

for i in range(1,roll_count,1):
        roll_total = roll_die()
        try:
            roll_total = int(roll_total)
        except ValueError:
            print("failed to set roll total count")
            break
        literal_rolls += 1
        if roll_total == 2:
            roll_2_count += 1
        if roll_total == 7:
            roll_7_count += 1
        if literal_rolls == 1:
            if roll_total == 7 or roll_total == 11:
                print("you rolled a {0:d} on your {1:d}st roll. You WIN!".format(roll_total, literal_rolls))
	        break
		if roll_total == 2 or roll_total == 3 or roll_total == 12:	        
                    print("you rolled a {0:d} on your {1:d}st roll. You LOST!".format(roll_total, literal_rolls))
                    break
        print("You've rolled a POINT number - {0:d} , you must roll again!".format(roll_total))
        point_number = int(roll_total)
        while True:
            roll_total = roll_die()
            try:
                roll_total = int(roll_total)
            except ValueError:
                    print("failed to set roll total count")
                    break
            point_rolls += 1
            if roll_total == 7:
               roll_7_count += 1
               print("you rolled a {0:d} on your POINT roll. You LOSE!".format(roll_total))
               break
            if roll_total == point_number:
               print("You rolled the POINT! You win! POINT was {0:d} and you rolled {1:d}".format(point_number, roll_total))
               break
            else:
               print("You did not roll point, rolled a {0:d} and point was {1:d} roll again.".format(roll_total, point_number))
               continue
