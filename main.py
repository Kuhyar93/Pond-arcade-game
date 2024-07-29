from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
screen = Screen()


def setup_screen():
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.title('Pong')
    screen.tracer(0)
setup_screen()


# def move_paddle_1():
#     paddle_head = paddle_1[4]
#     for seg in range(len(paddle_1)):
#         new_x = paddle_1[seg + 1].xcor()
#         new_y = paddle_1[seg + 1].ycor()
#         paddle_1[seg].goto(new_x, new_y)
#     paddle_head.forward(20)
#
#
# for position in range(len(STARTING_POSITIONS_PADDLE_1)):
#     new_paddle_seg = Turtle()
#     new_paddle_seg.shape('square')
#     new_paddle_seg.color('white')
#     new_paddle_seg.setheading(90)
#     new_paddle_seg.speed('fastest')
#     new_paddle_seg.penup()
#     new_paddle_seg.goto(STARTING_POSITIONS_PADDLE_1[position])
#     paddle_1.append(new_paddle_seg)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increment_l_score()

    if ball.xcor() < -400:
        scoreboard.increment_r_score()
        ball.reset_position()




























screen.exitonclick()