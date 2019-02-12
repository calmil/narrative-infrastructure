from game import resources, vector2, util, agent_generation, group_generation, site_generation
from collections import deque
from pyglet.gl import *
import pyglet
import random

# ---- Init Sequence ----
agent_batch = pyglet.graphics.Batch()
narrative_batch = pyglet.graphics.Batch()

fps_display = pyglet.clock.ClockDisplay()

# ---- Debug Options ----
debug = True
grid = False

# -----------------------

pyglet.options['debug_gl'] = False

window_width, window_height = 800, 500

agent_count = 40
agent_index = []
agents = []

_ALGINMENT_RADIUS, _ALIGNMENT_WEIGHT = 60, 0.5
_COHESION_RADIUS, _COHESION_WEIGHT = 50, 0.5
_SEPARATION_RADIUS, _SEPARATION_WEIGHT = 35, 0.25
_WIGGLE_AMOUNT = 2
_SPEED_LIMIT = 20
_SPEED_MULTIPLIER = 0.5
_INTERACTION_INTERVAL = 10
_INTERACTION_RADIUS = 50


class Narrative(object):
    """Main Narrative visualization, charting interactions between implicit actors. """

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        narrative_batch.draw()


class Agent(pyglet.sprite.Sprite):
    """Main Agent class, which is capable of executing set behaviors"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calculation
        self.total_agent_count = agent_count
        self.total_trades = 0
        self.interaction_timers = {}
        self.announce_timer = 0

        # Nature
        self.nature, self.alignment_weight, self.cohesion_weight, self.separation_weight = agent_generation.get_nature()

        # Movement
        self.alignment_weight /= _ALIGNMENT_WEIGHT
        self.cohesion_weight /= _COHESION_WEIGHT
        self.separation_weight /= _SEPARATION_WEIGHT

        self.velocity_x = random.randint(-50, 50)
        self.velocity_y = random.randint(-50, 50)
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)
        self.v.normalise()
        self.v *= 2

        # List of vertices for drawing lines. Needs updating!
        self.vlist = pyglet.graphics.vertex_list(2,
                                                 ('v2f',
                                                  [self.x,
                                                   self.y,
                                                   self.x + self.v.x,
                                                   self.y + self.v.y]))

        self.neighbor_vlist = pyglet.graphics.vertex_list(2,
                                                          ('v2f',
                                                           [self.x,
                                                            self.y,
                                                            self.x+self.v.x,
                                                            self.y+self.v.y]))

        # Initialize all timers to 0
        for j in range(self.total_agent_count):
            self.interaction_timers[j] = 0

    def update(self, dt):

        # Check edges of window
        self.check_bounds()

        # Cap agent movement speed.
        if abs(self.v.x) > _SPEED_LIMIT:
            self.v.x *= 0.90
        if abs(self.v.y) > _SPEED_LIMIT:
            self.v.y *= 0.90

        # Calculate wiggle.
        self.random_offset = vector2.Vector2(random.randint(_WIGGLE_AMOUNT / 2 * -1, _WIGGLE_AMOUNT / 2),
                                             random.randint(_WIGGLE_AMOUNT / 2 * -1, _WIGGLE_AMOUNT / 2))
        self.v += self.random_offset

        # Draw momentum vector
        self.vlist = pyglet.graphics.vertex_list(2, ('v2f', [self.x,
                                                             self.y,
                                                             self.x + self.v.x,
                                                             self.y + self.v.y])
                                                 )

        # Actual movement.
        self.x += self.v.x * dt
        self.y += self.v.y * dt

        # Increase interaction timers for all other agents
        for i in range(self.total_agent_count):
            self.interaction_timers[i] += 1

    # Movement

    def check_bounds(self):
        """Checks the object's edges against the edges of the window."""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = window_width + self.image.width / 2
        max_y = window_height + self.image.width / 2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def compute_alignment(self, other_agent):
        # Alignment vector will be the sum of the two
        alignment_vector = vector2.Vector2(self.velocity_x + other_agent.velocity_x,
                                           self.velocity_y + other_agent.velocity_y)
        alignment_vector.normalise()
        return alignment_vector

    def compute_cohesion(self, other_agent):
        # Cohesion vector is the force of grouping.
        cohesion_vector = vector2.Vector2(self.x + other_agent.x,
                                          self.y + other_agent.y)
        cohesion_vector.x /= 2
        cohesion_vector.y /= 2
        cohesion_vector.normalize()
        return cohesion_vector

    def compute_separation(self, other_agent):
        # Separation is repelling force
        separation_vector = vector2.Vector2(other_agent.x - self.x,
                                            other_agent.y - self.y)

        separation_vector *= -1
        return separation_vector

    def compute_wiggle(self):
        wiggle_vector = vector2.Vector2(random.randint(_WIGGLE_AMOUNT/2 * -1,
                                                       _WIGGLE_AMOUNT/2),
                                        random.randint(_WIGGLE_AMOUNT/2 * -1,
                                                       _WIGGLE_AMOUNT/2))
        return wiggle_vector

    # Detection / Interaction
    def neighbor_lines(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)
        glColor3f((4/actual_distance)*3, (4/actual_distance)
                  * 3, (4/actual_distance)*3)

        if actual_distance <= _INTERACTION_RADIUS:
            self.neighbor_vlist = pyglet.graphics.vertex_list(2, ('v2f', [
                self.x,
                self.y,
                other_agent.x,
                other_agent.y]))
            self.neighbor_vlist.draw(GL_LINES)

    def interacts_with(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)

        if actual_distance <= _ALGINMENT_RADIUS:
            self.v += self.compute_alignment(other_agent) * \
                self.alignment_weight
        if actual_distance <= _COHESION_RADIUS:
            self.v += self.compute_cohesion(other_agent) * self.cohesion_weight
        if actual_distance <= _SEPARATION_RADIUS:
            self.v += self.compute_separation(other_agent) * \
                self.separation_weight

        if actual_distance <= _INTERACTION_RADIUS:
            if self.interaction_timers[other_agent.id] > _INTERACTION_INTERVAL:
                self.trade(other_agent)

    def trade(self, other_agent):
        self.interaction_timers[other_agent.id] = 0


