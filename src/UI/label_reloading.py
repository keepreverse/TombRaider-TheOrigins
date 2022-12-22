import var
from src.UI.label import Label


class LabelReloading(Label):
    def __init__(self, center):
        super().__init__(center, "", size=20)

    def update(self):
        if var.bag.weapon.remain == 0:
            if not var.bag.has_bullet:
                self.text = 'No bullet'
            else:
                self.text = 'Reloading..'
        else:
            self.text = ''

