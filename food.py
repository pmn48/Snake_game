from turtle import Turtle
import random as rd

COLOR = ["blue", "gold", "turquoise", "magenta", "orange red", "deep pink"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # all attributes here come from the Turtle super class
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # stretch by the number
        self.color(rd.choice(COLOR))
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        self.goto(rd.randint(-270, 270), rd.randint(-270, 270))
