from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.update_score()
        
        

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align="center", font=('Arial', 24, 'normal'))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        