import pyglet, random, math
from . import resources, physicalobject, name

# where we initialize all our agents
# for future reference, starting information should not be random.
# like the stock market, it's not random, just inscrutably intricate.
def agents(num_agents, batch=None):
    """Initialize and load agents into an array"""
    agents = []

    # initializing loop
    for i in range(num_agents):
        agent_x = random.randint(0, 800)
        agent_y = random.randint(0, 800)

        new_agent = physicalobject.PhysicalObject(img=resources.agent_image,x=400, y=300, batch=batch)
        
        new_agent.name = name.gen(2)
        new_agent.rotation = random.randint(0, 360)
        new_agent.location = Vector2(randint(0, w), randint(0, h))

        agents.append(new_agent)

    return agents