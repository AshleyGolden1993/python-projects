# Imports
import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

# Create keybinding for user to turn the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# Snake movement forward
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food using distance method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        sb.game_over()

    # Detext collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            sb.game_over()

screen.exitonclick()

