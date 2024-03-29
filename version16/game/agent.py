import pyglet, random, math
from . import util, vector2, name, common
from pyglet.gl import *

_ALGINMENT_RADIUS = 60
_COHESION_RADIUS = 50
_SEPARATION_RADIUS = 35

_ALIGNMENT_WEIGHT = 0.5
_COHESION_WEIGHT = 0.5
_SEPARATION_WEIGHT = 0.25

_WIGGLE_AMOUNT = 2

_SPEED_LIMIT = 40
_SPEED_MULTIPLIER = 1

_INTERACTION_RADIUS = 50

# Get rid of superclass
class Agent(pyglet.sprite.Sprite):

    def __init__(self, total_agent_count, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name.gen(4)

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
        self.v *= 5

        # List of vertices for drawing lines. Needs updating!
        self.vlist = pyglet.graphics.vertex_list(2,('v2f', [self.x, self.y,
                                                            self.x + self.v.x, self.y + self.v.y]))
        self.neighbor_vlist = pyglet.graphics.vertex_list(2,('v2f', [self.x, self.y,
                                                            self.x + self.v.x, self.y + self.v.y]))

        self.bias = random.choice([-0.5, 0.5])
        self.final_guess = None

        # Initialize all timers to 0
        for j in range(self.total_agent_count):
            self.interaction_timers[j] = 0

    def update(self, dt):
        # Check edges
        self.check_bounds()

       # Cap agent movement speed.
        if self.v.x > _SPEED_LIMIT:
            self.v.x -= 20
        if self.v.y > _SPEED_LIMIT:
            self.v.y -= 20

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

        # Increase interaction timers for all other agents
        for i in range(self.total_agent_count):
            self.interaction_timers[i] += 1

#### Movement
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

#### Detection / Interaction
    def neighbor_lines(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)
        glColor3f(255,255,0)
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
            self.v += self.compute_alignment(other_agent) * _ALIGNMENT_WEIGHT

        if actual_distance <= _COHESION_RADIUS:
            self.v += self.compute_cohesion(other_agent) * _COHESION_WEIGHT

        if actual_distance <= _SEPARATION_RADIUS:
            self.v += self.compute_separation(other_agent) * _SEPARATION_WEIGHT

        if actual_distance <= _INTERACTION_RADIUS:
            if self.interaction_timers[other_agent.id] > 50:
                self.trade(other_agent)
                if abs(other_agent.bias) > abs(self.bias):
                    if other_agent.bias < 0:
                        self.bias -= 1
                    elif other_agent.bias > 0:
                        self.bias += 1

    def trade(self, other_agent):
        # self.update_log(other_agent)
        self.total_trades += 1

        # Reset trade timer
        self.interaction_timers[other_agent.id] = 0

        # Trade chars of a random index.
        # self.random_index = random.randint(0,8)
        # self.name[self.random_index] = other_agent.name[self.random_index]

#### Trading
    def guess(self):
        self.final_guess = round(self.bias/100)

        if self.final_guess < -1:
            self.final_guess = -1
        elif self.final_guess > 1:
            self.final_guess = 1
        elif self.final_guess == 0:
            self.final_guess = random.choice([-1, 1])

        return self.final_guess

    def feedback(self, correct):
        if (correct and self.final_guess == -1) or (not correct and self.final_guess == 1):
            self.bias -= 1
        else:
            self.bias += 1