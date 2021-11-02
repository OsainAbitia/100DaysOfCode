from turtle import Turtle, down
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.set_score()

    def set_score(self):
        self.goto(-200, 250)
        self.write(f'Level: {self.score}', align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.set_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
