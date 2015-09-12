from pytmx.util_pyglet import load_pyglet
from pytmx import TiledObjectGroup, TiledTileLayer
import pyglet
import pyqtree

from guafeng.models import load_model, tile_factory_create


class TileMap:
    def __init__(self, width, height, tile_width, tile_height):
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.map = [[None for _ in range(width)] for _ in range(height)]

    def add_tile(self, tile, x, y):
        self.map[y][x] = tile

    def closest_collision_tile(self, x, y, dx, dy, max_x=None, max_y=None):
        tx = int(x / self.tile_width)
        ty = int(y / self.tile_height)
        if dx:
            tile_x = next((tile for tile in self.map[ty][tx:] if tile), None)
        else:
            tile_x = next((tile for tile in reversed(self.map[ty][:tx])
                           if tile), None)
        if dy:
            tile_y = next((row[tx] for row in self.map[ty:] if row[tx]), None)
        else:
            tile_y = next((row[tx] for row in reversed(self.map[:ty])
                           if row[tx]), None)
        if tile_x is not None and max_x is not None and abs(x - tile_x * self.tile_width) > max_x:
            tile_x = None
        if tile_y is not None and max_y is not None and abs(y - tile_y * self.tile_height) > max_y:
            tile_y = None
        return tile_x, tile_y


class Map:
    def __init__(self):
        self.ground_batch = pyglet.graphics.Batch()
        self.sprites = []
        self.cells = []
        self.tilemap = None
        self.quadtree = None


class MapModel:
    def __init__(self, path):
        self.tmx = load_pyglet(path)
        assert self.tmx.orientation == 'orthogonal'

    def factory_create(self, world):
        # Insert living stuff into the game
        world.map = Map()
        self._load_ground(world, self.tmx.layernames['tiles-ground'])
        self._load_living(world, self.tmx.layernames['objs-living'])

    def _load_living(self, world, layer):
        assert isinstance(layer, TiledObjectGroup)
        h = self.tmx.tileheight * self.tmx.height
        for obj in layer:
            model = load_model(obj.type)
            print(obj.name, model.__class__.__name__, obj.x, h - obj.y)
            model.factory_create(world, x=obj.x, y=h - obj.y,
                                 rot=obj.rotation, properties=obj.properties)

    def _load_ground(self, world, layer):
        assert isinstance(layer, TiledTileLayer)
        tmx = self.tmx
        tw = tmx.tilewidth
        th = tmx.tileheight
        mh = tmx.height - 1
        world.tilemap = TileMap(tmx.width, tmx.height, tw, th)
        map_width = tw * tmx.width
        map_height = th * tmx.height
        world.map.quadtree = pyqtree.Index(bbox=(0, 0, map_width, map_height))
        # Create each cells of the map
        # iterate over the tiles in the layer
        for x, y, image in layer.tiles():
            yy = (mh - y) * th
            xx = x * tw
            tile = tile_factory_create(world, xx, yy, tw, th, image)
            world.tilemap.add_tile(tile, x, y)
            print('tile:', (xx, yy, xx + tw, yy + th))
            world.map.quadtree.insert(item=tile, bbox=(xx, yy, xx + tw, yy + th))
