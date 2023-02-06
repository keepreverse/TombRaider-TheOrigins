import var
import const
import pygame
from const import Init, SOUND, SCREEN_SIZE
from src.UI.button import Button
from src.UI.interface_loading import LOADING


class ButtonTryAgain(Button):
    def __init__(self, center):
        super().__init__(center, None, pygame.transform.scale(const.IMAGE['start'][10], (SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/20)), pygame.transform.scale(const.IMAGE['start'][11], (SCREEN_SIZE[0]/6, SCREEN_SIZE[1]/20)))

    def on_available(self):
        self.image = self.images[1]

    def on_hover(self):
        self.image = self.images[0]

    def on_click(self):
        self.image = self.images[1]
        var.interface = var.loading = LOADING()
        Init.init_music(SOUND, "game", 0.15)
