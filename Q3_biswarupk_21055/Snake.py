class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################
        self.color = 'yellow'
        self.direction = 'Up' 
        self.window_size = window_size
        self.GAME_OVER = False
        self.position = [0,0]        

    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.direction != 'Down':
            self.direction = 'Up'

        ##########################################
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'Up':
            self.direction = 'Down'

        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'Right':
            self.direction = 'Left'

        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.direction != 'Left':
            self.direction = 'Right'

        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############
        distance = 20
        if abs(self.position[0] - current_food_position[0]) < distance \
            and abs(self.position[1] - current_food_position[1]) < distance:
            return True
        return False
        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############
        if self.position[0] < -1 * self.window_size[0] / 2: 
            self.position[0] = self.window_size[0] / 2
        if self.position[0] > self.window_size[0] / 2: 
            self.position[0] = -1 * self.window_size[0] / 2
        if self.position[1] < -1 * self.window_size[1] / 2: 
            self.position[1] = self.window_size[1] / 2
        if self.position[1] > self.window_size[1] / 2: 
            self.position[1] = -1 * self.window_size[1] / 2
        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """

        ############## WRITE BELOW ###############
        position_update = 10
        if self.direction == "Up":
            self.position[1] = self.position[1] + position_update
        if self.direction == "Down":
            self.position[1] = self.position[1] - position_update
        if self.direction == "Left":
            self.position[0] = self.position[0] - position_update
        if self.direction == "Right":
            self.position[0] = self.position[0] + position_update

        self.keep_snake_onscreen()
        ##########################################









