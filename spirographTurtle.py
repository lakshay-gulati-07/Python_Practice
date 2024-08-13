import turtle
import random

tommy = turtle.Turtle()
tommy.speed("fastest")
turtle.colormode(255)
def color_generation():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tommy.color(color_generation())
        tommy.circle(100)
        tommy.setheading(tommy.heading() + size_of_gap)

spirograph(5)


screen = turtle.Screen()
screen.exitonclick()