from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Turtle()
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.goto(350, 0)
paddle.shapesize(stretch_wid=5, stretch_len=1)
screen.tracer(0)

def move_up():
    paddle.setheading(90)

def move_down():
    paddle.setheading(270)

game_is_on = True

"""while game_is_on:"""










screen.exitonclick()