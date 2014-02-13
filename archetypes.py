import pyglet
import components

# dummy image 
PLAYER_COLOR=(0xff, 0x00, 0x66, 255)
PLAYER_IMAGE=pyglet.image.create(20, 50,
	pyglet.image.SolidColorImagePattern(PLAYER_COLOR))

def create_player(entity_manager):
	player = entity_manager.create_entity()
	player_render = components.Render(pyglet.Sprite(PLAYER_IMAGE))
	entity_manager.add_component(player, player_render)
	player_coordinates = components.Coordinates()
	entity_manager.add_component(player, player_coordinates)
	entity_manager.add_component(player, components.Will())
	return player
