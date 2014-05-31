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
        self.body = body
    # def __init__(self, **kwargs):
    #     super().__init__()
    #     x = kwargs['x'] if 'x' in kwargs else 0
    #     y = kwargs['y'] if 'y' in kwargs else 0
    #     self.position = Vect2D(x, y)
    #     dx = kwargs['dx'] if 'dx' in kwargs else 0
    #     dy = kwargs['dy'] if 'dy' in kwargs else 0
    #     self.speed = Vect2D(dx, dy)
    #     ax = kwargs['ax'] if 'ax' in kwargs else 0
    #     ay = kwargs['ay'] if 'ay' in kwargs else 0
    #     self.acceleration = Vect2D(ax, ay)
    #     self.rot = kwargs['rot'] if 'rot' in kwargs else 0
    #     self.drot = kwargs['drot'] if 'drot' in kwargs else 0
    #     hitbox_x = kwargs['hitbox_x'] if 'hitbox_x' in kwargs else 0
    #     hitbox_y = kwargs['hitbox_y'] if 'hitbox_y' in kwargs else 0
    #     self.hitbox = Vect2D(hitbox_x, hitbox_y)


class Input(ecs.Component):

    def __init__(self, keymap=None):
        super().__init__()
        self.keymap = keymap if keymap else []


class Behaviour(ecs.Component):

    def __init__(self):
        super().__init__()
        self.movement = 0
        self.jump = False
        self.speed = 400

    def move_right(self):
        self.movement = 1

    def move_left(self):
        self.movement = -1

    def jump(self):
        self.jump = True

    def reset(self):
        self.movement = 0
        self.jump = False
