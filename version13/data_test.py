import pyglet, math, random, time
from game import resources, vector2, agent, name, common, data
from pyglet.gl import *

data_window = pyglet.window.Window(common.window_width, common.window_height)

main_batch = pyglet.graphics.Batch()

result_tag = pyglet.text.Label()
index_tag = pyglet.text.Label()

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
        data.agent_index.append("")

    return agents

agents = init_agents(common.agent_count, main_batch)

result_tag = pyglet.text.Label(
    text="hello",
    font_size=40,
    x=common.window_width/2,
    y=common.window_height/2)

random.seed()

@data_window.event
def on_draw():
    data_window.clear()

    for i in range(len(agents)):
        for j in range(i + 1, len(agents)):
            obj_1 = agents[i]
            obj_2 = agents[j]

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

def roll(dt):
    common.result = random.choice([-1,1])
    result_tag.text = str(common.result)

    for agent in agents:
        if agent.guess() == common.result:
            agent.feedback(True)
        else:
            agent.feedback(False)


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


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.clock.schedule_interval(roll, 2)
    pyglet.app.run()