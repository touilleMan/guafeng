import pyglet

import ecs
import archetypes
import systems

if __name__ == '__main__':
	entity_manager = ecs.EntityManager()
	system_manager = ecs.SystemManager(entity_manager)

	system_manager.add_system(systems.RenderSystem())
	archetypes.create_player(entity_manager)

	# Start the pyglet application
	window = pyglet.window.Window()
	@window.event
	def on_draw():
    	window.clear()
		system_manager.systems[systems.RenderSystem].update()
	pyglet.app.run()
