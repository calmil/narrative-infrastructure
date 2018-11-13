import pyglet, math
from game import resources, load, vector2

window_width, window_height = 800, 600
game_window = pyglet.window.Window(window_width, window_height)
# data_window = pyglet.window.Window(window_width, window_width)

main_batch = pyglet.graphics.Batch()
text_batch = pyglet.graphics.Batch()

world_label = pyglet.text.Label(text="World", x=400, y=575, anchor_x='center', batch=main_batch)

agents = load.agents(5, main_batch)

@game_window.event
def on_draw():
	game_window.clear()

	main_batch.draw()

def update(dt):
	for agent in agents:
		agent.update(dt)

	# Iterate through all object pairs to check for detection
	for i in range(len(agents)):
		for j in range(i + 1, len(agents)):
			obj_1 = agents[i]
			obj_2 = agents[j]
			if obj_1.interacts_with(obj_2):
				obj_1.handle_interaction_with(obj_2)
				obj_2.handle_interaction_with(obj_1)

if __name__ == '__main__':
	# schedule a function to be called at a certain time.
	pyglet.clock.schedule_interval(update, 1/60.0)
	pyglet.app.run()