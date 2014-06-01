import pyglet
import components
from pyglet.window import key
import pymunk

# dummy image
PLAYER_COLOR = (0xff, 0x00, 0x66, 255)
PLAYER_IMAGE = pyglet.image.create(20, 50,
                                   pyglet.image.SolidColorImagePattern(PLAYER_COLOR))


def create_camera(entity_manager):
    camera = entity_manager.create_entity()
    camera_c = components.Camera()
    entity_manager.add_component(camera, camera_c)
    keymap = [(key.Q, lambda: camera_c.move(-10, 0)),
              (key.D, lambda: camera_c.move(10, 0)),
              (key.S, lambda: camera_c.move(0, -10)),
              (key.W, lambda: camera_c.move(0, 10))]
    entity_manager.add_component(camera, components.Input(keymap))


def create_player(entity_manager, physic_system):
    player = entity_manager.create_entity()
    render = components.Render(pyglet.sprite.Sprite(PLAYER_IMAGE))
    entity_manager.add_component(player, render)
    coordinates = components.Coordinates()
    entity_manager.add_component(player, coordinates)

    # Create hitbox and add it to physic system
    body = pymunk.Body(1, 1666)
    body.position = 300, 300
    poly = pymunk.Poly.create_box(body)
    physic_system.space.add(body, poly)
    physic = components.Physic(body)
    entity_manager.add_component(player, physic)

    # Build key mapping
    behaviour = components.Behaviour()
    entity_manager.add_component(player, behaviour)
    keymap = [(key.LEFT, behaviour.move_left),
              (key.RIGHT, behaviour.move_right),
              (key.SPACE, behaviour.jump)]
    entity_manager.add_component(player, components.Input(keymap))
    return player


def create_map(entity_manager, physic_system):
    space = physic_system.space
    # static = [pymunk.Segment(space.static_body, (10, 50), (300, 50), 5),
    #           pymunk.Segment(space.static_body, (300, 50), (325, 50), 5),
    #           pymunk.Segment(space.static_body, (325, 50), (350, 50), 5),
    #           pymunk.Segment(space.static_body, (350, 50), (375, 50), 5),
    #           pymunk.Segment(space.static_body, (375, 50), (680, 50), 5),
    #           pymunk.Segment(space.static_body, (680, 50), (680, 370), 5),
    #           pymunk.Segment(space.static_body, (680, 370), (10, 370), 5),
    #           pymunk.Segment(space.static_body, (10, 370), (10, 50), 5)]
    static = [pymunk.Segment(space.static_body, (0, 0), (300, 0), 5)]
    space.add(static)
