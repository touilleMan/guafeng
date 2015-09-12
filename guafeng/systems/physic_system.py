from ecs import System
from copy import deepcopy

from guafeng.components import BehaviorComponent, PhysicComponent


class PhysicSystem(System):

    def __init__(self, world):
        super().__init__()
        self._world = world
        self.components = []

    def update(self, dt):
        quadtree = deepcopy(self._world.map.quadtree)
        entities = [(e, p) for e, p in self.entity_manager.pairs_for_type(PhysicComponent)]
        for e, p in entities:
            quadtree.insert(item=(e, p), bbox=(p.pos.x, p.pos.y, p.pos.x + p.width, p.pos.y + p.height))
        for entity, physic in entities:
            if physic.static:
                continue
            behavior = self.entity_manager.component_for_entity(entity, BehaviorComponent)
            if behavior.movement:
                physic.speed.x = behavior.movement * behavior.speed
            else:
                physic.speed.x = 0
            if physic.jumping:
                if physic.speed.y > -500:
                    physic.speed.y -= 400 * dt
            elif behavior.jump_:
                physic.speed.y += behavior.jump_velocity
                physic.jumping = True
            behavior.reset()
            move = physic.speed * dt
            if physic.speed.x < 0:
                # move.x is < 0
                aabb_xmin = physic.min_x + move.x
                aabb_xmax = physic.max_x
            else:
                aabb_xmin = physic.min_x
                aabb_xmax = physic.max_x + move.x
            if physic.speed.y < 0:
                aabb_ymin = physic.min_y + move.y
                aabb_ymax = physic.max_y
            else:
                aabb_ymin = physic.min_y
                aabb_ymax = physic.max_y + move.y
            matches = quadtree.intersect((aabb_xmin, aabb_ymin, aabb_xmax, aabb_ymax))
            physic.pos += physic.speed * dt
            if len(matches) == 1:
                pass
            else:
                # Need to correct the movement according to collisions
                for match_entity, match_physic in matches:
                    if match_entity is entity:
                        continue
                    delta = physic.collides_with(match_physic, hint_vector=physic.speed)
                    if delta:
                        physic.pos -= delta
                        if delta.y < 0:
                            physic.jumping = False
                            physic.speed.y = 0

            # tile_x, tile_y = self._world.tilemap.closest_collision_tile(
            #     physic.pos.x, physic.pos.y,
            #     physic.speed.x, physic.speed.y,
            #     move.x, move.y)
            # if not tile_x:
            #     physic.pos.x += move.x
            # if not tile_y:
            #     physic.pos.y += move.y

            # physic.pos += physic.speed * dt
            # for component in self.components:
            #     if component is physic:
            #         continue
            #     collision = physic.collides_with(component, physic.speed)
            #     if collision:
            #         physic.pos -= collision
