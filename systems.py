import ecs
import pyglet
from pyglet.window import key
from pyglet.gl import glTranslatef, glLoadIdentity
import pymunk

import components


class RenderSystem(ecs.System):

    """Renderer"""

    def __init__(self, window, show_fps=False):
        super().__init__()
        self._window = window
        self.show_fps = show_fps
        self._clock_display = pyglet.clock.ClockDisplay()
        self.batch = pyglet.graphics.Batch()

    def update(self, dt):
        for entity, render in \
                self.entity_manager.pairs_for_type(components.Render):
                physic = self.entity_manager.component_for_entity(
                    entity, components.Physic)
                render.sprite.x = physic.body.position.x
                render.sprite.y = physic.body.position.y

    def draw(self):
        self._window.clear()
        # Should be only one active camera, get the first available
        camera = next((c for e, c in
                       self.entity_manager.pairs_for_type(components.Camera)
                       if c.active), None)
        # Reset the "eye" back to the default location.
        glLoadIdentity()
        if camera:
            # Move the "eye" to the current location on the map.
            glTranslatef(*camera.gl_translate)

        # self.batch.draw()
        # TODO : use batch to draw everything
        for entity, render in \
                self.entity_manager.pairs_for_type(components.Render):
                render.sprite.draw()

        if self.show_fps:
            glLoadIdentity()
            self._clock_display.draw()


class InputSystem(ecs.System):

    """Input handler"""

    default = 0
    on_pressed = 1
    on_released = 2

    def __init__(self, window: pyglet.window):
        super().__init__()
        # Register the event lister from the window
        self._keys = key.KeyStateHandler()
        window.push_handlers(self._keys)
        self._pressed_keys = set()
        self._released_keys = set()
        window.on_key_press = lambda s, m: self._pressed_keys.add(s)
        window.on_key_release = lambda s, m: self._released_keys.add(s)

    def update(self, dt):
        for _, input_ in \
                self.entity_manager.pairs_for_type(components.Input):
            for key_bind in input_.keymap:
                key = key_bind[0]
                callback = key_bind[1]
                if len(key_bind) == 2 or key_bind[2] == 'key_press':
                    if self._keys[key]:
                        callback()
                elif key_bind[2] == 'on_press':
                    if key in self._pressed_keys:
                        callback()
                elif key_bind[2] == 'on_release':
                    if key in self._released_keys:
                        callback()
        self._pressed_keys.clear()
        self._released_keys.clear()


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
