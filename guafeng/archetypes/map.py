import pyglet
from pyglet.window import key
# import pymunk

from guafeng import components
from guafeng.components import (RenderComponent, CameraComponent,
                                InputComponent, BehaviorComponent, PhysicComponent)
from guafeng import systems


def create_map(entity_manager, system_manager):
    pass
    
    # physic_system = system_manager._system_types[systems.PhysicSystem]
    # space = physic_system.space
    # # static = [pymunk.Segment(space.static_body, (0, 0), (300, 0), 5)]
    # static = [pymunk.Segment(space.static_body, (0, 0), (1000, 0), 5),
    #           pymunk.Segment(space.static_body, (0, 0), (0, 200), 5),
    #           pymunk.Segment(space.static_body, (1000, 0), (1000, 200), 5)]
    # space.add(static)
