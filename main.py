from turtle import Turtle, Screen
from paddle import Paddle
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

padle1 = Turtle()  # Paddle(color="white", wid=5, len=1, x_pos=350, y_pos=0)

padle1.shape("square")
padle1.color("white")
padle1.shapesize(5, 1, None)
padle1.penup()
padle1.goto(350, 0)

scren = Screen()
scren.screensize(800, 600)
scren.bgcolor("black")
scren.title("PONG")
scren.tracer(0)

# Ad2


def go_up():
    new_y = padle1.ycor()+20
    padle1.goto(padle1.xcor(), new_y)


def go_down():
    new_y = padle1.ycor()-20
    padle1.goto(padle1.xcor(), new_y)


scren.listen()
scren.onkey(go_up, "Up")
scren.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    scren.update()

# exit when click
scren.exitonclick()
