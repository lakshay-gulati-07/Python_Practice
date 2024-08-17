from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.refresh()
        self.speed("fastest")

    def refresh(self):
        x_cor = random.randint(-270,270)
        y_cor = random.randint(-270,270)
        self.goto(x=x_cor,y=y_cor)

