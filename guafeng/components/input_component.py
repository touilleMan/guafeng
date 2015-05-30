from functools import namedtuple
from ecs import Component


KeyBind = namedtuple('KeyBind', ('key', 'callback', 'type'))


class InputComponent(Component):

    def __init__(self, keymap=None):
        super().__init__()
        self.keymap = []

    def add_keybind(self, key, callback, type='default'):
        self.keymap.append(KeyBind(key, callback, type))
