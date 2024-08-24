import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
screen.listen()
screen.onkey(player.move_forward,"Up")
car = CarManager()
car.createCar()
score = Scoreboard()
screen.title("T U R T L E    C R O S S I N G ")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.createCar()
    car.move_car()
    for c in car.cars_list:
        if c.distance(player) < 25 :
            game_is_on = False
            score.game_over()
    
    if player.is_at_finish_line():
        player.start()
        car.level_up()
        score.next_level()
    
    


screen.exitonclick()