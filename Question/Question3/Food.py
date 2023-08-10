"""
Imports
"""
import random # used to generate random positions of the food


"""
File that implements the Food class
"""
class Food:
    """
    Class that holds all the attributes of the food
    that the snake consumes in the game.
    """
    def __init__(self, window_size: tuple):
        """
        Constructor for the Food class. Takes the game
        window size as tuple for input. Has to initialize
        the following parameters.

        shape: str
               Indicates the shape of the food. Can have the
               values  “arrow”, “turtle”, “circle”, “square”,
               “triangle” and “classic”.

        color: str or tuple of RGB integers.
               Indicates the color of the food. Can have values
               "red", "green", "yellow" etc or be a tuple of
               integers like (44,99,244).

        size:  int
               Indicates the size of the food.

        window_size:
                tuple of integers
                Holds the size of the current game window

        position: tuple of integers
                  Holds the (x,y) position of the food


        You are to initialize the above variables with suitable
        values.

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW  ###############
        self.shape = "circle"
        self.color = "red"
        self.size = 10
        self.window_size = window_size
        self.position = (0,0)


        ###########################################

    def set_position(self, new_food_position: tuple) -> None:
        """
        Function that updates the value of the position of the
        food with the value that is passed to the function.

        :param new_food_position: A tuple of integers which
                                  represents the new position
                                  of the food.
        :return: None
        """
        ############### WRITE BELOW ################
        self.position = new_food_position


        ############################################

    def update_random_food_position(self)-> None:
        """
        Function that generates a random pair of (x,y)
        points inside the game window and updates the
        value of the position
        :return: None
        """
        ################ WRITE HERE ################
        x = random.randint(-1*(self.window_size[0]/2-20), self.window_size[0]/2-20)
        y = random.randint(-1*(self.window_size[1]/2-20), self.window_size[1]/2-20)
        self.set_position((x,y))
        ############################################

