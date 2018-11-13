import pyglet, math
from game import resources, load, vector2, physicalobject
from pyglet.gl import *

window_width, window_height = 800, 600

game_window = pyglet.window.Window(window_width, window_height)

main_batch = pyglet.graphics.Batch()
data_batch = pyglet.graphics.Batch()

world_label = pyglet.text.Label(text="World", x=400, y=575, anchor_x='center', batch=main_batch)

agents = load.agents(40, main_batch)

@game_window.event
def on_draw():
	game_window.clear()
	
	for i in range(len(agents)):
		agents[i].name_tag.draw()

	main_batch.draw()
	glColor3f(255,0,25)
	for agent in agents:
		agent.vlist.draw(GL_LINES)


def update(dt):
	# Go through each agent's update loop
	for agent in agents:
		agent.update(dt)
		agent.vlist.draw(GL_TRIANGLES)


	# Iterate through all object pairs to check for detection
	for i in range(len(agents)):
		for j in range(i + 1, len(agents)):
			obj_1 = agents[i]
			obj_2 = agents[j]
			obj_1.interacts_with(obj_2)
			obj_2.interacts_with(obj_1)

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/60.0)
	pyglet.app.run()