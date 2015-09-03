import pyglet
import ecs
import pickle
from pyglet.window import key

from guafeng import archetypes
from guafeng import systems
from guafeng.components import InputComponent


class World:
    def __init__(self, path):
        self._handlers_args = []
        self._handlers_kwargs = {}
        self.window = pyglet.window.Window()

        entity_manager = ecs.EntityManager()
        self.entity_manager = entity_manager
        system_manager = ecs.SystemManager(entity_manager)

        render_system = systems.RenderSystem(self)
        input_system = systems.InputSystem(self)

        system_manager.add_system(render_system)
        system_manager.add_system(input_system)
        # system_manager.add_system(systems.MoveSystem())
        physic_system = systems.PhysicSystem(self)
        system_manager.add_system(physic_system)

        self.map = archetypes.create_map(entity_manager, system_manager)
        self.player = archetypes.create_player(entity_manager, system_manager)
        self.camera = archetypes.create_camera(entity_manager, system_manager)

        save_load = entity_manager.create_entity()
        input_sl = InputComponent()
        input_sl.add_keybind(key.F5, lambda: self.save())
        input_sl.add_keybind(key.F9, lambda: self.load())
        entity_manager.add_component(save_load, input_sl)

        # Start the pyglet application
        @self.window.event
        def on_draw():
            render_system.draw()
        pyglet.clock.schedule_interval(system_manager.update, 1 / 60)

    def register_handler(self, *args, **kwargs):
        self._handlers_args += args
        self._handlers_kwargs.update(kwargs)

    def start(self):
        # TODO: use handler stack
        self.window.push_handlers(*self._handlers_args, **self._handlers_kwargs)
        pyglet.app.run()
        self.window.pop_handlers()

    def save(self, name='save.gf'):
        with open(name, 'w') as fd:
            pickle.dump(self.entity_manager, fd)

    def load(self, name='save.gf'):
        with open(name, 'rb') as fd:
            self.entity_manager = pickle.load(fd)
