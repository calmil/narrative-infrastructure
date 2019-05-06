import pyglet
from game import resources


title_x = 30
title_y = 30

bio_x = 0
bio_y = 40

history_x = 300
history_y = 300

def create_text(text, window_width, window_height):
    pass


class Biography():
    """Creates a dynamic biography from an agent."""

    def __init__(self, obj, batch, window_width, window_height, i):

        box_width = 2 * (window_width / 3)
        box_height = window_height / 30

        self.obj = obj
        self.batch = batch

        self.vertex_list = self.batch.add(8, pyglet.gl.GL_LINES, None,
                ("v2f", (
                        0, i*box_height, 
                        box_width, i*box_height,
                        box_width, i*box_height,
                        box_width, i*box_height + box_height, 
                        box_width, i*box_height + box_height, 
                        0, i*box_height + box_height,
                        0, i*box_height + box_height,
                        0, 0, 
                    )
                )
            )

        self.title_tag = pyglet.text.Label(
                str(obj.title),
                font_name='Bangla MN',
                font_size=12,
                color=(255, 255, 255, 255),
                x=title_x,
                y=(i*box_height) + box_height/2,
                width=200,
                anchor_x='left', anchor_y='center',
                batch=batch
            )

        self.nature_tag = pyglet.text.Label(
                str(
                        obj.nature[0] + ', ' +
                        obj.nature[1] + ', ' +
                        obj.nature[2] + ', ' +
                        obj.nature[3] + ', ' +
                        obj.nature[4] + ', ' +
                        obj.nature[5] + ', '
                    ),
                multiline=True,
                font_name='Helvetica',
                font_size=12,
                color=(255, 255, 255, 255),
                x=box_width - 30,
                y=(i*box_height)+box_height/2,
                width=600,
                align='right',
                anchor_x='right', anchor_y='center',
                batch=batch
            )


    def update(self):
        # REDEFINE VALUES HERE
        pass

    def update_history(self, history):
        self.history_tag.text = str(history)

    def draw(self):
        # self.weights_tag.draw()
        self.nature_tag.draw()
        self.title_tag.draw()
        # resources.green.blit(20,50)

