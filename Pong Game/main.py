# Imports
from turtle import Turtle, Screen
from paddle import Paddle
from tkinter import messagebox as mb
from ball import Ball
from scoreboard import Scoreboard
import time


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

net = Turtle()
net.width(3)
net.color("white")
net.pu()
net.ht()
net.goto(x=0, y=-300)
net.seth(90)
# Use a for loop to draw a dashed line to the top of the screen
for step in range(30):
    net.pd()
    net.fd(10)
    net.pu()
    net.fd(10)

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
sb = Scoreboard()
ball_speed = 0.1

# Paddle movement
screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

# Create algorithm for how many degrees the ball will turn depending on the degrees at which it hit the wall/paddle

# Start Game
mb.showinfo(message="Welcome to the pong game!\nPress ok to start.")

# Add screen.update() down here somewhere
game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()
    # Detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()
        ball_speed -= 0.01

    if ball.xcor() > 380:
        ball.restart()
        sb.l_point()
        ball_speed = 0.1

    if ball.xcor() < -380:
        ball.restart()
        sb.r_point()
        ball_speed = 0.1

screen.exitonclick()
