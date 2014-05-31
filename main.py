#! /usr/bin/env python3

import pyglet
import ecs

import archetypes
import systems


def main():
    window = pyglet.window.Window()

    entity_manager = ecs.EntityManager()
    system_manager = ecs.SystemManager(entity_manager)

    render_system = systems.RenderSystem(window)
    input_system = systems.InputSystem(window)

    system_manager.add_system(render_system)
    system_manager.add_system(input_system)
    system_manager.add_system(systems.MoveSystem())

    archetypes.create_player(entity_manager)

    # Start the pyglet application
    @window.event
    def on_draw():
        render_system.draw()
#   def on_update(dt, xx):
#       system_manager.update(dt)
    pyglet.clock.schedule_interval(system_manager.update, 1/60.)
    pyglet.app.run()

if __name__ == '__main__':
    main()
