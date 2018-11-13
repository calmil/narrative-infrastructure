import pyglet, math
from game import resources, load, vector2

# I like the idea of someone still clinging to this after some economic collapse
window_width, window_height = 800, 600

game_window = pyglet.window.Window(window_width, window_height)
# data_window = pyglet.window.Window(window_width, window_height)

main_batch = pyglet.graphics.Batch()
data_batch = pyglet.graphics.Batch()

world_label = pyglet.text.Label(text="World", x=400, y=575, anchor_x='center', batch=main_batch)

# call the load method, where our initial dataset will be created and agents inst'zd 
# this returns the 'agents' list that is created, and then that array is reassigned
agents = load.agents(40, main_batch)

@game_window.event
def on_draw():
	game_window.clear()

	# for i in range(len(agents)):
	# 	agents[i].name_tag.draw()
	# 	agents[i].data_tag.draw()

	main_batch.draw()

def update(dt):
	# Go through each agent's update loop
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

def update_moves(dt):
	for agent in agents:
		agent.update_move(dt)

if __name__ == '__main__':
	# schedule a function to be called at a certain time.
	pyglet.clock.schedule_interval(update, 1/60.0)
	pyglet.clock.schedule_interval(update_moves, 0.5)
	pyglet.app.run()