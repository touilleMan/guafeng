from ecs import models

class Renderable(Component):
	"""Component that can be render on screen"""
	def __init__(self, sprite):
		super(Renderable, self).__init__()
		self.sprite = sprite
