# import the random python module to help generate random numbers
import random

class Game():
    """
    This class contains all the functions for the program.
    """
    def __init__(self):
        self.random_numbers = []
        
    def get_min_limit(self):
        """
        Get the min number limit for the randomly generated numbers from the user.
        """
        self.MIN_LIMIT = int(input("What would you like the lowest number to be? "))

    def get_max_limit(self):
        """
        Get the max number limit for the randomly generated numbers from the user.
        """
        self.MAX_LIMIT = int(input("What would you like the highest number to be? "))

    def get_array_length(self):
        """
        Get array length from the user.
        """
        self.array_length = int(input("How long would you like the array? "))
    
    def number_generator(self):
        """
        Generate a random length between 0 and 30,
        Generate random numbers until length is reached,
        Append each number to the end of the array,
        Return the array of random numbers.
        """        
        # generate random numbers for an array of random length
        for _ in range(self.array_length):
            # generate a random number between 0 and 15
            random_int = random.randint(self.MIN_LIMIT, self.MAX_LIMIT)
            # append that random number to the array
            self.random_numbers.append(random_int)
        return self.random_numbers


    def write_file(self):
        """
        Open the file with settings to write to the file, 
        Write the random array of numbers to the file,
        Close the file.
        """
        # NOTE: "w" overwrites the content of the file, while "a" appends to the file content
        # In this case, we do not want to make the file any longer to save file space.
        random = open("random.txt", "w")
        random.write(str(self.random_numbers))
        random.close()


    def read_file(self):
        """
        Open the file with settings to read the text in the file, 
        Read and print the contents of the file, 
        Print the length of the array of nubers,
        Close the file.
        """
        random = open("random.txt", "rt")
        print(random.read())
        print("The length of the array is: ", len(self.random_numbers))
        random.close()
