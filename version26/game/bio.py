import pyglet


def create_text(text, window_width, window_height):
    created_tag = pyglet.text.HTMLLabel(
    '<font face="Times New Roman" size="4">' + text + '<i>world</i></font>',
    x=window_width//2, y=window_height//2,
    anchor_x='center', anchor_y='center')

    return created_tag

