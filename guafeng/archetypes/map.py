from os import path
import pyglet
from pyglet.window import key

from guafeng import components
from guafeng.components import (RenderComponent, CameraComponent, MapComponent,
                                InputComponent, BehaviorComponent, PhysicComponent)
from guafeng import systems


MAP = path.dirname(__file__) + '/../../data/map_01.tmx'
def create_map(entity_manager, system_manager):
    entity_manager.add_component(None, MapComponent(MAP))
    # physic_system = system_manager._system_types[systems.PhysicSystem]
    # space = physic_system.space
    # # static = [pymunk.Segment(space.static_body, (0, 0), (300, 0), 5)]
    # static = [pymunk.Segment(space.static_body, (0, 0), (1000, 0), 5),
    #           pymunk.Segment(space.static_body, (0, 0), (0, 200), 5),
    #           pymunk.Segment(space.static_body, (1000, 0), (1000, 200), 5)]
    # space.add(static)
