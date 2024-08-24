from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.color("white")
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            False

    def start(self):
        self.goto(STARTING_POSITION)