# write some functions for turtle movement
import turtle


def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)


def star_arm():
    line_without_moving()
    turtle.right(360/5)


def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_shape(sides, size):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)


# draw a shape by passing the direction to draw
def draw_shape_dir(sides, size, dir):
    for i in range(sides):
        turtle.forward(size)
        dir(360/sides)


# for _ in range(5):
#     star_arm()

# draw a honeycomb
# for _ in range(6):
#     draw_shape(6, 100)
#     turtle.forward(100)
#     turtle.right(60)

# 2 iterations so there is time to watch it draw
for _ in range(2):
    draw_shape_dir(3, 100, turtle.right) # triangle
    draw_shape_dir(4, 75, turtle.left) # square
    draw_shape_dir(90, 4, turtle.right) # circle

# draw_square(100)
# draw_square(200)

# line_without_moving()
# turtle.right(90)
# line_without_moving()
# turtle.right(90)
# line_without_moving()
# turtle.right(90)
# line_without_moving()

turtle.exitonclick()
