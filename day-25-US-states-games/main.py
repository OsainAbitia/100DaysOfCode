import turtle
from scoreboard import Scoreboard

screen = turtle.Screen()
score = Scoreboard()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(700, 500)
turtle.shape(image)


game_is_on = True
while game_is_on:

    if score.states_found == len(score.all_states):
        print("You've won!")
        game_is_on = False

    # We use title() functions so we can match, for example, new york with New York
    answer_state = screen.textinput(
        title=f"{score.states_found}/50 States Remaining", prompt="What's another state's name?").title()

    # Generate csv with missing states
    if answer_state == 'Exit':
        score.missing_states_csv()
        print(
            "Great! You'll find a csv of missing states to help you improve for next time!")
        game_is_on = False

    # Find the state
    score.find_state(answer_state)


turtle.mainloop()
