import turtle


# data munging: strip() removes whitespace, lower() makes lowercase

def move():
    direction = input("Go left or right? ")
    direction = direction.strip().lower()
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction == "right":
        turtle.right(60)
        turtle.forward(50)


def shape():
    shapeIn = input("what shape shall we draw?")
    shapeIn = shapeIn.strip().lower()
    if shapeIn == "circle":
        for _ in range(90):
            turtle.forward(4)
            turtle.left(4)
    if shapeIn == "square":
        for _ in range(4):
            turtle.forward(60)
            turtle.left(90)
    if shapeIn == "star":
        turtle.left(36)
        for _ in range(10):
            for _ in range(5):
                turtle.forward(150)
                turtle.left(144)
            turtle.left(36)


# for _ in range(5):
shape()

# for _ in range(5):
#     move()

# direction = -30
# if direction > 0:
#     turtle.forward(direction)
# else:
#     turtle.left(180)
#     turtle.forward(-direction)

turtle.exitonclick()
