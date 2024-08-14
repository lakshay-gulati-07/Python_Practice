import turtle
import random
screen = turtle.Screen()
bet = screen.textinput(title= "Place a Bet !",prompt="Whos Gonna Win ?? \n1.Red \n2.Green\n3.blue\n4.Purple\n5.violet")
screen.setup(height=600,width=600)
colors = ["red","green","blue","purple","violet"]
tommy_list = []
yposition = [-100,-50,0,50,100]
game_is_on = False
if bet:
    game_is_on=True

   
for i in range(5):
    new_tommy = turtle.Turtle()
    new_tommy.penup()
    new_tommy.shape("turtle")
    new_tommy.color(colors[i])
    new_tommy.goto(x=-285,y=yposition[i])
    new_tommy.forward(random.randint(0,10))
    tommy_list.append(new_tommy)

while game_is_on:
    for tommy in tommy_list:
        if tommy.xcor() >280:
            game_is_on = False
            winning_color = tommy.pencolor()
            if winning_color == bet:
                print(f"you won,{winning_color} Turtle ")
            else:
                print(f"you Lost, {winning_color} Turtle wins !!")
        else:
            tommy.forward(random.randint(0,10))


screen.exitonclick()