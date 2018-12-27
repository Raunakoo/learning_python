import turtle
from itertools import cycle


colors= cycle(["red", "orange", "yellow", "purple", "green", "blue", \
                "deep pink", "tomato", "medium orchid", "chartreuse", "cyan", "dark orange", "chocolate", "peach puff", "cornflower blue"])


def circle_draw(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    turtle.left(shift)
    turtle.right(shift)
    circle_draw(size+5, angle+1, shift+1)
#background color
turtle.bgcolor("black")
#turtle speed
turtle.speed("fast")
#size of loops
turtle.pensize(5)
circle_draw(30, 0 ,1)


turtle.pencolor("green")
turtle.circle(20)