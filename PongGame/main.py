import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.tracer(0)
screen.title("P O N G")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.listen()


ball = Ball()
score = Scoreboard()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.xbounce()

    # Misses right Paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        

    
    # Misses Left Paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()








screen.exitonclick()
