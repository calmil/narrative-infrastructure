import pyglet, random, math
from . import util, vector2, name

# for my purposes, instead of super-ing this from a sprite, we'll want to do it from a polygon. 
class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Values we know will be changed later, that we can temporarily set.
        self.name = name.gen(4)
        self.velocity_x = random.randint(-100, 100)
        self.velocity_y = random.randint(-100, 100)
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)

        # Initialize name tag
        self.name_tag = pyglet.text.Label(text=str(self.name))
        self.data_tag = pyglet.text.Label()

    def update(self, dt):
        self.compute_alignment()
        #! ##########MOVE 
        # Update name tag position. 
        self.name_tag = pyglet.text.Label(  text=str(self.name),
                                            x=self.x,
                                            y=self.y + 40,
                                            anchor_x='center')

        # self.data_tag = pyglet.text.Label(  text=str(self.v_normalised_str),
        #                                     x=self.x + 50,
        #                                     y=self.y + 60,
        #                                     anchor_x='center')

        # Movement
        self.x += math.ceil((self.v_normalised.x * 40) * dt)
        self.y += math.ceil((self.v_normalised.y * 40) * dt)

    def update_move(self, dt):
        self.check_bounds()


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

    #! 
    def compute_alignment(self):
        self.v_normalised = self.v.normalise()
        
        self.v_normalised_str = str(self.v_normalised.x) + ", " + str(self.v_normalised.y)
    
    def compute_cohesion(self, other_agent):
            self.v.x += other_agent.v.x
            self.v.y += other_agent.v.y
            self.v.x /= 2
            self.v.y /= 2

    #! Will need to change likely, perhaps to a cone of vision? 
    def interacts_with(self, other_agent):
        # detection/interaction distance
        interaction_distance = self.image.width * 1.2 + other_agent.image.width * 1.2
        
        # distance with all other agents
        actual_distance = util.distance(self.position, other_agent.position)
        return (actual_distance <= interaction_distance)

    def handle_interaction_with(self, other_agent):
        """What occurs when two agents are within interaction range"""
        self.v_normalised.x = self.v_normalised.x + other_agent.v_normalised.x
        self.v_normalised.y = self.v_normalised.y + other_agent.v_normalised.y
        
        self.compute_cohesion(other_agent)





    def name_eval(self, other_agent):
        """Evaluate the two name-strings"""
        pass