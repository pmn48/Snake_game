from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import numpy as np

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(fun=snake.left, key="Left")  # turn left with left arrow
screen.onkey(fun=snake.right, key="Right")  # turn left with left arrow
screen.onkey(fun=snake.up, key="Up")  # turn left with left arrow
screen.onkey(fun=snake.down, key="Down")  # turn left with left arrow

running = True
time_sleep = 0.1
stop_point = 0
while running:
    screen.update()
    snake.move()
    time.sleep(snake.time_sleep)
    # Detect collisions with food and grow an extra block
    if snake.head.distance(food) < 25:
        food.new_food()
        snake.extra()
        scoreboard.increase()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.save_high_score()
        snake.reset()
        running = False
        # scoreboard.game_over()
    # Detect collision with self
    for seg in snake.snake_list[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.save_high_score()
            snake.reset()
            running = False
            # scoreboard.game_over()

screen.exitonclick()
