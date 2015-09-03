from ecs import System
import pyglet
from pyglet.gl import glTranslatef, glLoadIdentity

from guafeng.components import (RenderComponent, PhysicComponent,
                                CameraComponent, MapComponent)


class RenderSystem(System):

    """Renderer"""

    def __init__(self, world, show_fps=False):
        super().__init__()
        self._world = world
        self._window = self._world.window
        self.show_fps = show_fps
        self._clock_display = pyglet.clock.ClockDisplay()
        self.batch = pyglet.graphics.Batch()

    def update(self, dt):
        for entity, render in self.entity_manager.pairs_for_type(RenderComponent):
            physic = self.entity_manager.component_for_entity(entity, PhysicComponent)
            render.sprite.x = physic.pos.x
            render.sprite.y = physic.pos.y

    def draw(self):
        self._window.clear()
        # Should be only one active camera, get the first available
        camera = next((c for e, c in self.entity_manager.pairs_for_type(CameraComponent)
                       if c.active), None)
        # Reset the "eye" back to the default location.
        glLoadIdentity()
        if camera:
            # Move the "eye" to the current location on the map.
            glTranslatef(*camera.gl_translate)
        # Draw the map
        self._world.map.ground_batch.draw()
        # _, map = next(self.entity_manager.pairs_for_type(MapComponent))
        # map.renderer.draw()
        # self.batch.draw()
        # TODO : use batch to draw everything
        for _, render in self.entity_manager.pairs_for_type(RenderComponent):
            render.sprite.draw()
        # Display GUI
        if self.show_fps:
            glLoadIdentity()
            self._clock_display.draw()
