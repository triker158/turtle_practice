# for, while and break practice
import turtle


def spiral(max_fwd):
    for fwd in range(max_fwd):
        turtle.left(20)
        turtle.forward(fwd)


# conditional loop always starting at origin
# stop when max distance from origin reached
def spiralMax(max_dist):
    dist = 0
    fwd = 1
    while dist < max_dist:
        turtle.left(10)
        turtle.forward(fwd)
        dist = turtle.distance(0, 0)
        fwd += .1
    print(turtle.distance(0, 0))


# infinite loop w/break on condition, start anywhere
# stop when max distance from start point reached
def draw_spiral(radius):
    original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        if turtle.distance(original_xcor, original_ycor) > radius:
            break
    print(turtle.distance(0, 0))


# go forward only if the pen is up
def forwardPenup(dist):
    if not turtle.isdown():
        turtle.forward(dist)
    else:
        print("pen is down")


spiralMax(100)
draw_spiral(100)

# x = False
# if not x:
#     print("condition met")
# else:
#     print("condition not met")

# turtle.forward(50)
# forwardPenup(100)

turtle.exitonclick()
