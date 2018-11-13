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
        new_agent = physicalobject.PhysicalObject(  img=resources.clear_agent_image,
                                                    x=random.randint(0, 800),
                                                    y=random.randint(0, 600), 
                                                    batch=batch,
                                                )
        
        # Values we know will need to be set as it is initialized. 

        new_agent.rotation = random.randint(0, 360)
        new_agent.velocity_x = random.randint(-100, 100)
        new_agent.velocity_y = random.randint(-100, 100)

        agents.append(new_agent)

    return agents