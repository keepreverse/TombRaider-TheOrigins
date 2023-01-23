from pygame.font import SysFont

import var
from src.UI.label import Label


class LabelBullet(Label):
    def __init__(self, left_center):
        super().__init__(left_center, "", size=30, is_left_center=True)

    def update(self):
        if var.player != None:
            if var.bag.weapon.remain >= 10:
                self.text = 'Bullet:   ' + str(var.bag.weapon.remain) + ' / ' + str(var.bag.weapon.clip)
            else:
                self.text = 'Bullet:    ' + str(var.bag.weapon.remain) + ' / ' + str(var.bag.weapon.clip)
