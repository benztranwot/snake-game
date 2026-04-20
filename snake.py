from turtle import Turtle

##
# @file snake.py
# @brief Defines the Snake class for the Snake Game.
#
# Handles snake creation, movement, growth, direction control,
# and reset behavior.

## Initial snake segment positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

## Distance the snake moves each step
MOVE_DISTANCE = 20

## Direction constants (in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


##
# @class Snake
# @brief Represents the snake in the game.
#
# Manages the snake's body segments, movement,
# direction changes, and growth.
class Snake:

    ##
    # @brief Constructor for Snake class.
    #
    # Initializes the snake segments and sets the head.
    def __init__(self):
        self.segments = []      ## List of snake segments
        self.create_snake()     ## Create initial snake body
        self.head = self.segments[0]  ## First segment is the head

    ##
    # @brief Create the initial snake body.
    #
    # Adds segments based on predefined starting positions.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    ##
    # @brief Add a new segment to the snake.
    #
    # @param position Tuple (x, y) where the segment will be placed.
    def add_segment(self, position):
        new_segment = Turtle("square")  ## Create square segment
        new_segment.color("white")      ## Set color
        new_segment.penup()             ## Prevent drawing lines
        new_segment.goto(position)      ## Move to position
        self.segments.append(new_segment)

    ##
    # @brief Reset the snake to initial state.
    #
    # Moves existing segments off-screen and recreates the snake.
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  ## Move segments out of view
        self.segments.clear()         ## Clear segment list
        self.create_snake()           ## Recreate snake
        self.head = self.segments[0]  ## Reset head reference

    ##
    # @brief Extend the snake by adding a segment.
    #
    # New segment is added at the position of the last segment.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    ##
    # @brief Move the snake forward.
    #
    # Each segment follows the one in front of it,
    # and the head moves forward.
    def move(self):
        # Move segments from tail to head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)  ## Move head forward

    ##
    # @brief Change direction to up.
    #
    # Prevents reversing direction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    ##
    # @brief Change direction to down.
    #
    # Prevents reversing direction.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    ##
    # @brief Change direction to left.
    #
    # Prevents reversing direction.
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    ##
    # @brief Change direction to right.
    #
    # Prevents reversing direction.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)