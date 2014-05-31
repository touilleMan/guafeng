import ecs
import pyglet
from pyglet.window import key

import components


class RenderSystem(ecs.System):
    """Renderer"""
    def __init__(self, window):
        super().__init__()
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
        super().__init__()
        # Register the event lister from the window
        self._keys = key.KeyStateHandler()
        window.push_handlers(self._keys)

    def update(self, dt):
        for entity, input_ in \
                self.entity_manager.pairs_for_type(components.Input):
                for key_, callback in input_.keymap:
                    if self._keys[key_]:
                        callback()


class MoveSystem(ecs.System):

    def __init__(self):
        super().__init__()

    def update(self, dt):
        for entity, behaviour in \
                self.entity_manager.pairs_for_type(components.Behaviour):
                coordinates = self.entity_manager.component_for_entity(entity, components.Coordinates)
                if behaviour.left:
                    coordinates.position.x -= behaviour.speed * dt
                if behaviour.right:
                    coordinates.position.x += behaviour.speed * dt
                behaviour.reset()


class PhysicSystem(ecs.System):
    def __init__(self):
        super().__init__()
