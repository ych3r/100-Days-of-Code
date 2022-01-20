import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in state_list:
            if state not in guessed_states:
                states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        point = turtle.Turtle()
        point.penup()
        point.hideturtle()
        point.goto(x, y)
        point.write(answer_state)
