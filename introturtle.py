import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 5
size_length = 80
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(size_length)
    polygon.right(angle)
turtle.done()

