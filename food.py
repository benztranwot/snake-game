import random
from turtle import Turtle


##
# @author Minh Quan Tran
# @class Food
# @brief Represents the food object in the Snake game.
#
# This class inherits from the Turtle class and is used to create,
# display, and reposition the food that the snake consumes.
#
class Food(Turtle):
    ##
    # @brief Constructor for the Food class.
    #
    # Initializes the food object with a circular shape,
    # sets its size, color, speed, and places it at a random location.
    #
    def __init__(self):
        super().__init__()
        self.shape("circle")               ## Set shape to circle
        self.penup()                       ## Disable drawing lines
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  ## Scale down size
        self.color("red")                  ## Set food color
        self.speed("fastest")              ## Set animation speed
        self.refresh()                     ## Place food at random position

    ##
    # @brief Moves the food to a new random location on the screen.
    #
    # Generates random x and y coordinates within the game boundary
    # and updates the food's position.
    #
    # @return None
    #
    def refresh(self):
        random_x = random.randint(-280, 280)  ## Random X coordinate
        random_y = random.randint(-280, 280)  ## Random Y coordinate
        self.goto(random_x, random_y)         ## Move food to new position