import pyglet, random
from pyglet.gl import *
from collections import deque

window = pyglet.window.Window(400,200)

class Graph(object):

    def __init__(self, r, g, b, width):
        self.r = r
        self.g = g
        self.b = b
        self.width = width

        self.data_array = deque([])
        for i in range(self.width):
            self.data_array.append(0)

    def update(self, dt, update_value):
        self.data_array.append(update_value)
        self.data_array.popleft()

    def draw_graph(self):
        glColor3f(self.r, self.g, self.b)

        for i in range((400)):
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                ('v2i', (i - 1, self.data_array[i - 1], i, self.data_array[i])))

new_graph = Graph(200, 1, 200, 400)

@window.event
def on_draw():
    window.clear()

    new_graph.draw_graph()

def update(dt):
    new_graph.update(dt, random.randint(0,20))

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/30)
    pyglet.app.run()