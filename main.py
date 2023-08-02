from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score
score = Scoreboard()
padle1 = Turtle()  # Paddle(color="white", wid=5, len=1, x_pos=350, y_pos=0)

sleep_time = 0.1


scren = Screen()
scren.screensize(800, 600)
scren.bgcolor("black")
scren.title("PONG")
scren.tracer(0)

# Ad2
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

scren.listen()
scren.onkey(r_paddle.go_up, "Up")
scren.onkey(r_paddle.go_down, "Down")
scren.onkey(l_paddle.go_up, "w")
scren.onkey(l_paddle.go_down, "s")

# Ad4
ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_sped)
    scren.update()
    ball.move()

    # Detect collision with r_padle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.move(20)
        ball.move_sped *= 0.9
        print("make contact")
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.move(-20)
        print("make contact")
        ball.move_sped *= 0.9
    if ball.ycor() > 280:
        ball.bounce('y')

    if ball.ycor() < -280:
        ball.bounce('y')

    if ball.xcor() > 340:
        ball.game_over()
        ball.move_sped = 0.1
        score.l_up()

    if ball.xcor() < -340:
        ball.game_over()
        ball.move_sped = 0.1
        score.r_up()

# exit when click
scren.exitonclick()
