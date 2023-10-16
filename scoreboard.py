from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.score=0

        self.color("white")
        self.penup()
        self.goto(0,270)
    def update_scoreboaqrd(self):
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))




    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
