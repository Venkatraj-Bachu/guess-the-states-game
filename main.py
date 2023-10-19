import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')
count = 0

states = states_data['state'].tolist()
guessed_states = []

while count < 50:
    answer_state = screen.textinput(title=f'{count}/50 Guess the state', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missed_states = [x for x in states if x not in guessed_states]
        missed_states_df = pandas.DataFrame(missed_states)
        missed_states_df.to_csv('states_to_learn.csv')
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer_state)
        count += 1

screen.exitonclick()