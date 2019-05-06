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


interaction_image = pyglet.resource.image("interaction_sprite.png")
interaction_seq = pyglet.image.ImageGrid(interaction_image, 1, 16, item_width=100, item_height=100)
interaction_anim =  pyglet.image.Animation.from_image_sequence(interaction_seq[0:], 0.04, loop=False)

symbolic_image = pyglet.resource.image("symbolic_sprite.png")
symbolic_seq = pyglet.image.ImageGrid(symbolic_image, 1, 16, item_width=100, item_height=100)
symbolic_anim =  pyglet.image.Animation.from_image_sequence(symbolic_seq[0:], 0.1, loop=False)