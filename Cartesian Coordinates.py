# Importing necessary libraries
import time
import os

# Define the Canvas class
class Canvas:
    # Initialize the Canvas with width and height
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # Create a 2D list to represent the canvas
        self._canvas = [[' ' for _ in range(self._y)] for _ in range(self._x)]

    # Method to set a position on the canvas with a mark
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark 
    
    # Method to clear the terminal screen
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Method to print the canvas with clearing the screen first
    def print(self):
        self.clear()
        # Print the canvas content row by row
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

# Define the TerminalScribe class
class TerminalScribe:
    # Initialize the TerminalScribe with a canvas object
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos = [0, 0]  # Initial position
        self.mark = '*'    # Mark to draw
        self.trail = '.'   # Trail mark

    # Method to draw on the canvas
    def draw(self, pos):
        # Set the trail mark at the current position
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos  # Update the position
        self.canvas.setPos(self.pos, self.mark)  # Set the mark at the new position
        self.canvas.print()  # Print the updated canvas

# Create a Canvas object with dimensions 20x20
canvas = Canvas(20, 20)
# Create a TerminalScribe object with the canvas object
scribe = TerminalScribe(canvas)

# Loop to draw on the canvas
for i in range(10):
    for j in range(10):
        scribe.draw([i, j])  # Draw at each position in the loop