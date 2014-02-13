import ecs
import pyglet
from pyglet.window import key

import components

class RenderSystem(ecs.System):
    """Renderer"""
    def __init__(self, window):
        super(RenderSystem, self).__init__()
        self._window = window

    def update(self, dt):
        for entity, render in \
            self.entity_manager.pairs_for_type(components.Render):
                coordinates = self.entity_manager.component_for_entity(entity, components.Coordinates)
                render.sprite.x = coordinates.position.x
                render.sprite.y = coordinates.position.y

    def draw(self):
        self._window.clear()
        for entity, render in \
            self.entity_manager.pairs_for_type(components.Render):
                render.sprite.draw()


class InputSystem(ecs.System):
    """Input handler"""

    def __init__(self, window: pyglet.window):
        super(InputSystem, self).__init__()
        # Register the event lister from the window
        self._keys = key.KeyStateHandler()
        window.push_handlers(self._keys)

    def update(self, dt):
        for entity, will in \
            self.entity_manager.pairs_for_type(components.Will):
                will.left = self._keys[key.LEFT]
                will.right = self._keys[key.RIGHT]


class MoveSystem(ecs.System):
    MOVE_SPEED = 50

    def __init__(self):
        super(MoveSystem, self).__init__()

    def update(self, dt):
        for entity, will in \
            self.entity_manager.pairs_for_type(components.Will):
                coordinates = self.entity_manager.component_for_entity(entity, components.Coordinates)
                if will.left:
                    coordinates.position.x -= MoveSystem.MOVE_SPEED * dt
                if will.right:
                    coordinates.position.x += MoveSystem.MOVE_SPEED * dt
