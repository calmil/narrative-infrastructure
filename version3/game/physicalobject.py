import pyglet, random, math
from . import util, vector2

# for my purposes, instead of super-ing this from a sprite, we'll want to do it from a polygon. 
class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self,
            *args,
            **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""
        self.speed = 0
        
    def update(self, dt):
        ###########MOVE 

        self.check_bounds()

    # will need to be rewritten for use with polygons.
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

    def interacts_with(self, other_agent):
        interaction_distance = self.image.width * 2 + other_agent.image.width * 2
        
        actual_distance = util.distance(self.position, other_agent.position)
        return (actual_distance <= interaction_distance)
        
    # Will need to change likely, perhaps to a cone of vision? 
    def handle_interaction_with(self, other_agent):
        """What occurs when two agents are within interaction range"""
        self.touch_count += math.ceil(1/60)