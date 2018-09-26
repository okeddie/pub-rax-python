"""

This program sets a number and a user must guess it.
"""

from random import randint

# Generate the random number
generated_num = randint(1,101)

# assuming 1 attempt to start with.
attempts = 1

while True:
    # initialize input
    user_guess = input("Enter your guess: ")
    if int(user_guess) == generated_num:
        break
    if int(user_guess) > generated_num:
        print("Your guess is too high")
    if int(user_guess) < generated_num:
        print("Your guess is too low")
    attempts += 1

print("Your guess is correct!")
print("You succeeded in {0:d}".format(attempts),"attempts")
