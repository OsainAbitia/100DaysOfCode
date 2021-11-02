from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.starting_position()

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def has_finished(self):
        position = self.ycor()
        if position > FINISH_LINE_Y:
            self.starting_position()
            return True
