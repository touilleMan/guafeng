from ecs import Component


class CameraComponent(Component):

    def __init__(self, x=0, y=0, active=True):
        """x,y : world coordinates of the camera"""
        super().__init__()
        self.active = active
        self.gl_translate = [0, 0, 0]

    @property
    def position(self):
        return (-self.gl_translate[0], -self.gl_translate[1])

    @position.setter
    def position(self, x, y):
        self.gl_translate = [-x, -y, 0]

    def move(self, x=0, y=0):
        self.gl_translate[0] -= x
        self.gl_translate[1] -= y
