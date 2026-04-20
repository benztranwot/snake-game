from turtle import Turtle

##
# @author Minh Quan Tran
# @class Scoreboard
# @brief A class to manage and display the score and high score in the game.
#
# Inherits from Turtle to render text on the screen.
class Scoreboard(Turtle):
    
    ##
    # @brief Constructor for the Scoreboard class.
    #
    # Initializes the scoreboard, loads the high score from a file,
    # and sets up the display position and appearance.
    def __init__(self):
        super().__init__()
        self.score = 0

        ## @brief Load the high score from file.
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

        ## @brief Initial rendering of the scoreboard.
        self.update_scoreboard()

    ##
    # @brief Updates the scoreboard display.
    #
    # Clears the previous text and writes the current score and high score.
    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    ##
    # @brief Resets the score and updates the high score if needed.
    #
    # If the current score exceeds the stored high score, it updates
    # the high score and writes it back to the file.
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            ## @brief Save the new high score to file.
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    ##
    # @brief Increases the score by one and updates the display.
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    ##
    # @brief Displays a "Game Over" message on the screen.
    #
    # (Currently commented out in original code.)
    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align="center", font=("Arial", 18, "normal"))