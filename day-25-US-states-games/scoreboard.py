from turtle import Turtle
import pandas as pd
from turtle import Turtle


class Scoreboard():
    def __init__(self) -> None:
        self.data = pd.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.states_found = 0
        self.guessed_states = []
        self.missing_states = []

    def find_state(self, state):
        if state in self.all_states:
            self.write_state(state, self.data[self.data.state == state])

    def write_state(self, state, state_data):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(int(state_data.x), int(state_data.y))
        new_state.write(state, align="center",
                        font=("Courier", 8, "normal"))
        self.guessed_states.append(state)
        self.states_found += 1

    def missing_states_csv(self):
        # Apply list comprehensions
        self.missing_states = [
            state for state in self.all_states if state not in self.guessed_states]
        # for state in self.all_states:
        #     if state not in self.guessed_states:
        #         self.missing_states.append(state)

        new_data = pd.DataFrame(self.missing_states)
        new_data.to_csv("states_to_learn.csv")
