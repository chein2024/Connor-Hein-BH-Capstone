import os
import time
from termcolor import colored
import math

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def forward(self, distance):
        for _ in range(distance):
            pos = [self.pos[0] + self.direction[0]*0.5, self.pos[1] + self.direction[1]*0.5]
            if not self.canvas.hitsWall(pos):
                self.draw(pos)
                self.pos = pos

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.canvas.setPos(pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

def sine_function(x):
    # Scale the sine wave to fit the canvas
    return 15 * math.sin(x / 5)

def plot_function(scribe, function, x_range):
    scribe.setDegrees(0)
    scribe.forward(1)  # Move to start plotting

    for x in range(x_range[0], x_range[1]):
        y = function(x)
        scribe.forward(int(y))

canvas = Canvas(60, 30)
scribe = TerminalScribe(canvas)

plot_function(scribe, sine_function, (0, 60))