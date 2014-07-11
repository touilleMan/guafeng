import ecs
import pyglet
from pyglet.window import key
import pymunk

import components


class RenderSystem(ecs.System):

    """Renderer"""

    def __init__(self, window):
        super().__init__()
        self._window = window

    def update(self, dt):
        # Should be only one active camera, get the first available
        camera = next((c for e, c in
                       self.entity_manager.pairs_for_type(components.Camera)
                       if c.active), None)
        if not camera:
            return
        for entity, render in \
                self.entity_manager.pairs_for_type(components.Render):
                physic = self.entity_manager.component_for_entity(
                    entity, components.Physic)
                render.sprite.x = physic.body.position.x - camera.x
                render.sprite.y = physic.body.position.y - camera.y

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
                physic = self.entity_manager.component_for_entity(
                    entity, components.Physic)
                if behaviour.movement:
                    physic.body.velocity.x = behaviour.movement * \
                        behaviour.speed
                else:
                    physic.body.velocity.x = 0
                if behaviour._jump and not physic.jumping:
                    physic.body.velocity.y += behaviour.jump_velocity

                behaviour.reset()


class PhysicSystem(ecs.System):
    GRAVITY = (0, -900)

    def __init__(self):
        super().__init__()
        self.space = pymunk.Space()
        self.space.gravity = self.GRAVITY

    def update(self, dt):
        self.space.step(dt)
