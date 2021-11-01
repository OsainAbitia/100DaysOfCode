from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.onkey(right_paddle.go_up, "i")
screen.onkey(right_paddle.go_down, "k")

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    print(ball.movement_speed)
    screen.update()
    ball.move()

    # Detect colission with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball need to bounce
        ball.bounce_y()

    # Detect colliton with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
