from turtle import Turtle
import random
COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            ycor = random.randint(-230,230)
            new_car.goto(280,ycor)
            self.cars_list.append(new_car)
        
    def move_car(self):
       for car in self.cars_list:
           car.forward(self.carspeed)
       
    def level_up(self):
        self.carspeed += MOVE_INCREMENT



    