from turtle import Turtle
ALLIGNMENT="center"
FONT=("courier", 32, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("#222831")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()



