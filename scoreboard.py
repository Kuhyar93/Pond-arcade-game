from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-10, 220)
        self.write(f"{self.l_score}       {self.r_score}", align='center', font=("Arial", 52, "normal"))


    def increment_l_score(self):
        self.l_score += 1
        self.update()
    def increment_r_score(self):
        self.r_score += 1
        self.update()