from ecs import Component


class BehaviorComponent(Component):

    def __init__(self):
        super().__init__()
        self.movement = 0
        self._jump = False
        self.speed = 100
        self.jump_velocity = 30

    def move_right(self):
        self.movement = 1

    def move_left(self):
        self.movement = -1

    def jump(self):
        self._jump = True

    def reset(self):
        self.movement = 0
        self._jump = False
