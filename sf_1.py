#Geometric shape maker 

import turtle
import easygui

#functions 

def draw_square(size, color):
    """Draws a square using 90-degree exterior turns."""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(size, color):
    """Draws an equilateral triangle using 120-degree exterior turns."""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_circles(radius, color):
    """Draws 3 concentric circles starting from the center outward."""
    turtle.color(color)
    # Draw 3 concentric circles scaling by step sizes
    for multiplier in [0.5,0.75,1.0]:
        current_r = radius * multiplier
        turtle.penup()
        # Move down by radius to keep circles centered at origin (0, 0)
        turtle.goto(0, -current_r)
        turtle.pendown()
        
        turtle.begin_fill()
        turtle.circle(current_r)
        turtle.end_fill()

def draw_star(size, color):
    """Draws a classic 5-pointed star using 144-degree turns."""
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


#GUI

def run_studio():
    # Step A: Choose Shape
    shape = easygui.buttonbox(
        msg="Select a geometric shape to render:",
        title="Interactive Geometric Pattern Studio",
        choices=["Square", "Equilateral Triangle", "Concentric Circles", "Custom Star"]
    )
    if not shape:  # User closed window or clicked cancel
        return

    # Step B: Gather Dimensions (Range 50 to 250)
    dimension = easygui.integerbox(
        msg="Enter size / base radius (50 to 250):",
        title="Dimension Input",
        default=100,
        lowerbound=50,
        upperbound=250
    )
    if not dimension:
        return

    # Step C: Gather Color Choice
    color = easygui.enterbox(
        msg="Enter fill color (e.g., 'blue', 'red', 'teal', 'gold'):",
        title="Color Selection",
        default="black"
    )
    if not color:
        return

    # Step D: Setup Turtle Screen
    screen = turtle.Screen()
    screen.title(f"Studio — {shape}")
    turtle.speed(1)
    turtle.hideturtle() 

    # Step E: Route to Specific Drawing Function
    try:
        if shape == "Square":
            draw_square(dimension, color)
        elif shape == "Equilateral Triangle":
            draw_triangle(dimension, color)
        elif shape == "Concentric Circles":
            draw_circles(dimension, color)
        elif shape == "Custom Star":
            draw_star(dimension, color)
    except turtle.TurtleGraphicsError:
        easygui.msgbox("Invalid color name entered! Drawing without fill.", title="Warning")

    # Step F: Teardown & Alert
    easygui.msgbox("Drawing completed successfully!", title="Done")
    turtle.bye()

#Entry here
#if __name__ == "__main__": -  this line is 
# written so that is any person wants to access this code by 
# importing it, the code will not run automatically.
run_studio()