# ----------HELP
# class Graph(object):
#     """Generates a graph of a set width, which can be updated. """

#     def __init__(self):
#         self.graph_batch = pyglet.graphics.Batch()

#     def update(self, update_value):

#     def draw(self):
#         self.graph_batch.draw()
# ------------------


class Application():
    """Main application run class. """

    def setup(self):
        """Initialize agents"""
        for i in range(agent_count):
            random.seed(i)
            new_agent = Agent(
                img=resources.white_agent_image,
                x=random.randint(0, window_width),
                y=random.randint(0, window_height),
                batch=agent_batch)
            new_agent.id = i
            agents.append(new_agent)
            agent_index.append("")

    def update(self, dt):
        # Go through each agent's update loop
        for agent in agents:
            agent.update(dt)

        # Iterate through all object pairs to check for detection
        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                obj_1 = agents[i]
                obj_2 = agents[j]
                obj_1.interacts_with(obj_2)
                obj_2.interacts_with(obj_1)


narrative = Narrative()
# graph = Graph()


def main():
    """
    Main loop. Windows are set up, and updates are called.
    """

    app = Application()
    app.setup()

    display = pyglet.window.get_platform().get_default_display()

    if debug is True:
        implicit_window = pyglet.window.Window(
            window_width, window_height, vsync=False)
        explicit_window = pyglet.window.Window(
            window_width, window_height, vsync=False)
        narrative_window = pyglet.window.Window(
            window_width, window_height, vsync=False)
    else:
        screen_1 = display.get_screens()[0]
        screen_2 = display.get_screens()[1]
        screen_3 = display.get_screens()[2]

        implicit_window = pyglet.window.Window(
            fullscreen=True, screen=screen_1, vsync=False)
        explicit_window = pyglet.window.Window(
            fullscreen=True, screen=screen_2, vsync=False)
        narrative_window = pyglet.window.Window(
            fullscreen=True, screen=screen_3, vsync=False)

    @implicit_window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        implicit_window.clear()
        agent_batch.draw()
        fps_display.draw()

        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                obj_1 = agents[i]
                obj_2 = agents[j]
                obj_1.neighbor_lines(obj_2)

        for agent in agents:
            glColor3f(255, 0, 0)
            agent.vlist.draw(GL_LINES)  # Draw velocity vector

    # @explicit_window.event
    # def on_draw():
    #     glClear(GL_COLOR_BUFFER_BIT)
    #     graph.draw()

    @narrative_window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        narrative_window.clear()
        narrative.draw()

    pyglet.clock.schedule_interval(app.update, 1 / 60.0)
    # pyglet.clock.schedule_interval(narrative.paint, 1)

    pyglet.app.run()


main()
