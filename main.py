"""
This random number generator demonstrates the following:
Variables, Expressions, Conditionals, Loops, Functions, Classes, Arrays,
reading/writing from a file, and inheritance.
"""

from random_numbers import Game

def start_game():
    """
    This function calls the functions of the game in the correct order.
    Built to refactor code and make it easier to debug.
    """
    play_again = 1
    while play_again == 1:
        """
        Loop for the game.
        Broken by user input.
        """
        g = Game()
        g.get_min_limit()
        g.get_max_limit()
        g.get_array_length()
        g.number_generator()
        g.write_file()
        g.read_file()
        play_again = int(input("Would you like to roll again? (1 for yes, 0 for no) "))

start_game()

exit()