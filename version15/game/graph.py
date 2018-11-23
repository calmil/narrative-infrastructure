import pyglet, random
from pyglet.gl import *
from collections import deque

class Graph(object):

    def __init__(self, r, g, b, width):
        self.r = r
        self.g = g
        self.b = b
        self.width = width

        self.data_array = deque([])
        for i in range(self.width + 1):
            self.data_array.append(0)

    def update(self, dt, update_value):
        self.data_array.append(update_value)
        self.data_array.popleft()

    def draw(self):
        glColor3f(self.r, self.g, self.b)

        for i in range(self.width):
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                ('v2i', (i - 1, self.data_array[i - 1], i, self.data_array[i])))

# How you initialize a graph:
#   new_graph = Graph(200, 1, 200, 400)

# How you draw a graph:
#   new_graph.draw()

# How you update a graph:
#   new_graph.update(dt, random.randint(0,20))