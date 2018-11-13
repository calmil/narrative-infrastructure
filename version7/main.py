import pyglet, math, random
from game import resources, vector2, agent, name
from pyglet.gl import *

###########################################
#############VERSION7######################
# No load file now, trying to consolidate #
# most of the structure in 'main' other   #
# than the agents, utilities, and vectors.#
###########################################

window_width, window_height = 800, 600
game_window = pyglet.window.Window(window_width, window_height)

main_batch = pyglet.graphics.Batch()


def init_agents(num_agents, batch=None):
    """Initialize and load agents into a returned array"""
    agents = []

    for i in range(num_agents):
        new_agent = agent.Agent(img=resources.white_agent_image,
                                x=random.randint(0, 800),
                                y=random.randint(0, 600),
                                total_agent_count=num_agents,
                                batch=batch)
        agents.append(new_agent)
        new_agent.id = i

    return agents

agents = init_agents(40, main_batch)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    
    glColor3f(255,0,0)
    for agent in agents:
        agent.vlist.draw(GL_LINES)
        agent.vlist.draw(GL_TRIANGLES)
        agent.trade_tag.draw()

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