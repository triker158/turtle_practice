# turtle in a prison. turn around when he hits a wall
import turtle
import math


# version is ok but can't handle high numbers
def forward(distance):
    if distance > 100:
        remainder = distance - 100
        turtle.forward(distance)
        angle = turtle.towards(0, 0)
        turtle.setheading(angle)
        turtle.forward(remainder)
    else:
        turtle.forward(distance)


# version is better but slower.  any number.
def forward2(distance):
    while distance > 0:
        if turtle.distance(0, 0) > 100:
            angle = turtle.towards(0, 0)
            turtle.setheading(angle)
        turtle.forward(1)
        distance = distance - 1


# go forward only if the pen is up
def forwardPenup(dist):
    if not turtle.isdown():
        turtle.forward(dist)


# draw a square
def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


# draw the prison centered at origin and set turtle to origin
def drawPrison(size):
    turtle.penup()
    turtle.setpos(-size, -size)
    turtle.pendown()
    draw_square(size * 2)
    turtle.penup()
    turtle.home()
    turtle.pendown()


# box prison. turn back towards center (my solution)
def forwardBox(distance):
    original_xcor = 0
    original_ycor = 0
    x_dist = 0
    y_dist = 0
    while distance > 0:
        if x_dist >= 100 or y_dist >= 100:
            turtle.setheading(turtle.towards(0, 0))
            print("wall: " + str(turtle.xcor()) + ", " + str(turtle.ycor()) + " : " + str(distance))
        turtle.forward(1)
        x_dist = math.fabs(turtle.xcor() - original_xcor)
        y_dist = math.fabs(turtle.ycor() - original_ycor)
        distance -= 1
    print("final: " + str(turtle.xcor()) + ", " + str(turtle.ycor()) + " : " + str(distance))


# box prison solution from training. turn back towards center
def forwardBox2(distance):
    while distance > 0:
        if (turtle.xcor() > 100
            or turtle.xcor() < -100
            or turtle.ycor() > 100
            or turtle.ycor() < -100):
            turtle.setheading(turtle.towards(0, 0))
        turtle.forward(1)
        distance = distance - 1


# box prison. reflect in the box at same angle
def reflectBox(prison, gamma, distance):
    original_xcor = 0
    original_ycor = 0
    x_dist = 0
    y_dist = 0
    turtle.left(gamma)
    while distance > 0:
        if x_dist >= prison or y_dist >= prison:
            theta = 90 - gamma
            turtle.left(theta * 2)
            gamma = theta
            print("wall: " + str(turtle.pos()) + " : " + str(distance))
        turtle.forward(1)
        x_dist = math.fabs(turtle.xcor() - original_xcor)
        y_dist = math.fabs(turtle.ycor() - original_ycor)
        distance -= 1
    print("final: " + str(turtle.pos()) + " : " + str(distance))


drawPrison(80)
reflectBox(80, 30, 1000)

# drawPrison(100)
# turtle.left(138)
# forwardBox(500)
# turtle.left(35)
# forwardBox(500)

# turtle.reset()
# forward2(420)

turtle.exitonclick()
