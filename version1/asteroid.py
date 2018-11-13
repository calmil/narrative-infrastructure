import pyglet
import math
from game import resources, load

# initialize window
game_window = pyglet.window.Window()

world_label = pyglet.text.Label(text="World", x=400, y=575, anchor_x='center')

agents = load.agents(3)

def distance(point_1=(0, 0), point_2=(0, 0)):
    """Return the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0])** 2 + (point_1[1] - point_2[1])** 2)

# this decorator lets the game_window instance know that
#   'on_draw()' is an event handler, being fired
#   whenever the window needs to be redrawn.
@game_window.event
def on_draw():
    game_window.clear()

    world_label.draw()
    for agent in agents:
        agent.draw()

if __name__ == '__main__':
    pyglet.app.run()