import pygame
import os
import var
from src.animation.animation_repository import AnimationRepository

"""
The file store the constant object or variable.
"""

# Screen pixel size.
SCREEN_SIZE = (1920, 1080)
# Room consist of many tiles. It's one tile's size on pixel.
TILE_SIZE = (35, 35)
# The room consist of 20 * 20 tiles on width and height.
ROOM_SIZE = (int(SCREEN_SIZE[0]/60) - 1, int(SCREEN_SIZE[0]/60) - 2)
# The map consist of maximum 6 * 6 room on width and height.
MAP_SIZE = (6, 6)
FPS = 60
MAX_ENEMY = 10
MIN_ENEMY = 1
# Use for quad tree
ENTITY_CAPACITY = 5
# The door position in the room.
DOOR_POS = {'left': (2, ROOM_SIZE[1] // 2), 'right': (ROOM_SIZE[0] - 3, ROOM_SIZE[1] // 2),
            'up': (ROOM_SIZE[0] // 2, 2), 'down': (ROOM_SIZE[0] // 2, ROOM_SIZE[1] - 3)}
# The portal position relative to the door position in the room.
PORTAL_POS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
# Store all the image.
IMAGE = {}
# Store all the sound.
SOUND = {}
TEST = {}
# Store the legal state for a creature.
LEGAL_STATE = ["stand_left", "stand_right", "move_up", "move_down", "move_right", "move_left"]
# The animation repository, it store all the animation.
ANIMATION_REPOSITORY = None


# Load the image and sound, initialize the animation repository.
class Init:
    global ANIMATION_REPOSITORY
    def __init__(self):
        self.scale = pygame.transform.scale
        self.load = pygame.image.load

    def init_creature(self, image, legal_state, name, scale_value):
        image[name] = {}
        for state in legal_state:
            image[name][state] = []
            i = 0
            while os.path.exists("data/image/creature/%s/%s/%d.png" % (name, state, i)):
                tmp_image = self.load("data/image/creature/%s/%s/%d.png" % (name, state, i))
                tmp_width = round(scale_value * tmp_image.get_width())
                tmp_height = round(scale_value * tmp_image.get_height())
                image[name][state].append(self.scale(tmp_image, (tmp_width, tmp_height)).convert_alpha())
                i += 1

    def init_music(sound, name, volume):
        pygame.mixer.init()
        pygame.mixer.music.load('data/music/%s.mp3' % name)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)


    def init_obj(self, name, number, is_alpha=False):
        if is_alpha:
            IMAGE[name] = [self.load("data/image/%s/%d.png" % (name, i)).convert_alpha() for i in range(number)]
        else:
            IMAGE[name] = [self.load("data/image/%s/%d.png" % (name, i)).convert() for i in range(number)]
 
# pygame initialization
pygame.init()
pygame.display.set_caption('Tomb Raider: Old Times')
# Initialize the screen
var.screen = pygame.display.set_mode(SCREEN_SIZE)
init = Init()
init.init_obj('ground', 8)
init.init_obj('wall', 6, is_alpha=True)
init.init_obj('chest', 2)
init.init_obj('potion', 1, is_alpha=True)
init.init_obj('trap', 6)
init.init_obj('door', 6, is_alpha=True)
init.init_obj('key', 1, is_alpha=True)
init.init_obj('bullet', 1, is_alpha=True)
init.init_obj('armor', 6, is_alpha=True)
init.init_obj('weapon', 5, is_alpha=True)
init.init_obj('treasure', 1, is_alpha=True)
init.init_obj('start', 13, is_alpha=True)
init.init_creature(IMAGE, LEGAL_STATE, "player", 2)
init.init_creature(IMAGE, LEGAL_STATE, "guard", 2)
init.init_creature(IMAGE, LEGAL_STATE, "mummy", 2)
init.init_creature(IMAGE, LEGAL_STATE, "pharaoh", 2)
Init.init_music(SOUND, "menu", 0.2)
ANIMATION_REPOSITORY = AnimationRepository()