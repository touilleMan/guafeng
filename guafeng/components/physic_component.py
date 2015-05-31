from ecs import Component
from functools import namedtuple

from guafeng.tools import Vect2D

Hitbox = namedtuple('Hitbox', ('width', 'length'))


class PhysicComponent(Component):

    def __init__(self, x=0, y=0, hitbox=None):
        super().__init__()
        self.pos = Vect2D(x, y)
        self.speed = Vect2D(0, 0)
        self.acc = Vect2D(0, 0)
        self.hitbox = hitbox or Hitbox(10, 20)
        self.jumping = False
