from turtle import Turtle
xpositions = [-20,0,20]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head =self.snake_body[0]

    
    def create_snake(self):
        for i in range(0,3):
            snake = Turtle()
            snake.penup()
            snake.goto(x=xpositions[i],y=0)
            snake.shape("square")
            snake.color("white")
            self.snake_body.append(snake)

    
    def move(self):
        for snake_part in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake_part -1].xcor()
            new_y = self.snake_body[snake_part -1].ycor()
            self.snake_body[snake_part].goto(new_x,new_y)
        self.snake_body[0].forward(10)
    
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)


