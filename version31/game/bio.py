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

        box_width = window_width / 2
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

        # self.batch.add(4, pyglet.gl.GL_QUADS, None,
        #     ('v2f', )
        #     ('c3B', (
        #             obj.rgb_code[0], 
        #             obj.rgb_code[1], 
        #             obj.rgb_code[2], 
        #             255, 
        #             0, 
        #             0
        #     ))
        # )


        # self.batch.add(2, pyglet.gl.GL_LINES, None,
        #         ('v2i', (0, window_height - 50, window_width, window_height - 50)),
        #         ('c3B', (
        #                 obj.rgb_code[0], obj.rgb_code[1], obj.rgb_code[2],
        #                 255, 0, 0
        #                 ))
        # )




        self.title_tag = pyglet.text.Label(
                str(obj.title),
                font_name='Bangla MN',
                font_size=12,
                color=(255, 255, 255, 255),
                x=title_x,
                y=(i*box_height) + 10,
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
                x=100,
                y=(i*box_height),
                width=600,
                anchor_x='left', anchor_y='center',
                batch=batch
            )

        # self.weights_tag = pyglet.text.Label(
        #     (
        #         str(obj.ia_weight) + '\n' +
        #         str(obj.oa_weight) + '\n' +
        #         str(obj.ic_weight) + '\n' +
        #         str(obj.oc_weight) + '\n' +
        #         str(obj.is_weight) + '\n' +
        #         str(obj.os_weight) + '\n'
        #     ),
        #         multiline=True,
        #         font_name='Helvetica',
        #         font_size=12,
        #         color=(255, 255, 255, 255),
        #         x=150,
        #         y=600//2,
        #         width=200,
        #         anchor_x='left', anchor_y='center',
        #         batch=batch
        #     )

        # self.history_tag = pyglet.text.Label(
        #         str(' '),
        #         multiline=True,
        #         font_name='courier',
        #         font_size=12,
        #         color=(255, 255, 255, 255),
        #         x=history_x,
        #         y=history_y,
        #         width=400,
        #         anchor_x='left', anchor_y='center',
        #         batch=self.batch
        #     )


    def update(self):
        # REDEFINE VALUES HERE
        pass

    def update_history(self, history):
        self.history_tag.text = str(history)

    # def draw(self):
    #     # self.weights_tag.draw()
    #     self.nature_tag.draw()
    #     self.title_tag.draw()
    #     resources.green.blit(20,50)

    #     pyglet.graphics.glBegin(pyglet.gl.GL_LINES)
    #     pyglet.graphics.glVertex3f(100,100,0)
    #     pyglet.graphics.glVertex3f(100,0,100)
    #     pyglet.graphics.glEnd()
        # self.history_tag.draw()
