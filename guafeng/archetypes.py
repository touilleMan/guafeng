import pyglet
from pyglet.window import key
# import pymunk

from guafeng import components
from guafeng.components import (RenderComponent, CameraComponent,
                                InputComponent, BehaviorComponent, PhysicComponent)
from guafeng import systems

# dummy image
PLAYER_COLOR = (0xff, 0x00, 0x66, 255)
PLAYER_IMAGE = pyglet.image.create(20, 50,
                                   pyglet.image.SolidColorImagePattern(PLAYER_COLOR))


def create_camera(entity_manager, system_manager):
    camera = entity_manager.create_entity()
    camera_c = CameraComponent()
    render_system = system_manager._system_types[systems.RenderSystem]
    def switch_show_fps():
        if camera_c.active:
            render_system.show_fps = not render_system.show_fps
    entity_manager.add_component(camera, camera_c)
    input_c = InputComponent()
    input_c.add_keybind(key.U, lambda: camera_c.move(-10, 0))
    input_c.add_keybind(key.E, lambda: camera_c.move(10, 0))
    input_c.add_keybind(key.I, lambda: camera_c.move(0, -10))
    input_c.add_keybind(key.P, lambda: camera_c.move(0, 10))
    input_c.add_keybind(key.F10, switch_show_fps, type='on_press')
    entity_manager.add_component(camera, input_c)


def create_player(entity_manager, system_manager):
    physic_system = system_manager._system_types[systems.PhysicSystem]
    player = entity_manager.create_entity()
    render = RenderComponent(pyglet.sprite.Sprite(PLAYER_IMAGE))
    entity_manager.add_component(player, render)
    # coordinates = components.Coordinates()
    # entity_manager.add_component(player, coordinates)

    # Create hitbox and add it to physic system
    entity_manager.add_component(player, PhysicComponent())
    # body = pymunk.Body(1, 1666)
    # body.position = 300, 300
    # poly = pymunk.Poly.create_box(body)
    # physic_system.space.add(body, poly)
    # physic = components.Physic(body)
    # entity_manager.add_component(player, physic)

    # Build key mapping
    behavior = BehaviorComponent()
    entity_manager.add_component(player, behavior)

    input_c = InputComponent()
    input_c.add_keybind(key.LEFT, behavior.move_left)
    input_c.add_keybind(key.RIGHT, behavior.move_right)
    input_c.add_keybind(key.SPACE, behavior.jump)
    entity_manager.add_component(player, input_c)
    return player


def create_map(entity_manager, system_manager):
    physic_system = system_manager._system_types[systems.PhysicSystem]
    # space = physic_system.space
    # # static = [pymunk.Segment(space.static_body, (0, 0), (300, 0), 5)]
    # static = [pymunk.Segment(space.static_body, (0, 0), (1000, 0), 5),
    #           pymunk.Segment(space.static_body, (0, 0), (0, 200), 5),
    #           pymunk.Segment(space.static_body, (1000, 0), (1000, 200), 5)]
    # space.add(static)
