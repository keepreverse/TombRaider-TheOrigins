import const
import pygame
from const import SCREEN_SIZE
from src.UI.image import Image

class ImageStart(Image):
    def __init__(self, center):
        super().__init__(center, pygame.transform.scale(const.IMAGE['start'][3], (SCREEN_SIZE[0], SCREEN_SIZE[1])))