#!/usr/bin/env python

from game import bio, resources, vector2, util, agent_natures, agent_titles, event_generation, narrator
# from collections import deque
from termcolor import colored
from pyglet.gl import *
import colorama
import pyglet
import random
import os
import sys
import time
# import math

# ----- Init Sequence -------
agent_batch = pyglet.graphics.Batch()
bio_batch = pyglet.graphics.Batch()
fps_display = pyglet.clock.ClockDisplay()

agent_index = []
agents = []
agent_bios = []
agent_batches = []

# ---- Timer Options ------

bio_duration = 200
cycle_interval = 100

symbolic_cycle_interval = 1
retirement_cycle_interval = 10


# ----- Debug Options --------
debug = True

pyglet.options['debug_gl'] = False

# ----- Program Options ------
window_width, window_height = 1200, 800
agent_count = 30

# ----- Behavior Options -----
_ALGINMENT_RADIUS, _ALIGNMENT_WEIGHT = 60, 1
_COHESION_RADIUS, _COHESION_WEIGHT = 50, 1
_SEPARATION_RADIUS, _SEPARATION_WEIGHT = 35, 1
_WIGGLE_AMOUNT = 2
_SPEED_LIMIT = 20
_SPEED_MULTIPLIER = 0.3
_INTERACTION_INTERVAL = 120
_INTERACTION_RADIUS = 50


class Agent(pyglet.sprite.Sprite):
    """Main Agent class, which is capable of executing set behaviors"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Calculation
        self.total_agent_count = agent_count
        self.interaction_timer = 0

        # Title
        self.title = agent_titles.get_title()

        # Nature
        (
            self.nature,
            self.nature_str,
            self.ia_index,
            self.oa_index,
            self.ic_index,
            self.oc_index,
            self.is_index,
            self.os_index
        ) = agent_natures.get_nature()

        self.ia_weight = _ALIGNMENT_WEIGHT * (
                util.round_nearest(
                        self.oa_index/len(
                                agent_natures.outer_alignment_nature), 0.05)*2)
        self.oa_weight = _COHESION_WEIGHT * (
                util.round_nearest(
                        self.oa_index/len(
                                agent_natures.outer_alignment_nature), 0.05)*2)
        self.ic_weight = _ALIGNMENT_WEIGHT * (
                util.round_nearest(
                        self.oc_index/len(
                                agent_natures.outer_cohesion_nature), 0.05)*2)
        self.oc_weight = _SEPARATION_WEIGHT * (
                util.round_nearest(
                        self.oc_index/len(
                                agent_natures.outer_cohesion_nature), 0.05)*2)
        self.is_weight = _COHESION_WEIGHT * (
                util.round_nearest(
                        self.os_index/len(
                                agent_natures.outer_separation_nature), 0.05)*2)
        self.os_weight = _SEPARATION_WEIGHT * (
                util.round_nearest(
                        self.os_index/len(
                                agent_natures.outer_separation_nature), 0.05)*2)

        self.color_str = ""

        self.velocity_x = random.randint(-50, 50)
        self.velocity_y = random.randint(-50, 50)
        self.v = vector2.Vector2(self.velocity_x, self.velocity_y)
        self.v.normalise()
        self.v *= 2

        # List of vertices for drawing lines. Needs updating!
        self.vlist = pyglet.graphics.vertex_list(2,
                                                 ('v2f',
                                                  [self.x,
                                                   self.y,
                                                   self.x + self.v.x,
                                                   self.y + self.v.y]))

        # self.history = []

    def update(self, dt):

        # Check edges of window
        self.check_bounds()

        # Cap agent movement speed.
        if abs(self.v.x) > _SPEED_LIMIT:
            self.v.x *= 0.90
        if abs(self.v.y) > _SPEED_LIMIT:
            self.v.y *= 0.90

        # Calculate wiggle.
        self.random_offset = vector2.Vector2(
                random.randint(((_WIGGLE_AMOUNT / 2) ) * -1, (_WIGGLE_AMOUNT / 2) ),
                random.randint(((_WIGGLE_AMOUNT / 2) ) * -1, (_WIGGLE_AMOUNT / 2) )
                )
        self.v += self.random_offset

        # Draw momentum vector
        self.vlist = pyglet.graphics.vertex_list(
                2, ('v2f', [
                        self.x,
                        self.y,
                        self.x + self.v.x,
                        self.y + self.v.y
                    ])
                )

        # Actual movement.
        self.x += self.v.x * dt
        self.y += self.v.y * dt

        # Increase interaction timer
        self.interaction_timer += 1

    # Movement calculations
    def check_bounds(self):
        """Checks the object's edges against the edges of the window."""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = window_width + self.image.width / 2
        max_y = window_height + self.image.width / 2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def compute_alignment(self, other_agent):
        # Alignment vector will be the sum of the two
        alignment_vector = vector2.Vector2(
                self.velocity_x + other_agent.velocity_x,
                self.velocity_y + other_agent.velocity_y)
        alignment_vector.normalise()
        return alignment_vector

    def compute_cohesion(self, other_agent):
        # Cohesion vector is the force of grouping.
        cohesion_vector = vector2.Vector2(
                self.x + other_agent.x,
                self.y + other_agent.y)
        cohesion_vector.x /= 2
        cohesion_vector.y /= 2
        cohesion_vector.normalize()
        return cohesion_vector

    def compute_separation(self, other_agent):
        # Separation is repelling force
        separation_vector = vector2.Vector2(
                other_agent.x - self.x,
                other_agent.y - self.y)

        separation_vector *= -1
        return separation_vector

    # Detection / Interaction
    def neighbor_lines(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)
        glColor3f(
                (4/actual_distance) * 3,
                (4/actual_distance) * 3,
                (4/actual_distance) * 3)

        if actual_distance <= _INTERACTION_RADIUS:
            self.neighbor_vlist = pyglet.graphics.vertex_list(
                    2, ('v2f', [
                            self.x,
                            self.y,
                            other_agent.x,
                            other_agent.y]))
            self.neighbor_vlist.draw(GL_LINES)

    def interacts_with(self, other_agent):
        actual_distance = util.distance(self.position, other_agent.position)

        if actual_distance <= _ALGINMENT_RADIUS:
            self.v += (
                    self.compute_alignment(other_agent) * (
                            self.ia_weight + other_agent.oa_weight))
        if actual_distance <= _COHESION_RADIUS:
            self.v += (
                    self.compute_cohesion(other_agent) * (
                            self.ic_weight + other_agent.oc_weight))
        if actual_distance <= _SEPARATION_RADIUS:
            self.v += (
                    self.compute_separation(other_agent) * (
                            self.is_weight + other_agent.is_weight))


