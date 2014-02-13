import pyglet
import ecs
from tools import Vect2D

class Render(ecs.Component):
	"""Component that can be render on screen"""
	def __init__(self, sprite):
		super(Renderable, self).__init__()
		self.sprite = sprite

class Coordinate(ecs.Component):
	""""""
	def __init__(self, x=0, y=0, dx=0, dy=0, ax=0, ay=0):
		super(Renderable, self).__init__()
		self.pos = Vect2D(x, y)
		self.speed = Vect2D(dx, dy)
		self.acceleration = Vect2D(ax, ay)
