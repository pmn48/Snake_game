from turtle import Turtle, Screen

X_COR = [0, -20, -40]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.time_sleep = 0.3

    def create_snake(self):
        for position in range(len(X_COR)):
            tom = Turtle()
            tom.penup()
            tom.shape("square")
            tom.color("white")
            tom.setx(position)
            self.snake_list.append(tom)

    def new_segment(self, position):
        tommy = Turtle()
        tommy.penup()
        tommy.shape("square")
        tommy.color("white")
        tommy.goto(position)
        self.snake_list.append(tommy)

    def extra(self):
        self.new_segment(self.snake_list[-1].position())
        self.time_sleep *= 0.85

    def move(self):
        for i in range(-1, -len(self.snake_list), -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.head.forward(MOVE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def reset(self):
        for block in self.snake_list:
            block.goto((1200, 1200))
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
