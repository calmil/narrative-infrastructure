import pyglet
from game import resources

title_x = 30
title_y = 30

bio_x = 0
bio_y = 0

history_x = 300
history_y = 300

def create_text(text, window_width, window_height):
    pass


class Biography():
    """Creates a dynamic biography from an agent."""

    def __init__(self, obj, batch, window_width, window_height):

        self.obj = obj
        self.batch = batch

        self.title_tag = pyglet.text.Label(
                str(obj.title),
                font_name='Bangla MN',
                font_size=30,
                color=(255, 255, 255, 255),
                x=title_x,
                y=window_height - title_y,
                width=200,
                anchor_x='left', anchor_y='center',
                batch=batch
                )

        self.nature_tag = pyglet.text.Label(
                str(
                        obj.nature[0] + '\n' +
                        obj.nature[1] + '\n' +
                        obj.nature[2] + '\n' +
                        obj.nature[3] + '\n' +
                        obj.nature[4] + '\n' +
                        obj.nature[5] + '\n'
                    ),
                multiline=True,
                font_name='Helvetica',
                font_size=12,
                color=(255, 255, 255, 255),
                x=30,
                y=600//2,
                width=200,
                anchor_x='left', anchor_y='center',
                batch=batch
                )

        self.history_tag = pyglet.text.Label(
                str(' '),
                multiline=True,
                font_name='courier',
                font_size=12,
                color=(255, 255, 255, 255),
                x=history_x,
                y=history_y,
                width=400,
                anchor_x='left', anchor_y='center',
                batch=self.batch
                )

        # self.batch.add(resources.magenta)

        self.batch.add(2, pyglet.gl.GL_LINES, None,
                ('v2i', (0, window_height - 50, window_width, window_height - 50)),
                ('c3B', (
                        obj.rgb_code[0], obj.rgb_code[1], obj.rgb_code[2],
                        255, 0, 0
                        ))
        )

    def update(self, dt):
        pass

    def update_history(self, history):
        self.history_tag.text = str(history)

    def draw(self):
        self.nature_tag.draw()
        self.title_tag.draw()
        # self.history_tag.draw()

    # return created_tag

