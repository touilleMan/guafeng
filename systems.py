from ecs import models

import components

class Renderer(System):
	"""Renderer"""

	def __init__(self):
		super(Render, self).__init__()

	def update(self, dt):
        for entity, renderable_component in \
        	self.entity_manager.pairs_for_type(Renderable):
                renderable_component.sprite.draw()
