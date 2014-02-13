import pyglet

import ecs
import archetypes
import systems

if __name__ == '__main__':
	entity_manager = ecs.EntityManager()
	system_manager = ecs.SystemManager(entity_manager)

	render_system = systems.RenderSystem()
	system_manager.add_system(render_system)
	input_system = systems.InputSystem()
	system_manager.add_system(input_system)
	archetypes.create_player(entity_manager)

	# Start the pyglet application
	window = pyglet.window.Window()
	@window.event
	def on_draw():
    	window.clear()
		render_system.draw()
	pyglet.clock.schedule_interval(system_manager.update, 1/60.)
	pyglet.app.run()
