import unittest


class Vect2D:

    """2 dimentional vector"""

    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Vect2D (x: {}, y: {})".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vect2D):
            return Vect2D(self.x + other.x, self.y + other.y)
        else:
            return Vect2D(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vect2D):
            return Vect2D(self.x - other.x, self.y - other.y)
        else:
            return Vect2D(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vect2D):
            return Vect2D(self.x * other.x, self.y * other.y)
        else:
            return Vect2D(self.x * other, self.y * other)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError()


class TestVect2D:

    def test_1(self):
        v1 = Vect2D()
        v2 = Vect2D(1, 2)
        v1 += 1
        self.assertEqual(v1 + 1, v2 - Vect2D(0, 1))
        self.assertEqual(v1 * 4, v2 * Vect2D(4, 2))


if __name__ == '__main__':
    unittest.main()
