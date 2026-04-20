import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

##
# @file main.py
# @brief Main entry point for the Snake Game.
#
# This file initializes the game window, handles user input,
# runs the main game loop, and manages collision detection.

## Initialize the game screen
screen = Screen()
screen.setup(width=600, height=600)  ## Set screen dimensions
screen.bgcolor("black")              ## Set background color
screen.title("Snake Game")           ## Set window title
screen.tracer(0)                     ## Turn off automatic screen updates

## Create game objects
snake = Snake()          ## Snake object (player)
food = Food()            ## Food object
scoreboard = Scoreboard()## Score tracking object

## Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")     ## Move snake up
screen.onkey(snake.down, "Down") ## Move snake down
screen.onkey(snake.left, "Left") ## Move snake left
screen.onkey(snake.right, "Right") ## Move snake right

## Game loop control flag
game_is_on = True

##
# @brief Main game loop.
#
# Continuously updates the screen, moves the snake,
# and checks for collisions with food, walls, and itself.
while game_is_on:
    screen.update()      ## Refresh screen manually
    time.sleep(0.1)      ## Control game speed
    snake.move()         ## Move the snake forward

    ## Detect collision with food
    # If snake head is close enough to the food, trigger:
    # - Food reposition
    # - Score increment
    # - Snake growth
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    ## Detect collision with wall
    # If snake hits boundary, reset game state
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    ## Detect collision with tail
    # Check if head collides with any body segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

## Exit game when screen is clicked
screen.exitonclick()