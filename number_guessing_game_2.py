#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon/May3/2021
# This program is a Number Guessing Game


import random


def main():
    # this function checks if the number guessed is correct or wrong
    print("hey,guess the number if you can!\n")

    # input
    guessed_number = int(input("Enter the number between 0 - 9:"))
    random_number = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    if (guessed_number == random_number):
        print("You guessed correct!")
    else:
        print("You guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
