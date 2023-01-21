import var
import const
import pygame
from const import SCREEN_SIZE
from src.UI.button import Button
from src.UI.interface_option import OPTION


class ButtonOption(Button):
    def __init__(self, center):
        super().__init__(center, None, pygame.transform.scale(const.IMAGE['start'][1], (SCREEN_SIZE[0] / 7.1, SCREEN_SIZE[1] / 20)), pygame.transform.scale(const.IMAGE['start'][5], (SCREEN_SIZE[0] / 7.1, SCREEN_SIZE[1] / 20)))

    def on_available(self):
        self.image = self.images[1]

    def on_hover(self):
        self.image = self.images[0]

    def on_click(self):
        self.image = self.images[1]
        var.interface = var.option = OPTION()