class Narrative(object):
    """Main Narrative visualization, displaying the story generated by event_generation. """

    def __init__(self):
        self.cycle = 0
        self.age = 0
        self.duration = 0
        narrator.intro()

    def update(self, dt):
        self.duration += 1

        # Cycle
        if self.duration % cycle_interval == 0 and self.age != 6:
            self.cycle += 1
            self.age += 1

            age = narrator.counter(self.cycle, random.choice(narrator.ages))

        elif self.duration % cycle_interval == 0 and self.age == 6:
            self.cycle += 1
            self.age = 1

            age = narrator.counter(self.cycle, random.choice(narrator.ages))


        # Symbolic Gestures
        if self.duration % (cycle_interval*symbolic_cycle_interval) == 0:
            event_generation.symbolic_interaction(random.choice(agents),random.choice(agents))


class Bio_Screen(object):
    """Manages the display of the biographies created with the 'bio' module"""

    def __init__(self):

        self.created_tag = pyglet.text.Label(
                'Hello, world',
                font_name='Times New Roman',
                font_size=36,
                color=(255, 255, 255, 255),
                x=window_width//2,
                y=window_height//2,
                anchor_x='center', anchor_y='center')



    def draw(self):
        pass
        # self.test_tag.draw()


class Application():
    """
    Initializes and iterates through agents.
    """

    def add_agent(self, i):
        rand_color_choice = random.randint(0,5)
        agent_color_id=[
            resources.red,
            # resources.white,
            resources.yellow,
            resources.green,
            resources.blue,
            resources.cyan,
            resources.magenta
            ]

        agent_rgb=[
                [255,0,0], # red
                [255,255,0], # yellow
                [0,255,0], # blue
                [0,0,255], # green
                [0,255,255], # cyan
                [255,0,255] # magenta
        ]

        agent_color=[
            "on_red",
            # "on_white",
            "on_yellow",
            "on_green",
            "on_blue",
            "on_cyan",
            "on_magenta"
            ]

        new_agent = Agent(
            img = agent_color_id[rand_color_choice],
            x=random.randint(0, window_width),
            y=random.randint(0, window_height),
            batch=agent_batch
            )

        new_agent.color_str=agent_color[rand_color_choice]
        new_agent.rgb_code=agent_rgb[rand_color_choice]

        new_agent.id = i
        agents.append(new_agent)
        agent_index.append("")

        new_agent_batch = pyglet.graphics.Batch()
        agent_batches.append(new_agent_batch)

        new_agent_bio = bio.Biography(new_agent, bio_batch, window_width, window_height, i)
        agent_bios.append(new_agent_bio)

    def setup(self):
        self.duration = 0
        self.bio_index = 0

        """Initialize agents"""
        for i in range(agent_count):
            self.add_agent(i)

            print(
                # "Agent " + str(i)
                # + " is a "
                colored(agents[i].title, color=None, on_color=agents[i].color_str)
                + " who is seen as "
                + agents[i].nature_str)
                # + " with weights of"
                # + str(agents[i].ia_weight) + " "
                # + str(agents[i].ic_weight) + " "
                # + str(agents[i].is_weight) + " "
                # + str(agents[i].oa_weight) + " "
                # + str(agents[i].oc_weight) + " "
                # + str(agents[i].os_weight) + " "


    def retire(self, retiree):
        
        retiree_index = agents.index(retiree)

        retiree.delete()
        del agents[retiree_index]
        del agent_bios[retiree_index]

        self.add_agent(retiree.id)

        event_generation.retire(retiree)

    def update(self, dt):
        # Go through each agent's update loop
        for agent in agents:
            agent.update(dt)
            
        # Iterate through all object pairs to check for detection
        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                obj_1 = agents[i]
                obj_2 = agents[j]
                obj_1.interacts_with(obj_2)
                obj_2.interacts_with(obj_1)

            # agent_bios[i].update(dt)            

        self.duration += 1
        if self.duration % bio_duration == 0 and self.bio_index != (agent_count-1):
            self.bio_index += 1
        if self.duration % bio_duration == 0 and self.bio_index == (agent_count-1):
            self.bio_index = 0

        if self.duration % (cycle_interval*retirement_cycle_interval) == 0:
            retiree = random.choice(agents)
            self.retire(retiree)

        # ------------ System Restart ------------------
        if debug == False:
            if self.duration == 1000:
                    python = sys.executable
                    os.execl(python, python, * sys.argv)

        # if self.duration == 500:
        #     time.sleep(2)


