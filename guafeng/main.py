#! /usr/bin/env python3

import pyglet
import ecs

from guafeng import archetypes
from guafeng import systems


def main():
    window = pyglet.window.Window()

    entity_manager = ecs.EntityManager()
    system_manager = ecs.SystemManager(entity_manager)

    render_system = systems.RenderSystem(window)
    input_system = systems.InputSystem(window)

    system_manager.add_system(render_system)
    system_manager.add_system(input_system)
    # system_manager.add_system(systems.MoveSystem())
    physic_system = systems.PhysicSystem()
    system_manager.add_system(physic_system)

    archetypes.create_map(entity_manager, system_manager)
    archetypes.create_player(entity_manager, system_manager)
    archetypes.create_camera(entity_manager, system_manager)

    # Start the pyglet application
    @window.event
    def on_draw():
        render_system.draw()
    pyglet.clock.schedule_interval(system_manager.update, 1 / 60)
    pyglet.app.run()

if __name__ == '__main__':
    main()
