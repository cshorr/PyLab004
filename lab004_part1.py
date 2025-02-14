import turtle
import math

def polyline(t: turtle.Turtle, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t: turtle.Turtle, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t,n, length, step_angle)


def jump(t: turtle.Turtle,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def rectangle(t: turtle.Turtle, base, height):
    for length in (base, height, base, height):
        t.forward(length)
        t.left(90)

def square(t: turtle.Turtle, length):
    rectangle(t, length, length)

def draw_ribbon(t: turtle.Turtle, x, y, base, height, color = "green"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base,height)
    t.end_fill()

def draw_bow(t: turtle.Turtle, x, y, bow_size=50, color = "green"):
    jump(t, x, y)
    temp_color = t.color()
    t.pensize(3.5)
    t.color(color)
    t.right(15)
    print (t.pos())
    arc(t,bow_size, 120)
    t.left(60)
    arc(t,bow_size, 120)
    t.right(200)
    arc(t,bow_size, 120)
    t.left(60)
    arc(t,bow_size, 120)
    print(t.pos(), t.heading())


def draw_present(t: turtle.Turtle, x, y, base, height, ribbon_width, color= "red"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base,height)
    t.end_fill()
    p_center = (x + (base/2))
    r_x = p_center - (ribbon_width / 2)
    draw_ribbon(t, r_x, y, ribbon_width, height)
    r_y = (y + height / 2 - (ribbon_width / 2))
    draw_ribbon(t,x, r_y, base,ribbon_width)
    draw_bow(t, p_center, y + height, base /3)

t = turtle.Turtle()
t.speed(10)
#t.hideturtle()
screen = turtle.Screen()

# Create a window to draw in
screen.bgcolor("darkblue")
screen.setup(width=625, height=625)

t.color("white")

# Draw the squares
draw_present(t, -50, -50, 100, 100, ribbon_width = 10)

turtle.done()








































