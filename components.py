import pyglet
import ecs

class Renderable(ecs.Component):
	"""Component that can be render on screen"""
	def __init__(self, sprite):
		super(Renderable, self).__init__()
		self.sprite = sprite