def main():
    """
    Main loop. Windows are set up, and updates are called.
    """

    narrative = Narrative()
    bio_screen = Bio_Screen()
    app = Application()
    app.setup()

    display = pyglet.window.get_platform().get_default_display()

    if debug is True:
        agent_window = pyglet.window.Window(
            window_width, window_height, vsync=False)
        bio_window = pyglet.window.Window(
            window_width, window_height, vsync=False)
    else:
        screen_1 = display.get_screens()[0]
        screen_2 = display.get_screens()[1]

        agent_window = pyglet.window.Window(
            fullscreen=True, screen=screen_1, vsync=False)
        bio_window = pyglet.window.Window(
            fullscreen=True, screen=screen_2, vsync=False)

    @agent_window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        agent_window.clear()
        agent_batch.draw()
        fps_display.draw()

        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                obj_1 = agents[i]
                obj_2 = agents[j]
                obj_1.neighbor_lines(obj_2)

                actual_distance = util.distance(obj_1.position, obj_2.position)
                if actual_distance < _INTERACTION_RADIUS:
                    if (obj_1.interaction_timer and
                            obj_2.interaction_timer > _INTERACTION_INTERVAL):
                        obj_1.interaction_timer = 0
                        obj_2.interaction_timer = 0
                        print(event_generation.physical_event(obj_1, obj_2))
                        interaction_sprite = pyglet.sprite.Sprite(
                                resources.interaction_anim, 
                                x=(obj_1.x-50), 
                                y=(obj_1.y-50), 
                                batch=agent_batch
                                )

                        # ADD HISTORY
                        # agent_bios[obj_1.id].update_history(obj_1.history)

        for agent in agents:     
            glColor3f(agent.rgb_code[0], agent.rgb_code[1], agent.rgb_code[2])
            agent.vlist.draw(GL_LINES)  # Draw velocity vector

    @bio_window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        bio_window.clear()
        # bio_screen.draw()

        # for i in range(agent_count):
        #     glBegin(pyglet.gl.GL_LINES)
        #     glVertex2f(0,0)
        #     glVertex2f(100,100)
        #     glEnd()

        bio_batch.draw()

    pyglet.clock.schedule_interval(app.update, 1 / 60.0)
    pyglet.clock.schedule_interval(narrative.update, 1 / 60.0)

    pyglet.app.run()


main()
