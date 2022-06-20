from state_names import StateName
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=600)
sb = Scoreboard()

turtle.shape(image)

data = pd.read_csv("50_states.csv")

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in data["state"].values:
            if state not in guessed_states:
                states_to_learn.append(state)

        states_df = pd.DataFrame(states_to_learn)
        states_df.to_csv("states_to_learn.csv")
        break
    print(answer_state)
    answer_row = data[data.state == answer_state].index.values
    y = data.at[answer_row[0], "y"]
    x = data.at[answer_row[0], "x"]
    state = StateName()
    if answer_state in data.state.values and answer_state not in guessed_states:
        state.write_state(x, y, answer_state)
        sb.update_score()
        sb.write_score()
        guessed_states.append(answer_state)

# states_to_learn.to_csv(states_to_learn.csv)
# Create a list of states that the user still needs to learn and save it as a csv
