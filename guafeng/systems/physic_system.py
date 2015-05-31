from ecs import System

from guafeng.components import BehaviorComponent, PhysicComponent


class PhysicSystem(System):
    GRAVITY = (0, -900)

    def __init__(self, world):
        super().__init__()
        self._world = world

    def update(self, dt):
        for entity, physic in self.entity_manager.pairs_for_type(PhysicComponent):
            behavior = self.entity_manager.component_for_entity(entity, BehaviorComponent)
            if behavior.movement:
                physic.speed.x = behavior.movement * behavior.speed
            else:
                physic.speed.x = 0
            if physic.jumping:
                physic.speed.y -= 400 * dt
            elif behavior.jump_:
                physic.speed.y += behavior.jump_velocity
                physic.jumping = True
            behavior.reset()
            physic.pos += physic.speed * dt
