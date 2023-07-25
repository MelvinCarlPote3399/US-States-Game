import turtle
import pandas

# Create screen/window
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

# display map image in place of a normal turtle
turtle.shape(image)

# Obtain data from CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# empty array to add attempts into
guessed_states = []

# allow user to guess until the length of the initial empty array is 50, or user enters "exit"
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter the name of a state:").title()
    print(answer_state)

    """
    If user enters "Exit", break out of the while loop; all missing states that aren't 
    answered during the loop are appended to a new CSV file. Otherwise, if all states are guessed correctly, the CSV file
    will essentially be empty, or the file may not be generated
    """

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    """
    If answer_state is one of the states in the CSV file, display text to the map, 
    corresponding to the correct position on the map, in place of a turtle
    """
    if answer_state in all_states:
        guessed_states.append(answer_state)
    # if user gets it right
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# screen.exitonclick()