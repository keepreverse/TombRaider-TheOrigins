import pygame
import var
from const import SCREEN_SIZE
from src.UI.image_map import ImageMap
from src.UI.interface import Interface
from src.UI.label_bullet import LabelBullet
from src.UI.label_hp import LabelHP
from src.UI.label_reloading import LabelReloading
from src.UI.progress_bar_bullet import ProgressBarBullet
from src.UI.progress_bar_hp import ProgressBarHP
"""
Control the map.
"""

class PLAY(Interface):
    def __init__(self):
        super().__init__(ImageMap((SCREEN_SIZE[0]/1.35, SCREEN_SIZE[1]/5)), LabelHP((20, 50)), ProgressBarHP((110, 48)),
                         LabelBullet((20, 80)), ProgressBarBullet((140, 78)), LabelReloading((140, 80)))

    def update(self):
        var.map.update()
        super().update()
        for event in var.key_down:
            if event.key == pygame.K_ESCAPE:
                var.player.refresh()
                var.interface = var.pause
                var.pause.refresh()
        if var.player.is_dead:
            var.interface = var.death

    def draw(self, surface):
        var.map.active_room.draw(surface)
        super().draw(surface)
