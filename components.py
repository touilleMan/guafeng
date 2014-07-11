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


class Physic(ecs.Component):

    def __init__(self, body):
        super().__init__()
        self.body = body
        self.jumping = False


class Input(ecs.Component):

    def __init__(self, keymap=None):
        """:param: keymap : dict of keys with they callback"""
        super().__init__()
        self.keymap = keymap if keymap else []


class Camera(ecs.Component):

    def __init__(self, x=0, y=0, active=True):
        """x,y : world coordinates of the camera"""
        super().__init__()
        self.active = active
        self.x = x
        self.y = y

    def move(self, x=0, y=0):
        self.x += x
        self.y += y


class Behaviour(ecs.Component):

    def __init__(self):
        super().__init__()
        self.movement = 0
        self._jump = False
        self.speed = 400
        self.jump_velocity = 300

    def move_right(self):
        self.movement = 1

    def move_left(self):
        self.movement = -1

    def jump(self):
        self._jump = True

    def reset(self):
        self.movement = 0
        self._jump = False
