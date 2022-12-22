from pygame.font import SysFont

import var
from src.UI.label import Label


class LabelHP(Label):
    def __init__(self, left_center):
        super().__init__(left_center, "", size=30, is_left_center=True)

    def update(self):
        if var.player is not None:
            self.text = 'HP: ' + str(var.player.health) + ' / ' + str(var.player.max_health)
