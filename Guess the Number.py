# 2. Guess the Number

# The Goal: Similar to the first project, this project also uses the random module in Python. The program will first
# randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words,
# the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort
# of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive
# indication should appear. You’ll need functions to check if the user input is an actual number, to see the
# difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
# Concepts to keep in mind:

# Random function
# Variables
# Integers
# Input/Output
# Print
# While loops
# If/Else statements

# Programmer: Hugo Leça Ribeiro

import random


def verify(number_rand):
    try:
        number_player = int(input("\nTry to guess. The number is between 0 and 100: "))
    except ValueError:
        print(f'Wrong value, try again please!')
        verify(number_rand)
    if number_player == number_rand:
        print('Heyyy, congratulations! You got the number right!')
        return
    else:
        print('Ow, no! You missed the number :(')
        difference(number_player, number_rand)
        verify(number_rand)


def difference(number_player, number_rand):
    if number_player > number_rand:
        dif = number_player - number_rand
        if 10 < dif <= 25:
            print('Owww, you are far from the number. The number is lowest than this.')
        elif dif > 25:
            print('WOW, you are very far from the number. The number is lowest than this.')
        else:
            print('Hmmm, you are so close. The number is lowest than this.')
    elif number_rand > number_player:
        dif = number_rand - number_player
        if 10 < dif <= 25:
            print('Owww, you are far from the number. The number is highest than this.')
        elif dif > 25:
            print('WOW, you are very far from the number. The number is highest than this.')
        else:
            print('Hmmm, you are so close. The number is highest than this.')
    return


def generate_number():
    print('Hello, player. Try to found the number that i am thinking right now. I doubt!')
    number_rand = random.randint(0, 100)
    return number_rand


generated_number = generate_number()
verify(generated_number)
