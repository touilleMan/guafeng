from ecs import Component

from guafeng.tools import Vect2D
from guafeng.components.physic_component import PhysicComponent
from guafeng.components.camera_component import CameraComponent
from guafeng.components.input_component import InputComponent
from guafeng.components.behavior_component import BehaviorComponent
from guafeng.components.map_component import MapComponent


class RenderComponent(Component):

    """Component that can be rendered on screen"""

    def __init__(self, sprite):
        super().__init__()
        self.sprite = sprite
