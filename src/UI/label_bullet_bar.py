import var
from src.UI.label import Label


class LabelBulletBar(Label):
    def __init__(self, center):
        super().__init__(center, "", size=23)

    def update(self):
        if var.player is not None:
            if var.bag.weapon.remain:
                self.text = str(var.bag.weapon.remain) + ' / ' + str(var.bag.weapon.clip)
            else:
                if not var.bag.has_bullet:
                    self.text = 'NO AMMO'
                else:
                    self.text = 'RELOAD'