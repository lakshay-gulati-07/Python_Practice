from turtle import Turtle
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-280,250)
        self.write(f"Level = {self.level}",font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level = {self.level}",font=FONT)

    def next_level(self):
        self.level +=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",font=FONT,align="center")

