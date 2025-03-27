#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 27, 2025
"""
This program creates a guessing game with a number range of 0-9.
It uses exception handling with a try-catch statement to
prevent erroneous user input from crashing the program.
"""

# Import the random module for random number generators.
import random


# Define the main function.
def main():
    # Generate an integer between 0 and 9 and store it as the correct number.
    correct_num = random.randint(0, 9)
    # Ask for the user to enter an integer between 0 and 9.
    chosen_num_str = input("Enter an integer between 0 and 9.\n")

    # Try to check the validity of the user's input.
    try:
        # Convert the user's input as a string into an integer.
        chosen_num_int = int(chosen_num_str)

        # Checks if the chosen integer is equal to the correct number.
        if chosen_num_int == correct_num:
            # Display that the user guessed correctly.
            print("You guessed correctly!")
        # Otherwise, the user did not guess correctly.
        else:
            # Display that the user guessed incorrectly, showing the correct answer.
            print(f"You guessed incorrectly! The correct answer was {correct_num}.")

    # Run if int() could not convert the user's input value to an integer.
    except ValueError:
        # Display that the user did not enter a valid integer.
        print(f"{chosen_num_str} is not an integer.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
