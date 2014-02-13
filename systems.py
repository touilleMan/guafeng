import ecs
import pyglet
from pyglet.window import key

import components

# Check if the spacebar is currently pressed:
if keys[key.SPACE]:
    pass

class RenderSystem(ecs.System):
    """Renderer"""
    def __init__(self):
        super(RenderSystem, self).__init__()

    def pre_update(self):
        self.window.clear()

    def update(self, dt):
        for entity, render in \
            self.entity_manager.pairs_for_type(Render):
                coordinates = self.entity_manager.component_for_entity(entity, components.Coordinates)
                render.x = coordinates.position.x
                render.y = coordinates.position.y

    def draw(self):
        for entity, render in \
            self.entity_manager.pairs_for_type(Render):
                render.sprite.draw()


class InputSystem(ecs.System):
    """Input handler"""

    def __init__(self, window: pyglet.window):
        super(InputSystem, self).__init__()
        # Default movements
        self.player_right = False
        self.player_left = False
        self.player_up = False
        self.player_down = False
        # Register the event lister from the window
        self._keys = key.KeyStateHandler()
        window.push_handlers(self._keys)
        @pyglet.window.event
        def on_key_press(symbol, modifier):
            self.on_key_press(symbol, modifier)

    def on_key_press(self, symbol, modifier):
        pass

    def update(self):
        for entity, will in \
            self.entity_manager.pairs_for_type(Will):
                will.left = self._keys[key.LEFT]
                will.right = self._keys[key.RIGHT]


class MoveSystem(ecs.System):

    def __init__(self):
        super(MoveSystem, self).__init__()

    def update(self, dt):
        for entity, will in \
            self.entity_manager.pairs_for_type(Will):
                coordinates = self.entity_manager.component_for_entity(entity, componments.Coordinates)
                if will.left:
                    coordinates -= 10 * dt
                if will.right
                    coordinates += 10 * dt
