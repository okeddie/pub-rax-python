"""

This program sets a number and a user must guess it.
"""

from random import randint

# Generate the random number
generated_num = randint(1,101)

# assuming 1 attempt to start with.
attempts = 1

while True:
    # set input
    user_guess = input("Enter your guess: ")
    # test if user guessed the correct number.
    if int(user_guess) == generated_num:
        break
    # test if the user guessed too high.
    if int(user_guess) > generated_num:
        print("Your guess is too high")
    # test if the user guessed too low.
    if int(user_guess) < generated_num:
        print("Your guess is too low")
    # auto increment attempts.
    attempts += 1

# return feedback when guessed correct.
print("Your guess is correct!")
print("You succeeded in {0:d}".format(attempts),"attempts")
