import pygame
import os
from src.animation.animation_repository import AnimationRepository
"""
The file store the constant object or variable.
"""
# Screen pixel size.
SCREEN_SIZE = (1920, 1080)
# Room consist of many tiles. It's one tile's size on pixel.
TILE_SIZE = (36, 36)
# The room consist of 20 * 20 tiles on width and height.
ROOM_SIZE = (20, 20)
# The map consist of maximum 6 * 6 room on width and height.
MAP_SIZE = (6, 6)
FPS = 60
MAX_ENEMY = 10
MIN_ENEMY = 2
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
# Store the legal state for a creature.
LEGAL_STATE = ["stand_left", "stand_right", "move_up", "move_down", "move_right", "move_left"]
# The animation repository, it store all the animation.
ANIMATION_REPOSITORY = None


# Load the image and sound, initialize the animation repository.
def init():
    global ANIMATION_REPOSITORY
    scale = pygame.transform.scale
    load = pygame.image.load

    def init_creature(image, legal_state, name, scale_value):
        image[name] = {}
        for state in legal_state:
            image[name][state] = []
            i = 0
            while os.path.exists("data/image/creature/%s/%s/%d.png" % (name, state, i)):
                tmp_image = load("data/image/creature/%s/%s/%d.png" % (name, state, i))
                tmp_width = round(scale_value * tmp_image.get_width())
                tmp_height = round(scale_value * tmp_image.get_height())
                image[name][state].append(scale(tmp_image, (tmp_width, tmp_height)).convert_alpha())
                i += 1

    def init_music(sound, name, volume):
        pygame.mixer.init()
        pygame.mixer.music.load('data/music/%s.wav' % name)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)


    def init_obj(name, number, is_alpha=False):
        if is_alpha:
            if (name == 'start') & (number == 3):
                IMAGE[name] = [scale(load("data/image/start/3.png"), (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2).convert_alpha())]
            else:
                IMAGE[name] = [load("data/image/%s/%d.png" % (name, i)).convert_alpha() for i in range(number)]

        else:
            if (name == 'start') & (number == 3):
                IMAGE[name] = [scale(load("data/image/start/3.png"), (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2).convert())]
            else:
                IMAGE[name] = [load("data/image/%s/%d.png" % (name, i)).convert() for i in range(number)]
 

    init_obj('ground', 8)
    init_obj('wall', 6, is_alpha=True)
    init_obj('chest', 3)
    init_obj('potion', 1, is_alpha=True)
    init_obj('trap', 6)
    init_obj('door', 6, is_alpha=True)
    init_obj('key', 1, is_alpha=True)
    init_obj('bullet', 1, is_alpha=True)
    init_obj('armor', 6, is_alpha=True)
    init_obj('weapon', 5, is_alpha=True)
    init_obj('treasure', 1, is_alpha=True)
    init_obj('start', 7, is_alpha=True)
    init_creature(IMAGE, LEGAL_STATE, "player", 2)
    init_creature(IMAGE, LEGAL_STATE, "guard", 2)
    init_creature(IMAGE, LEGAL_STATE, "mummy", 2)
    init_creature(IMAGE, LEGAL_STATE, "pharaoh", 2)
    #init_music(SOUND, "bgm", 0.1)
    ANIMATION_REPOSITORY = AnimationRepository()
