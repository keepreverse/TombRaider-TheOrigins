import pygame
import var
from const import SCREEN_SIZE
from src.UI.image_map import ImageMap
from src.UI.interface import Interface
from src.UI.label_bullet import LabelBullet
from src.UI.label_hp import LabelHP
from src.UI.label_hp_bar import LabelHPBar
from src.UI.label_bullet_bar import LabelBulletBar
from src.UI.progress_bar_bullet import ProgressBarBullet
from src.UI.progress_bar_hp import ProgressBarHP
from src.UI.label_debuff import LabelDebuffName, LabelDebuffTime
from src.UI.interface_pause import PAUSE
from src.UI.interface_death import DEATH



"""
Control the map.
"""

class PLAY(Interface):
    def __init__(self):
        super().__init__(ImageMap((SCREEN_SIZE[0]/1.15, SCREEN_SIZE[1]/5)), LabelHP((20, 50)), ProgressBarHP((147, 48)), LabelHPBar((147, 50)),
                         LabelBullet((20, 80)), ProgressBarBullet((147, 78)), LabelBulletBar((147, 80)),
                         LabelDebuffName((20, 110)), LabelDebuffTime((20, 140)))

    def update(self):
        var.map.update()
        super().update()
        for event in var.key_down:
            if event.key == pygame.K_ESCAPE:
                var.player.refresh()
                var.interface = var.pause = PAUSE()
                var.pause.refresh()
        if var.player.is_dead:
            var.interface = var.death = DEATH()

    def draw(self, surface):
        var.map.active_room.draw(surface)
        super().draw(surface)
