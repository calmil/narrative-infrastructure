import pyglet, random, math
from . import util, vector2, name

_INFLUENCE_RADIUS = 0.75

_ALIGNMENT_WEIGHT = 30
_COHESION_WEIGHT = 20
_SEPARATION_WEIGHT = 0.2

_SPEED_MULTIPLIER = 1


# for my purposes, instead of super-ing this from a sprite, we'll want to do it from a polygon. 
class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name.gen(4)

        # initial velocities.
        self.velocity_x = random.randint(-100, 100)
        self.velocity_y = random.randint(-100, 100)

        # create movement vector based off of the values set above
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)

        # Initialize name tag and data tag
        # self.name_tag = pyglet.text.Label(text=str(self.name))
        # self.data_tag = pyglet.text.Label()

        self.v.normalise()
        self.v *= 10

    def update(self, dt):
        self.check_bounds()

        # Update name tag position. 

        # self.name_tag = pyglet.text.Label(  text=str(self.name),
        #                                     x=self.x,
        #                                     y=self.y + 40,
        #                                     anchor_x='center')

        # self.data_tag = pyglet.text.Label(  text=str(self.v_normalised_str),
        #                                     x=self.x + 50,
        #                                     y=self.y + 60,
        #                                     anchor_x='center')
        self.x += self.v.x * dt
        self.y += self.v.y * dt

    # Called less often, when we need to save processing power.
    def update_move(self, dt):
        pass

    #! Remember to update with different window sizes
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

    #! Compute alignment between the two agents
    def compute_alignment(self, other_agent):
        alignment_vector = vector2.Vector2( self.velocity_x + other_agent.velocity_x,
                                            self.velocity_y + other_agent.velocity_y)

        alignment_vector.normalise()
        return alignment_vector


    def compute_cohesion(self, other_agent):
        # Average the two positions
        cohesion_vector = vector2.Vector2(self.x + other_agent.x, self.y + other_agent.y)

        cohesion_vector.x /= 2
        cohesion_vector.y /= 2 
        cohesion_vector.normalize()
        return cohesion_vector

    def compute_separation(self, other_agent):
        # 
        separation_vector = vector2.Vector2(other_agent.x - self.x, other_agent.y - self.y)

        separation_vector *= -1
        return separation_vector


    #! Will need to change likely, perhaps to a cone of vision? 
    def interacts_with(self, other_agent):
        # detection/interaction distance
        interaction_distance = self.image.width * _INFLUENCE_RADIUS + other_agent.image.width * _INFLUENCE_RADIUS
        
        actual_distance = util.distance(self.position, other_agent.position)
        return (actual_distance <= interaction_distance)

    def handle_interaction_with(self, other_agent):
        """What occurs when two agents are within interaction range"""
        
        # modify the movement vector based on our computed modifiers 
        self.v.normalise()
        self.v += self.compute_alignment(other_agent) * _ALIGNMENT_WEIGHT
        self.v += self.compute_cohesion(other_agent) * _COHESION_WEIGHT
        self.v += self.compute_separation(other_agent) * _SEPARATION_WEIGHT
        self.v *= _SPEED_MULTIPLIER






    # def name_eval(self, other_agent):
    #     """Evaluate the two name-strings"""
    #     pass