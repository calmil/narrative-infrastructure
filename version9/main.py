import pyglet, math, random
from game import resources, vector2, agent, name, common, data
from pyglet.gl import *

game_window = pyglet.window.Window(common.window_width, common.window_height)
data_window = pyglet.window.Window(common.window_width, common.window_height)
text_window = pyglet.window.Window(common.window_width, common.window_height)

main_batch = pyglet.graphics.Batch()

#### LOAD OPERATIONS

def init_agents(num_agents, batch=None):
    """Initialize and load agents into a returned array"""
    agents = []

    for i in range(num_agents):
        new_agent = agent.Agent(img=resources.white_agent_image,
                                x=random.randint(0, common.window_width), # Random starting x
                                y=random.randint(0, common.window_height),# Random starting y
                                total_agent_count=num_agents,      # Total count (for internal calc.)
                                batch=batch)
        agents.append(new_agent)
        new_agent.id = i

    return agents

agents = init_agents(common.agent_count, main_batch)

for agent in agents:
    data.agent_index.append(str(agent.id) + " " + agent.name)


#### DRAWING / UPDATE OPERATIONS

# When drawing needs to happen.
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

    glColor3f(255, 0, 0)

    for i in agents:
        i.vlist.draw(GL_LINES)
        i.vlist.draw(GL_TRIANGLES)

@data_window.event
def on_draw():
    data_window.clear()

    for i in agents:
        i.vlist.draw(GL_LINES)
        i.data_tag.draw()

@text_window.event
def on_draw():
    text_window.clear()

    for i in agents:
        i.trade_tag.draw()
        # i.data_tag.draw()


# When data updates need to happen
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
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()