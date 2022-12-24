import const
import pygame
from const import SCREEN_SIZE
from src.UI.image import Image

class ImageDeath(Image):
    def __init__(self, center):
        super().__init__(center, pygame.transform.scale(const.IMAGE['start'][7], (SCREEN_SIZE[0], SCREEN_SIZE[1])))