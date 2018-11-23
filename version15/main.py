import pyglet, math, random, time
from game import resources, vector2, agent, name, common, graph
from pyglet.gl import *

game_window = pyglet.window.Window(common.window_width, common.window_height)
data_window = pyglet.window.Window(common.window_width, common.window_height)
text_window = pyglet.window.Window(common.window_width, common.window_height)

main_batch = pyglet.graphics.Batch()
fps_display = pyglet.clock.ClockDisplay()

result_tag = pyglet.text.Label()
index_tag = pyglet.text.Label()

result_sum = 50

result_graph = graph.Graph(200, 0, 20, 200)

def init_agents(num_agents, batch = None):
    """Initialize and load agents into a returned array"""
    agents = []
    for i in range(num_agents):
        random.seed(i)
        new_agent = agent.Agent(
            img = resources.white_agent_image,
            x = random.randint(0, common.window_width), # Random starting x
            y = random.randint(0, common.window_height), # Random starting y
            total_agent_count = num_agents,      # Total count (for internal calc.)
            batch=batch)
        new_agent.id = i
        agents.append(new_agent)
        common.agent_index.append("")
    return agents

agents = init_agents(common.agent_count, main_batch)

#
#
#

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    fps_display.draw()

    glColor3f(255, 0, 0)

    for i in agents:
        i.vlist.draw(GL_LINES)  # Draw velocity vector

@data_window.event
def on_draw():
    data_window.clear()

    result_graph.draw()

    for i in range(len(agents)):
        for j in range(i + 1, len(agents)):
            obj_1 = agents[i]
            obj_2 = agents[j]
            obj_1.neighbor_lines(obj_2)
            obj_1.neighbor_vlist.draw(GL_LINES)

    for agent in agents:
        index_tag = pyglet.text.Label(
            text=(
                "Bias: " + str(agent.bias) + '\n' +
                "Guess: " + str(agent.final_guess)),
            font_name = 'Arial',
            font_size = 10,
            x = agent.x, y=agent.y,
            multiline=True, width = 100,
            align = 'left')
        index_tag.draw()

    result_tag.draw()

@text_window.event
def on_draw():
    text_window.clear()
    fps_display.draw()

    index_tag = pyglet.text.Label(
        text = '\n'.join(common.agent_index),
        font_name = 'Courier New',
        font_size = 15,
        x = common.window_width / 2,
        y = common.window_height - 20,
        width = common.window_width - 20,
        multiline = True,
        align = 'center',
        anchor_x = 'center')
    index_tag.draw()

#
#
#

def update(dt):
    # Go through each agent's update loop
    for agent in agents:
        agent.update(dt)

    result_graph.update(dt, result_sum)

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

def roll(dt):
    """Make a random choice, and give agents respective feedback based on their response"""
    common.result = random.choice([-1,1])
    result_tag.text = str(common.result)

    for agent in agents:
        if agent.guess() == common.result:
            agent.feedback(True)
        else:
            agent.feedback(False)

    result_sum += common.result

def refresh_data(dt):
    for agent in agents:
        common.agent_index[agent.id] = ("".join(agent.name))

#
#
#

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.clock.schedule_interval(refresh_data, 1)
    pyglet.clock.schedule_interval(roll, 2)
    pyglet.app.run()