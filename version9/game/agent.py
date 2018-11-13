import pyglet, random, math
from . import util, vector2, name, common, data
from pyglet.gl import *

_ALGINMENT_RADIUS = 1
_COHESION_RADIUS = 1
_SEPARATION_RADIUS = 0.8

_ALIGNMENT_WEIGHT = 1
_COHESION_WEIGHT = 0.5
_SEPARATION_WEIGHT = 0.5

_WIGGLE_AMOUNT = 2

_SPEED_LIMIT = 30
_SPEED_MULTIPLIER = 1

# Will soon have to break up the agent class to only handle movement behavior rather than the entire
# business of trading data. This is getting tricky lol.

agent_batch = pyglet.graphics.Batch()

# for my purposes, instead of super-ing this from a sprite, we'll want to do it from a polygon.
class Agent(pyglet.sprite.Sprite):

    def __init__(self, total_agent_count, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name.gen(4)
        # self.name_tag = pyglet.text.Label(text=str(self.name))

        self.trade_tag = pyglet.text.Label()
        self.data_tag = pyglet.text.Label()

        self.total_agent_count = total_agent_count
        self.total_trades = 0
        self.interaction_timers = {}

        # Give a random heading, normalise, and scale by 10.
        self.velocity_x = random.randint(-100, 100)
        self.velocity_y = random.randint(-100, 100)
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)
        self.v.normalise()
        self.v *= 10

        # List of vertices for drawing line. Needs updating!
        self.vlist = pyglet.graphics.vertex_list(2,('v2f', [self.x, self.y,
                                                            self.x + self.v.x, self.y + self.v.y]))

        # Initialize all timers to 0
        for j in range(self.total_agent_count):
            self.interaction_timers[j] = 0


    def update(self, dt):
        # Check edges
        self.check_bounds()

        # Cap agent movement speed.
        if self.v.x > _SPEED_LIMIT:
            self.v.x = _SPEED_LIMIT
        if self.v.y > _SPEED_LIMIT:
            self.v.y = _SPEED_LIMIT

        # Movement calculations.
        self.x += self.v.x * dt
        self.y += self.v.y * dt

        # Calculate wiggle.
        self.random_offset = vector2.Vector2(random.randint(_WIGGLE_AMOUNT / 2 * -1, _WIGGLE_AMOUNT / 2),
                                             random.randint(_WIGGLE_AMOUNT / 2 * -1, _WIGGLE_AMOUNT / 2))
        self.v += self.random_offset

        # Draw momentum vector
        self.vlist = pyglet.graphics.vertex_list(2, ('v2f', [   self.x,
                                                                self.y,
                                                                self.x + self.v.x,
                                                                self.y + self.v.y]
                                                            ))

        # Display dynamic data
        self.data_tag = pyglet.text.Label( text=str(self.id),
                                            x=self.x,
                                            y=self.y,
                                            anchor_x='center')

        # Internal data calculations
        # Increase interaction timers for all other agents
        for i in range(self.total_agent_count):
            self.interaction_timers[i] += 1


    def check_bounds(self):
        """Checks the object's edges against the edges of the window."""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = common.window_width + self.image.width / 2
        max_y = common.window_height + self.image.width / 2

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
        alignment_vector = vector2.Vector2( self.velocity_x + other_agent.velocity_x,
                                            self.velocity_y + other_agent.velocity_y)
        alignment_vector.normalise()
        return alignment_vector

    def compute_cohesion(self, other_agent):
        cohesion_vector = vector2.Vector2(self.x + other_agent.x, self.y + other_agent.y)

        cohesion_vector.x /= 2
        cohesion_vector.y /= 2

        cohesion_vector.normalize()
        return cohesion_vector

    def compute_separation(self, other_agent):
        separation_vector = vector2.Vector2(other_agent.x - self.x, other_agent.y - self.y)

        separation_vector *= -1
        return separation_vector

    def compute_wiggle(self):
        wiggle_vector = vector2.Vector2(random.randint(_WIGGLE_AMOUNT / 2 * -1, _WIGGLE_AMOUNT / 2),
                                        random.randint(_WIGGLE_AMOUNT / 2* -1, _WIGGLE_AMOUNT / 2))
        return wiggle_vector


    def interacts_with(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)

        if actual_distance <= self.image.width * _ALGINMENT_RADIUS:
            self.v += self.compute_alignment(other_agent) * _ALIGNMENT_WEIGHT

        if actual_distance <= self.image.width * _COHESION_RADIUS:
            self.v += self.compute_cohesion(other_agent) * _COHESION_WEIGHT

        if actual_distance <= self.image.width * _SEPARATION_RADIUS:
            self.v += self.compute_separation(other_agent) * _SEPARATION_WEIGHT
            if self.interaction_timers[other_agent.id] > 50:
                self.trade(other_agent)

    def trade(self, other_agent):
        self.update_log(other_agent)
        self.total_trades += 1
        self.interaction_timers[other_agent.id] = 0

        # self.name[4] = other_agent.name[4]

        self.trade_record = str(self.name) + " and " + str(other_agent.name)

        # self.trade_tag = pyglet.text.Label( text=self.trade_record,
        #                             x=self.x,
        #                             y=self.y,
        #                             anchor_x='left')

    def update_log(self, other_agent):
        data.trade_history.insert(0, str(self.name) + " and " + str(other_agent.name))
        data.trade_history.pop()