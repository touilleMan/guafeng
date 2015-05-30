from ecs import System
# import pymunk

from guafeng.components import BehaviorComponent, PhysicComponent


class MoveSystem(System):

    def __init__(self):
        super().__init__()

    def update(self, dt):
        for entity, behavior in self.entity_manager.pairs_for_type(BehaviorComponent):
            physic = self.entity_manager.component_for_entity(entity, PhysicComponent)
            if behavior.movement:
                physic.body.velocity.x = behavior.movement * behavior.speed
            else:
                physic.body.velocity.x = 0
            if behavior._jump and not physic.jumping:
                physic.body.velocity.y += behavior.jump_velocity
            behavior.reset()


class PhysicSystem(System):
    GRAVITY = (0, -900)

    def __init__(self):
        super().__init__()
        # self.space = pymunk.Space()
        # self.space.gravity = self.GRAVITY

    def update(self, dt):
        for entity, physic in self.entity_manager.pairs_for_type(PhysicComponent):
            behavior = self.entity_manager.component_for_entity(entity, BehaviorComponent)
            if behavior.movement:
                physic.speed.x = behavior.movement * behavior.speed
            else:
                physic.speed.x = 0
            behavior.reset()
            physic.pos += physic.speed * dt
            # physic.speed += physic.acc * dt
            # if behavior._jump and not physic.jumping:
            #     physic.body.velocity.y += behavior.jump_velocity
        # self.space.step(dt)
