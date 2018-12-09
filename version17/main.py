import pyglet, math, random, time
from game import resources, vector2, agent, name, common, graph, stele
from pyglet.gl import *
#----------------------------------- WINDOWS -----------------------------------#
implicit_window = pyglet.window.Window(common.window_width, common.window_height)
explicit_window = pyglet.window.Window(common.window_width, common.window_height)
stele_window = pyglet.window.Window(common.window_width, common.window_height)
#----------------------------------- GRAPHICS ----------------------------------#
main_batch = pyglet.graphics.Batch()
result_graph = graph.Graph(200, 0, 20, common.window_width)
stele = stele.Stele()
#----------------------------------- BETTING ----------------------------------#
result_sum = 300 # Half of the height, atm. Used for graph.
result_tag = pyglet.text.Label()
#----------------------------------- DEBUG ------------------------------------#
fps_display = pyglet.clock.ClockDisplay()


def init_agents(batch = None):
    """Initialize and load agents into a returned array"""
    agents = []
    for i in range(common.agent_count):
        random.seed(i)
        new_agent = agent.Agent(
            img=resources.white_agent_image,
            x=random.randint(0, common.window_width),
            y=random.randint(0, common.window_height),
            batch=batch)
        new_agent.id = i
        agents.append(new_agent)
        common.agent_index.append("")
    return agents

agents = init_agents(main_batch)

#
#
#

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

    for agent in agents:
        agent.announce("Hello")

@explicit_window.event
def on_draw():
    explicit_window.clear()

    result_graph.draw()

    result_tag.draw()

@stele_window.event
def on_draw():
    stele_window.clear()

    stele.draw()

#
#
#

def roll(dt):
    """Make a random choice, and give agents respective feedback based on their response"""
    common.result = random.choice([-1,1])

    global result_sum
    result_sum += (common.result*2)
    result_tag.text = str(common.result)

    for agent in agents:
        if agent.guess() == common.result:
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

#
#
#

def refresh_data(dt):
    pass

#
#
#

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.clock.schedule_interval(refresh_data, 1)
    pyglet.clock.schedule_interval(roll, 1)
    pyglet.app.run()