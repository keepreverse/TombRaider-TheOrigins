from pygame.font import SysFont

import var
from src.UI.label import Label


class LabelBullet(Label):
    def __init__(self, left_center):
        super().__init__(left_center, "", size=30, is_left_center=True)

    def update(self):
        if var.player is not None:
            self.text = 'Bullet: ' + str(var.bag.weapon.remain) + ' / ' + str(var.bag.weapon.clip)
            return ''
