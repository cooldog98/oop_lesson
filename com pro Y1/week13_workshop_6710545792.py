import turtle
start = 0


def move_up():
    global start
    if start != 1:
        turtle.setheading(90)
        start = 1
    else:
        turtle.forward(10)


def move_down():
    global start
    if start != 2:
        turtle.setheading(270)
        start = 2
    else:
        turtle.forward(10)


def move_right():
    global start
    if start != 3:
        turtle.setheading(0)
        start = 3
    else:
        turtle.forward(10)


def move_left():
    global start
    if start != 4:
        turtle.setheading(180)
        start = 4
    else:
        turtle.forward(10)


turtle.onkey(move_up, "Up")
turtle.onkey(move_down, 'Down')
turtle.onkey(move_right, 'Right')
turtle.onkey(move_left, 'Left')

turtle.listen()
turtle.done()