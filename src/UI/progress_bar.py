import pygame
from pygame import Color
from pygame.surface import Surface
from src.UI.component import Component
"""
Set the progress to adjust the bar.
"""


class ProgressBar(Component):
    def __init__(self, center, size, length,
                 border_color=(255, 255, 255), inactive_color=(100, 100, 100), active_color=(255, 255, 255)):
        super().__init__(center)
        self.rect.size = size
        self.rect.center = center
        self.__surface = Surface(size)
        self.__length = int(length)
        self.__border_color = border_color
        self.__inactive_color = inactive_color
        self.__active_color = active_color
        self.__progress = 0

    @property
    def length(self):
        return self.__length

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        if not isinstance(value, int):
            raise TypeError("ProgressBar.progress must be int type.")
        elif not 0 <= value <= self.length:
            raise ValueError("ProgressBar.progress must less or equal to %d." % self.length)
        self.__progress = value

    @property
    def active_color(self):
        return self.__active_color

    @active_color.setter
    def active_color(self, value):
        self.__active_color = Color(value)

    @property
    def image(self):
        self.__surface.fill(self.__inactive_color)
        pygame.draw.rect(self.__surface, self.__active_color,
                         (0, 0, self.rect.width // self.length * self.progress, self.rect.height))
        pygame.draw.rect(self.__surface, self.__border_color, self.__surface.get_rect(), int(self.rect.height // 10))
        return self.__surface.copy()

    @image.setter
    def image(self, value):
        pass
