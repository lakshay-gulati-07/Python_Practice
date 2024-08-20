import turtle
from paddle import Paddle
from ball import Ball
import time


screen = turtle.Screen()
screen.tracer(0)
screen.title("P O N G")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.listen()

ball = Ball()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()








screen.exitonclick()