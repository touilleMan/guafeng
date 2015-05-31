from ecs import Component


class BehaviorComponent(Component):

    def __init__(self):
        super().__init__()
        self.movement = 0
        self.jump_ = False
        self.speed = 100
        self.jump_velocity = 300

    def move_right(self):
        self.movement = 1

    def move_left(self):
        self.movement = -1

    def jump(self):
        self.jump_ = True

    def reset(self):
        self.movement = 0
        self.jump_ = False
