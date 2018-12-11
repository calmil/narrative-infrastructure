import pyglet, random
from . import common
from pyglet.gl import *
from collections import deque

class Stele(object):

    def __init__(self):
        self.q_width = common.window_width / (common.agent_count + 1)
        self.q_height = common.window_height / (common.agent_count + 1)
        self.last_interaction = None

    def update(self):
        pass

    def draw(self):
        # if self.last_interaction != common.last_interaction:
        #     self.last_interaction = common.last_interaction
        stele_labels = pyglet.graphics.Batch()
        for x in range(0, common.agent_count + 1):

            if x != 0:
                # X label
                pyglet.text.Label(text=str(x),
                                            x = (x * self.q_width) + self.q_width/2,
                                            y = common.window_height - self.q_height/2,
                                            anchor_x='center',
                                            batch=stele_labels)
                # Y label
                pyglet.text.Label(text=str(x),
                                            x = self.q_width/2,
                                            y = common.window_height - ((x * self.q_height) + self.q_height/2),
                                            anchor_x='center',
                                            batch=stele_labels)

            for y in range(0, common.agent_count+1):
                pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                    ('v2f',
                           [x * self.q_width, y * self.q_height,
                            x * self.q_width, y * self.q_height + self.q_height,
                            x * self.q_width + self.q_width, y * self.q_height + self.q_height,
                            x * self.q_width + self.q_width, y * self.q_height
                    ]))

                if x != 0 and y != 0:
                    pyglet.text.Label(text=(str(x) + " to " + str(y)),
                                                    x = (x * self.q_width) + self.q_width/2,
                                                    y = common.window_height - ((y * self.q_height) + self.q_height/2),
                                                    anchor_x='center',
                                                    batch=stele_labels)

                if common.last_interaction == (x, y):
                    glColor3f(200,100,0)
                    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f',
                                                            [x * self.q_width, y * self.q_height,
                                                             x * self.q_width, y * self.q_height + self.q_height,
                                                             x * self.q_width + self.q_width, y * self.q_height + self.q_height,
                                                             x*self.q_width + self.q_width, y*self.q_height]
                                        ))
        stele_labels.draw()
