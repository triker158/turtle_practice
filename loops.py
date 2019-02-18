# excercises with for loops and some notes
import turtle

# ctrl + ` toggles the terminal window closed to put focus
#          back to the editor window

# Ctrl+K+C to comment out the section of code
# Ctrl+K+U will uncomment the code

# for loops practice
# for name in "John", "Sam", "Jill":
#    print("hello " + name)

# for i in range(1,10,3):
#   print(i)

# total = 0
# for i in 5, 7, 11, 13:
#     print(i)
#     total = total + i
# print(total)

# loop variable not necessary unless it needs referenced
# for _ in range(10):
#     print("wassup")

# dashed line, dashes get bigger
# for i in range(10,20):
#     turtle.pendown()
#     turtle.forward(5+i)
#     turtle.penup()
#     turtle.forward(5)
# turtle.exitonclick()

# draw a square
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.exitonclick()
