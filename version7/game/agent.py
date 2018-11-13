import pyglet, random, math
from . import util, vector2, name
from pyglet.gl import *

_ALGINMENT_RADIUS = 1
_COHESION_RADIUS = 1
_SEPARATION_RADIUS = 1

_ALIGNMENT_WEIGHT = 0.25
_COHESION_WEIGHT = 0.25
_SEPARATION_WEIGHT = 0.5

_SPEED_MULTIPLIER = 1


agent_batch = pyglet.graphics.Batch()


#### MAKE THEM TRADE DATA TODAY ! ! ! ! ! 

# for my purposes, instead of super-ing this from a sprite, we'll want to do it from a polygon. 
class Agent(pyglet.sprite.Sprite):

    def __init__(self, total_agent_count, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.name = name.gen(4)
        # self.name_tag = pyglet.text.Label(text=str(self.name))
        self.trade_tag = pyglet.text.Label()
        self.data_tag = pyglet.text.Label()
        

        self.total_agent_count = total_agent_count
        self.interaction_history = []
        self.interaction_timers = {}

        self.velocity_x = random.randint(-100, 100)
        self.velocity_y = random.randint(-100, 100)
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)
        self.v.normalise()
        self.v *= 10

        self.vlist = pyglet.graphics.vertex_list(3, ('v2f',[self.x, self.y,
                                                            self.x - 20, self.y - 40,
                                                            self.x + 20, self.y - 40]
                                                            ))
        
        for j in range(self.total_agent_count):
            self.interaction_timers[j] = 0



    def update(self, dt):
        self.vlist = pyglet.graphics.vertex_list(2, ('v2f', [   self.x,
                                                                self.y,
                                                                self.x + self.v.x,
                                                                self.y + self.v.y]
                                                            ))

        # self.data_tag = pyglet.text.Label(  text=str(self.interaction_timers),
        #                                     x=50,
        #                                     y=60,
        #                                     anchor_x='left')

        # Check edges
        self.check_bounds()

        # Movement
        self.x += self.v.x * dt
        self.y += self.v.y * dt

        # I don't need to use specific id here, as it doesn't matter,
        # the counter for each individual is always going up regardless.
        for i in range(self.total_agent_count):
            self.interaction_timers[i] += 1

    def check_bounds(self):
        """Checks the object's edges against the edges of the window."""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.width / 2

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

    def interacts_with(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)

        if actual_distance <= self.image.width * _ALGINMENT_RADIUS:
            self.v += self.compute_alignment(other_agent) * _ALIGNMENT_WEIGHT

        if actual_distance <= self.image.width * _COHESION_RADIUS:
            self.v += self.compute_cohesion(other_agent) * _COHESION_WEIGHT

        if actual_distance <= self.image.width * _SEPARATION_RADIUS:
            self.v += self.compute_separation(other_agent) * _SEPARATION_WEIGHT
            if self.interaction_timers[other_agent.id] > 100:
                self.trade(other_agent)

    def trade(self, other_agent):
        self.trade_tag = pyglet.text.Label(  text=str(self.id) + " and " + str(other_agent.id),
                                            x=self.x,
                                            y=self.y,
                                            anchor_x='left')

        self.interaction_timers[other_agent.id] = 0
        