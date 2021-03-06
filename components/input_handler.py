#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  input_handler.py
#  
#  Copyright 2019 Bonzu <bonzupii@protonmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  
#  
import tcod as libtcod

from components.game_states import GameStates

def handle_keys(key, game_state):
	if game_state == GameStates.PLAYERS_TURN:
		return handle_player_turn_keys(key)
	elif game_state == GameStates.PLAYER_DEAD:
		return handle_player_dead_keys(key)
	elif game_state == GameStates.TARGETING:
		return handle_targeting_keys(key)
	elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
		return handle_inventory_keys(key)
	elif game_state == GameStates.LEVEL_UP:
		return handle_level_up_menu(key)
	elif game_state == GameStates.CHARACTER_SCREEN:
		return handle_character_screen(key)
		
	return {}

def handle_player_turn_keys(key):
	key_char = chr(key.c)
	
	# Movement keys
	if key.vk == libtcod.KEY_UP or key_char == 'k': # UP
		return {'move': (0, -1)}
	elif key.vk == libtcod.KEY_DOWN or key_char == 'j': # DOWN
		return {'move': (0, 1)}
	elif key.vk == libtcod.KEY_LEFT or key_char == 'h': # LEFT
		return {'move': (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT or key_char == 'l': # RIGHT
		return {'move': (1, 0)} 
	elif key_char == 'y': # UP LEFT
		return {'move': (-1, -1)}
	elif key_char == 'u': # UP RIGHT
		return {'move': (1, -1)}
	elif key_char == 'b': # DOWN LEFT
		return {'move': (-1, 1)}
	elif key_char == 'n': # DOWN RIGHT
		return {'move': (1, 1)}
	elif key_char == 'z': # HOLD POSITION FOR 1 TURN
		return {'wait': True}

	if key_char == 'g':
		return {'pickup': True}
		
	elif key_char == 'i':
		return {'show_inventory': True}
		
	elif key_char == 'd':
		return {'drop_inventory': True}
		
	elif key_char == '.':
		return {'take_trail': True}
		
	elif key_char == 'c':
		return {'show_character_screen': True}
		
	elif key_char == 's':
		return {'checkpoint': True}
		
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: Toggle full screen
		return {'fullscreen': True}
	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the game
		return {'exit': True}

	# No key was pressed
	return {}
	
def handle_targeting_keys(key):
	if key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}
		
	return {}
	
def handle_player_dead_keys(key):
	key_char = chr(key.c)
	
	if key_char == 'i':
		return {'show_inventory': True}
		
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: Toggle full screen
		return {'fullscreen': True}
	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the game
		return {'exit': True}
		
	return {}
	
def handle_mouse(mouse):
	(x, y) = (mouse.cx, mouse.cy)
	
	if mouse.lbutton_pressed:
		return {'left_click': (x, y)}
	elif mouse.rbutton_pressed:
		return {'right_click': (x, y)}
		
	return {}

def handle_inventory_keys(key):
	index = key.c - ord('a')
	
	if index >= 0:
		return {'inventory_index': index}
		
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		# Alt+Enter: Toggle full screen
		return {'fullscreen': True}
	elif key.vk == libtcod.KEY_ESCAPE:
		# Exit the menu
		return {'exit': True}
		
	return {}

def handle_main_menu(key):
	key_char = chr(key.c)
	
	if key_char == 'a':
		return {'new_game': True}
	elif key_char == 'b':
		return {'load_game': True}
	elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}

	return {}
	
def handle_level_up_menu(key):
	if key:
		key_char = chr(key.c)
		
		if key_char == 'a':
			return {'level_up': 'hp'}
		elif key_char == 'b':
			return {'level_up': 'str'}
		elif key_char == 'c':
			return {'level_up': 'def'}
			
	return {}

def handle_character_screen(key):
	key_char = chr(key.c)
	
	if key.vk == libtcod.KEY_ESCAPE or key_char == 'c':
		return {'exit': True}
		
	return {}
