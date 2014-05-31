import pyglet
import components
from pyglet.window import key

# dummy image
PLAYER_COLOR = (0xff, 0x00, 0x66, 255)
PLAYER_IMAGE = pyglet.image.create(20, 50,
                   pyglet.image.SolidColorImagePattern(PLAYER_COLOR))


def create_player(entity_manager):
    player = entity_manager.create_entity()
    render = components.Render(pyglet.sprite.Sprite(PLAYER_IMAGE))
    entity_manager.add_component(player, render)
    coordinates = components.Coordinates()
    entity_manager.add_component(player, coordinates)
    # Build key mapping
    behaviour = components.Behaviour()
    entity_manager.add_component(player, behaviour)
    keymap = [(key.LEFT, behaviour.move_left),
              (key.RIGHT, behaviour.move_right),
              (key.SPACE, behaviour.jump)]
    entity_manager.add_component(player, components.Input(keymap))
    return player
