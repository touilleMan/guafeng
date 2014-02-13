import pyglet
import ecs
from tools import Vect2D

class Render(ecs.Component):
	"""Component that can be render on screen"""
	def __init__(self, sprite):
		super(Render, self).__init__()
		self.sprite = sprite

class Coordinates(ecs.Component):
	def __init__(self, x=0, y=0, dx=0, dy=0, ax=0, ay=0):
		super(Coordinates, self).__init__()
		self.position = Vect2D(x, y)
		self.speed = Vect2D(dx, dy)
		self.acceleration = Vect2D(ax, ay)

class Will(ecs.Component):
	def __init__(self):
		super(Will, self).__init__()
		self.right = False
		self.left = False
