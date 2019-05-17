import libtcodpy as libtcod

import os

from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder


def kill_player(player):
# Delete savegame file upon death to force player to start over
	if not os.path.isfile('savegame.dat'):
		pass
	else:
		os.remove('savegame.dat')
	player.char = 180
	player.color = libtcod.dark_red

	return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD

def kill_monster(monster):
	death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

	monster.char = 180
	monster.color = libtcod.dark_red
	monster.blocks = False
	monster.fighter = None
	monster.ai = None
	monster.name = 'remains of ' + monster.name
	monster.render_order = RenderOrder.CORPSE

	return death_message