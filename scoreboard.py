from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            content = file.read()
            self.high_score = int(content)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"    GAME OVER ", align=ALIGNMENT, font=FONT)

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
