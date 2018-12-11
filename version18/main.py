import pyglet, math, random, time
pyglet.options['debug_gl'] = False
from game import resources, vector2, graph, util
from pyglet.gl import *

window_width, window_height = 900, 700

result = None

last_interaction = None

agent_count = 7
agent_index = []

implicit_window = pyglet.window.Window(window_width, window_height)
explicit_window = pyglet.window.Window(window_width, window_height)
stele_window = pyglet.window.Window(window_width, window_height)

main_batch = pyglet.graphics.Batch()
result_graph = graph.Graph(200, 0, 20, window_width)

result_sum = 300 # Half of the height, atm. Used for graph.
result_tag = pyglet.text.Label()

fps_display = pyglet.clock.ClockDisplay()

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

class Stele(object):

    def __init__(self):
        self.q_width = window_width / (agent_count + 1)
        self.q_height = window_height / (agent_count + 1)
        self.last_interaction = None

    def update(self):
        pass

    def draw(self):
        # if self.last_interaction != last_interaction:
        #     self.last_interaction = last_interaction
        stele_labels = pyglet.graphics.Batch()
        for x in range(0, agent_count + 1):

            if x != 0:
                # X label
                pyglet.text.Label(text=str(x),
                                            x = (x * self.q_width) + self.q_width/2,
                                            y = window_height - self.q_height/2,
                                            anchor_x='center',
                                            batch=stele_labels)
                # Y label
                pyglet.text.Label(text=str(x),
                                            x = self.q_width/2,
                                            y = window_height - ((x * self.q_height) + self.q_height/2),
                                            anchor_x='center',
                                            batch=stele_labels)

            for y in range(0, agent_count+1):
                pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                    ('v2f',
                           [x * self.q_width, y * self.q_height,
                            x * self.q_width, y * self.q_height + self.q_height,
                            x * self.q_width + self.q_width, y * self.q_height + self.q_height,
                            x * self.q_width + self.q_width, y * self.q_height
                    ]))

                if x != 0 and y != 0:
                    # index_tag.join(str(x) + " to " + str(y))
                    pyglet.text.Label(text=("index_tag"),
                                                    x = (x * self.q_width) + self.q_width/2,
                                                    y = window_height - ((y * self.q_height) + self.q_height/2),
                                                    anchor_x='center',
                                                    batch=stele_labels)

                if last_interaction == (x, y):
                    glColor3f(200,100,0)
                    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f',
                                                            [x * self.q_width, y * self.q_height,
                                                             x * self.q_width, y * self.q_height + self.q_height,
                                                             x * self.q_width + self.q_width, y * self.q_height + self.q_height,
                                                             x * self.q_width + self.q_width, y*self.q_height]
                                        ))
        stele_labels.draw()

stele = Stele()

class Agent(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.trade_tag = pyglet.text.Label()
        self.data_tag = pyglet.text.Label()

        self.total_agent_count = agent_count
        self.total_trades = 0
        self.interaction_timers = {}
        self.announce_timer = 0

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
        # Reset trade timer
        self.interaction_timers[other_agent.id] = 0
        last_interaction = (self.id, other_agent.id)
        print(last_interaction)

    #### Guessing
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

    def announce(self, text):
        self.announce_timer = 0

        pyglet.text.Label(
            text=(text),
            font_name = 'Arial',
            font_size = 6,
            x = self.x, y=self.y,
            multiline=True, width = 40,
            align='left').draw()


def init_agents(batch = None):
    """Initialize and load agents into a returned array"""
    agents = []
    for i in range(agent_count):
        random.seed(i)
        new_agent = Agent(
            img=resources.white_agent_image,
            x=random.randint(0, window_width),
            y=random.randint(0, window_height),
            batch=main_batch)
        new_agent.id = i
        agents.append(new_agent)
        agent_index.append("")
    return agents

agents = init_agents(main_batch)


@implicit_window.event
def on_draw():
    implicit_window.clear()
    main_batch.draw()
    fps_display.draw()

    for i in range(len(agents)):
        for j in range(i + 1, len(agents)):
            obj_1 = agents[i]
            obj_2 = agents[j]
            obj_1.neighbor_lines(obj_2)

    for agent in agents:
        glColor3f(255,0,0)
        agent.vlist.draw(GL_LINES)  # Draw velocity vector

    # for agent in agents:
    #     announce("Hello")

@explicit_window.event
def on_draw():
    explicit_window.clear()

    result_graph.draw()

    result_tag.draw()

@stele_window.event
def on_draw():
    stele_window.clear()

    stele.draw()


def roll(dt):
    """Make a random choice, and give agents respective feedback based on their response"""
    result = random.choice([-1,1])

    global result_sum
    result_sum += (result*2)
    result_tag.text = str(result)

    for agent in agents:
        if agent.guess() == result:
            agent.feedback(True)
        else:
            agent.feedback(False)

    result_graph.update(result_sum)

def update(dt):
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

def refresh_data(dt):
    pass

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.clock.schedule_interval(roll, 1)
    pyglet.app.run()