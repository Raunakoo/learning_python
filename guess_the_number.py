import math
import random

# Generating a random number to guess
number_to_guess = 1
number_to_guess = random.randint(0, 100)
int_number_to_guess = int(number_to_guess)
print("Random Number", number_to_guess)


user_input = 0

# user will in put a number


def number_guessed():
    user_input = int(
        input("Guess a number from 0 to 100(0 and 100 are included : "))
    #make sure to return user_input
    return user_input


Answer = False


# I have to do everything in the loop so something can repeat when user guesses it wrong
while Answer == False:
    user_input = number_guessed()
    if user_input > int_number_to_guess:
        print("checking if number is high or low")
        print("Your number is too high")

    elif user_input < int_number_to_guess:
        print("checking if number is high or low")
        print("your number is too low")

    elif user_input == int_number_to_guess:
        print("You guessed the right number!")
        Answer = True
        exit()
