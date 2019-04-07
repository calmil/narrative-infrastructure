import pyglet


def center_image(image):
    """Sets an image anchor point to center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

white = pyglet.resource.image("white.png")
center_image(white)

red = pyglet.resource.image("red.png")
center_image(red)

orange = pyglet.resource.image("orange.png")
center_image(orange)

yellow = pyglet.resource.image("yellow.png")
center_image(yellow)

green = pyglet.resource.image("green.png")
center_image(green)

blue = pyglet.resource.image("blue.png")
center_image(blue)

cyan = pyglet.resource.image("cyan.png")
center_image(cyan)

magenta = pyglet.resource.image("magenta.png")
center_image(magenta)
