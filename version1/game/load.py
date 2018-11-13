import pyglet
import random
import math
from . import resources

def agents(num_agents):
    agents = []
    for i in range(num_agents):
        agent_x = random.randint(0, 800)
        agent_y = random.randint(0, 800)
        new_agent = agent = pyglet.sprite.Sprite(img=resources.agent_image,x=400, y=300)
        new_agent.rotation = random.randint(0, 360)
        agents.append(new_agent)
    return agents

    
    