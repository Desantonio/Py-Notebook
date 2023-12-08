import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Simple Button")

button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack()

root.mainloop()

import turtle
from random import randint

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest drawing speed

# Draw the spiral pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for _ in range(360):
    spiral_turtle.color(colors[randint(0, 5)])
    spiral_turtle.forward(100)
    spiral_turtle.right(45)
    spiral_turtle.forward(50)
    spiral_turtle.right(45)
    spiral_turtle.forward(100)
    spiral_turtle.right(91)

# Hide the turtle and display the graphics
spiral_turtle.hideturtle()
turtle.done()
