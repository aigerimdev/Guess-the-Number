import random

RANGE_LOW = 0
RANGE_HIGH = 100

random_number = random.randint(RANGE_LOW, RANGE_HIGH)
def guess_the_number():
    user_input = get_the_number_from_user() 
    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print("Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
            print("You guessed the number! Good job!")
    elif user_input > random_number:
            print("Your guess is too high")
    elif user_input < random_number:
            print("Your guess is too low")
def get_the_number_from_user():
    attempting_valid_input = True
    user_input = None

    while attempting_valid_input:
        user_input_string = input("Guess the number: ")

        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            attempting_valid_input = False
        else:
            print("You must input a number!")
    return user_input

guess_the_number()
guess_the_number()
guess_the_number()