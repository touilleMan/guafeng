import ecs
import pyglet
from pyglet.window import key

import components


class RenderSystem(ecs.System):
    """Renderer"""
    def __init__(self):
        super(Render, self).__init__()

    def pre_update(self):
        self.window.clear()

    def update(self, dt):
        for entity, renderable_component in \
            self.entity_manager.pairs_for_type(Render):
                renderable_component.sprite.draw()


class InputSystem(ecs.System):
    """Input handler"""

    def __init__(self, window: pyglet.window):
        super(Input, self).__init__()
        # Default movements
        self.player_right = False
        self.player_left = False
        self.player_up = False
        self.player_down = False
        # Register the event lister from the window
        @pyglet.window.event
        def on_key_press(symbol, modifier):
            self.on_key_press(symbol, modifier)

    def pre_update(self):
        pass

    def on_key_press(self, symbol, modifier):
        if symbol == key.LEFT:
            pass
        elif symbol == key.RIGHT:            
            pass
