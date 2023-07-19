# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()


# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def counter_clockwise():
#     tim.left(8)
#
#
# def clockwise():
#     tim.right(8)
#
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_drawing)
# screen.exitonclick()


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a rainbow color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


y = 170
for _ in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(_)
    new_turtle.goto(x=-230, y=y)
    y -= 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
