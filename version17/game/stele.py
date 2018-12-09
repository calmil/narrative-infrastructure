import pyglet, random
from . import common
from pyglet.gl import *
from collections import deque

class Stele(object):

    def __init__(self):
        self.q_width = common.window_width / common.agent_count - 1
        self.q_height = common.window_height / common.agent_count
        self.color = 255 / common.agent_count

        # List of vertices for stele
    def update(self):
        pass

    def draw(self):
        for x in range(0, common.agent_count):
            for y in range(0, common.agent_count):
                pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                    ('v2f',
                       [x * self.q_width, y * self.q_height,
                        x * self.q_width, y * self.q_height + self.q_height,
                        x * self.q_width + self.q_width, y * self.q_height + self.q_height,
                        x * self.q_width + self.q_width, y * self.q_height]))