import pyglet
from pyglet.window import key

from guafeng.components import (RenderComponent, PhysicComponent,
                                BehaviorComponent, InputComponent)


BASE_MODULE_PATH = 'guafeng.models'
model_cache = {}


def tile_factory_create(world, x, y, width, height, image):
    tile = world.create_entity()
    world.add_component(tile, RenderComponent(
        pyglet.sprite.Sprite(image, batch=world.map.ground_batch, x=x, y=y)))
    physic = PhysicComponent(x, y, width, height, static=True)
    world.add_component(tile, physic)
    return tile, physic


def load_model(model_name):
    if model_name not in model_cache:
    #     splitted = model_name.rsplit('.', 1)
    #     if len(splitted) == 2:
    #         module_path, model_name = splitted
    #     else:
    #         module_path = ''
    #     module = __import__('.'.join([BASE_MODULE_PATH + module_path]))
    #     model_cache[model_name] = getattr(module, model_name)()
        model_cache[model_name] = eval(model_name)()
    return model_cache[model_name]


class Model:
    def factory_create(self, world):
        raise NotImplementedError()


class Beatle(Model):
    COLOR = (0x33, 0x00, 0xff, 255)

    def __init__(self):
        self.texture = pyglet.image.create(20, 50,
            pyglet.image.SolidColorImagePattern(self.COLOR))

    def factory_create(self, world, x, y, rot=0, properties=None):
        beatle = world.create_entity()
        render = RenderComponent(pyglet.sprite.Sprite(self.texture))
        world.add_component(beatle, render)
        world.add_component(beatle, PhysicComponent(x=x, y=y, width=20, height=50))
        world.add_component(beatle, BehaviorComponent())


class Hero(Model):
    COLOR = (0xff, 0x00, 0x66, 255)

    def __init__(self):
        self.texture = pyglet.image.create(20, 50,
            pyglet.image.SolidColorImagePattern(self.COLOR))

    def factory_create(self, world, x, y, rot=0, properties=None):
        player = world.create_entity()
        render = RenderComponent(pyglet.sprite.Sprite(self.texture))
        world.add_component(player, render)
        world.add_component(player, PhysicComponent(x=x, y=y, width=20, height=50))
        world.player = player

        # Build key mapping
        behavior = BehaviorComponent()
        world.add_component(player, behavior)

        input_c = InputComponent()
        input_c.add_keybind(key.LEFT, behavior.move_left)
        input_c.add_keybind(key.RIGHT, behavior.move_right)
        input_c.add_keybind(key.SPACE, behavior.jump)
        world.add_component(player, input_c)

        return player
