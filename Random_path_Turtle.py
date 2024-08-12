import turtle
import random

tommy = turtle.Turtle()
tommy.color("blue")
colour = ["red","blue","cyan","pink","magenta","violet","pink","green"]
directions = [0,90,270,180,360]
tommy.width(10)
for i in range (50):
    tommy.forward(50)
    tommy.setheading(random.choice(directions))
    tommy.color(random.choice(colour))
  
    



screen = turtle.Screen()
screen.exitonclick()