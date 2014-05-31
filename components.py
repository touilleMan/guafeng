import ecs

from tools import Vect2D


class Render(ecs.Component):
    """Component that can be render on screen"""
    def __init__(self, sprite):
        super().__init__()
        self.sprite = sprite


class Coordinates(ecs.Component):
    def __init__(self, x=0, y=0, dx=0, dy=0, ax=0, ay=0):
        super().__init__()
        self.position = Vect2D(x, y)
        self.speed = Vect2D(dx, dy)
        self.acceleration = Vect2D(ax, ay)


class Input(ecs.Component):
    def __init__(self, keymap=None):
        super().__init__()
        self.keymap = keymap if keymap else []


class Behaviour(ecs.Component):
    def __init__(self):
        super().__init__()
        self.right = False
        self.left = False
        self.jump = False
        self.speed = 400

    def move_right(self):
        self.right = True
        self.left = False

    def move_left(self):
        self.left = True
        self.right = False

    def jump(self):
        self.jump = True

    def reset(self):
        self.left = self.right = self.jump = False
