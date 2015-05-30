from ecs import System
from pyglet.window import key
from enum import Enum

from guafeng.components import InputComponent


# TODO: use this ?
class KeyPressType(Enum):
    KEY_PRESS = 0
    ON_PRESS = 1
    ON_RELEASE = 2


class InputSystem(System):

    """Input handler"""

    def __init__(self, window):
        super().__init__()
        # Register the event lister from the window
        self._keys = key.KeyStateHandler()
        window.push_handlers(self._keys)
        self._pressed_keys = set()
        self._released_keys = set()
        window.on_key_press = lambda s, m: self._pressed_keys.add(s)
        window.on_key_release = lambda s, m: self._released_keys.add(s)

    def update(self, dt):
        for _, input_ in self.entity_manager.pairs_for_type(InputComponent):
            for kb in input_.keymap:
                if kb.type == 'on_press':
                    if kb.key in self._pressed_keys:
                        kb.callback()
                elif kb.type == 'on_release':
                    if kb.key in self._released_keys:
                        kb.callback()
                else:
                    if self._keys[kb.key]:
                        kb.callback()
        self._pressed_keys.clear()
        self._released_keys.clear()
