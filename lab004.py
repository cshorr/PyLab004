import turtle
import random

t = turtle.Turtle()
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_pumpkin(t, x, y, radius):

    t.penup()  # Lift the pen to move without drawing
    t.goto(x, y)  # Move to the specified location
    t.pendown()  # Lower the pen to start drawing
    t.fillcolor("orange")  # Set the fill color to orange
    t.begin_fill()  # Start filling the shape
    t.circle(radius)  # Draw the pumpkin as a circle
    t.end_fill()  # Complete the fill
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
    import random

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

# Example usage
draw_sky(t, 20)  # Draw 20 stars

# Example usage
draw_star(t, -100, 150, 30)  # Star in the sky
draw_star(t, 100, 180, 20)
def draw_stem(t, x, y, radius):
    # Drawing the stem
    t.penup()
    t.goto(0, y + radius)  # Move to the top center of the circle
    t.pendown()
    t.fillcolor("green")  # Set the fill color to green for the stem
    t.begin_fill()  # Start filling the stem
    t.left(90)  # Rotate the turtle to point upwards
    t.forward(radius // 2)  # Draw the stem upwards
    t.left(90)  # Rotate to draw the horizontal part of the stem
    t.forward(radius // 5)  # Draw the top of the stem
    t.left(90)  # Rotate to draw the downward part of the stem
    t.forward(radius // 2)  # Draw the stem downwards
    t.left(90)  # Rotate to close the stem rectangle
    t.forward(radius // 5)  # Complete the stem
    t.end_fill()  # Complete the fill for the stem

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()

def draw_polygon(t, sides, size):
    """Draws a polygon with the given number of sides and size."""
    for _ in range(sides):
        t.forward(size)
        t.left(360 / sides)


draw_pumpkin(t, -150, -150, 100)
draw_eye(t, -190, -60, 30)  # Left eye
draw_eye(t, -110, -60, 30)  # Right eye
draw_mouth(t, -190, -100, 80)  # Mouth


# Draw the night sky
draw_sky(t, 30)

# Close the turtle graphics window when clicked
turtle.exitonclick()
