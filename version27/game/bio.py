import pyglet

def create_text(text, window_width, window_height):
    pass

class Biography():
    """Creates a dynamic biography from an agent."""

    def __init__(self, obj, batch, window_width, window_height, *args, **kwargs):

        self.title_tag = pyglet.text.Label(str(obj.title),
                     font_name='courier',
                     font_size=30,
                     color=(255,255,255,255),
                     x=30,
                     y=window_height-20,
                     width=200,
                     anchor_x='left', anchor_y='center',
                     batch=batch)

        self.nature_tag = pyglet.text.Label(str(obj.nature),
                     font_name='courier',
                     font_size=12,
                     color=(255,255,255,255),
                     x=30,
                     y=600//2,
                     width=200,
                     anchor_x='left', anchor_y='center',
                     batch=batch)

    def draw(self):

        self.nature_tag.draw()
        self.title_tag.draw()

    # return created_tag

