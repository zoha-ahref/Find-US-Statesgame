from turtle import Turtle, Screen
import pandas

tim = Turtle()
screen = Screen()
screen.title("U.S States Games")

image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
data = pandas.read_csv("50_states.csv")
# data_dict = data.to_dict()
all_states = data.state.to_list()
# state_x_cor = data["x"].to_list
# state_y_cor = data["y"].to_list
# print(state_x_cor)
# data_dict = data.set_index('state').T.to_dict('list')
# print(data_dict)

# create a turtle to write


# game_is_on = True
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What is another state's name?").title()
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df= pandas.DataFrame(missing_states)
        df.to_csv("learn-states.csv")
        break

    if guess in all_states:
        guessed_states.append(guess)
        tim_new = Turtle()
        tim_new.hideturtle()
        tim_new.penup()
        state_data = data[data.state == guess]
        tim_new.goto(int(state_data.x), int(state_data.y))
        tim_new.write(guess)

df = pandas.DataFrame(missing_states)
df.to_csv("learn-states.csv")

# for states in all_states:
#     if guessed_states in all_states:
#         print(all_states.remove(guessed_states))

# for states in all_states:
#     if guessed_states in all_states:
#           correct_states = all_states.remove(guessed_states)
#     print(correct_states)
# print(guessed_states)
# correct_states = all_states - guessed_states
# print(correct_states)
# screen.exitonclick()
