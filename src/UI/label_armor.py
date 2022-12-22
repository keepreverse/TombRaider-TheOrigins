import var
from src.UI.label import Label


class LabelArmorName(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Name: ' + var.bag.armor.name


class LabelArmorDefense(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Defense: ' + str(var.bag.armor.defense)
