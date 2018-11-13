import pyglet

def center_image(image):
    """Sets an image anchor point to center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

clear_agent_image = pyglet.resource.image("clear_agent.png")
center_image(clear_agent_image)

agent_image = pyglet.resource.image("agent.png")
center_image(agent_image)

object_image = pyglet.resource.image("object.png")
center_image(object_image)