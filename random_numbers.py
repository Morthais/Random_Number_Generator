"""
This random number generator demonstrates the following:
Variables, Expressions, Conditionals, Loops, Functions, Classes, Arrays,
and reading/writing from a file.
"""

# import the random python module to help generate random numbers
import random

class Game():
    """
    This class contains all the functions for the program.
    """
    def number_generator():
        """
        Generate a random length between 0 and 30,
        Generate random numbers until length is reached,
        Append each number to the end of the array,
        Return the array of random numbers.
        """
        random_numbers = []
        MAX_LIMIT = 30
        array_length = int(input("How long would you like the array? "))
        # generate random numbers for an array of random length
        for _ in range(array_length):
            # generate a random number between 0 and 15
            random_int = random.randint(0, MAX_LIMIT)
            # append that random number to the array
            random_numbers.append(random_int)
        return random_numbers


    def write_file(random_numbers):
        """
        Open the file with settings to write to the file, 
        Write the random array of numbers to the file,
        close the file
        """
        # NOTE: "w" overwrites the content of the file, while "a" appends to the file content
        # In this case, we do not want to make the file any longer to save file space.
        random = open("random.txt", "w")
        random.write(str(random_numbers))
        random.close()


    def read_file(random_numbers):
        """
        Open the file with settings to read the text in the file, 
        Read and print the contents of the file, 
        Print the length of the array of nubers,
        Close the file
        """
        random = open("random.txt", "rt")
        print(random.read())
        print("The length of the array is: ", len(random_numbers))
        random.close()

play_again = 1
while play_again == 1:
    """
    Loop for the game.
    Broken by user input.
    """
    random_numbers = Game.number_generator()
    Game.write_file(random_numbers)
    Game.read_file(random_numbers)
    play_again = int(input("Would you like to roll again? (1 for yes, 0 for no) "))

exit()