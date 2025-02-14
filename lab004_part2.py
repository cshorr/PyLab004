import turtle
import random
t = turtle.Turtle()
def draw_square(t, length):
    """Draws a square with a given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with a given radius."""
    t.circle(radius)
def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
def jump(t: turtle.Turtle,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    #"""Draws one triangular eye at the given (x, y) position."""
def draw_eye(t, x, y, size, ):
     jump(t, x, y)
     t.fillcolor("yellow")
     t.begin_fill()
     draw_polygon(t, 3, size)
     t.end_fill()

def draw_mouth(t, x, y, width, ):
    """Draws a jagged mouth using a series of connected lines."""
    jump(t, x, y)
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_pumpkin(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    jump(t, x+(radius //10), y +2*radius)
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()


def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_jack(t, x , y, radius):
    draw_pumpkin(t, x, y, radius)
    eye_height = y + .55*2*radius
    mouth_height = y + .33*2*radius
    eye_size = radius/4
    draw_eye(t, x - .333* radius, eye_height, eye_size)  # Left eye
    draw_eye(t, x + .333* radius, eye_height, eye_size)  # Right eye
    draw_mouth(t, x -.333*radius, mouth_height, radius)  # Mouth

t.speed(00)
t.clear()
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
t.color("white")



# Example of drawing a jack-o-lantern with eyes and a mouth
# Draw three jack-o-lanterns


draw_jack(t, -150, -285, 107)

draw_jack(t, 25, -260, 50)

draw_jack(t, 165, -290, 75)
# Draw the night sky
draw_sky(t, 30)
turtle.done()






