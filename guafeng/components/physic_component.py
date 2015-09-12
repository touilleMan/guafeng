from ecs import Component
from functools import namedtuple

from guafeng.tools import Vect2D


Hitbox = namedtuple('Hitbox', ('width', 'length'))


class PhysicComponent(Component):

    def __init__(self, x=0, y=0, width=10, height=20, static=False):
        super().__init__()
        self.static = static
        self.pos = Vect2D(x, y)
        self.speed = Vect2D(0, 0)
        self.width = width
        self.height = height
        self.jumping = False

    @property
    def min_x(self):
        return self.pos.x

    @property
    def max_x(self):
        return self.pos.x + self.width

    @property
    def min_y(self):
        return self.pos.y

    @property
    def max_y(self):
        return self.pos.y + self.height

    def collides_with(self, other, hint_vector=(1, 1)):
        # Exit with no intersection if found separated along an axis
        if (self.max_x <= other.min_x or self.min_x >= other.max_x or
                self.max_y <= other.min_y or self.min_y >= other.max_y):
            return None
        # No separating axis found, therefor there is at least one overlapping axis
        hint_x, hint_y = hint_vector
        if hint_x > 0:
            # Solid was going right, need to mov Xmax
            dx = self.max_x - other.min_x
        elif hint_x < 0:
            # Solid was going left, need to mov Xmin
            dx = self.min_x - other.max_x
        else:
            dx = 0
        if hint_y > 0:
            # Solid was going up, need to mov Ymax
            dy = self.max_y - other.min_y
        elif hint_y < 0:
            # Solid was going down, need to mov Ymin
            dy = self.min_y - other.max_y
        else:
            dy = 0
        return Vect2D(dx, dy)


# class PositionComponent(Component):
#     pass


class HitboxComponent(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min = Vect2D(x, y)
        self.max = Vect2D(x + width, y + height)

    def collides_with(self, other, hint_vector=(1, 1)):
        # Exit with no intersection if found separated along an axis
        if (self.max.x < other.min.x or self.min.x > other.max.x or
                self.max.y < other.min.y or self.min.y > other.max.y):
            return None
        # No separating axis found, therefor there is at least one overlapping axis
        if hint_vector[0]:
            # Solid was going right, need to mov Xmax
            dx = self.max.x - other.min.x
        else:
            # Solid was going left, need to mov Xmin
            dx = self.min.x - other.max.x
        if hint_vector[1]:
            # Solid was going up, need to mov Ymax
            dy = self.max.y - other.min.y
        else:
            # Solid was going down, need to mov Ymin
            dy = self.min.y - other.max.y
        return dx, dy
