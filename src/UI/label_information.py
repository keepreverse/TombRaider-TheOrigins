import var
from src.UI.label import Label
from src.obj.entity.item.armor import Armor
from src.obj.entity.item.treasure import Treasure
from src.obj.entity.item.weapon import Weapon


class LabelInformationName(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', color = (0, 0, 0), size=30, is_left_center=True)

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.text = 'Name: '
        else:
            self.text = 'Name: ' + var.bag.items[var.bag.active_item_id].name


class LabelInformationType(Label):
    def __init__(self, left_center, color = (0, 0, 0)):
        super().__init__(left_center, '', size=30, is_left_center=True, color = (0, 0, 0))

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.text = 'Type: '
        else:
            item = var.bag.items[var.bag.active_item_id]
            if isinstance(item, Armor):
                self.text = 'Type: ' + 'Armor'
            elif isinstance(item, Weapon):
                self.text = 'Type: ' + 'Weapon'
            elif isinstance(item, Treasure):
                self.text = 'Type: ' + 'Treasure'
            else:
                self.text = 'Type: ' + 'Item'


class LabelInformation1(Label):
    def __init__(self, left_center, color = (0, 0, 0)):
        super().__init__(left_center, '', size=27, is_left_center=True, color=(0, 0, 0))

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.text = ''
        else:
            self.text = var.bag.items[var.bag.active_item_id].information[0:68]


class LabelInformation2(Label):
    def __init__(self, left_center, color = (0, 0, 0)):
        super().__init__(left_center, '', size=27, is_left_center=True, color = (0, 0, 0))

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.text = ''
        else:
            self.text = var.bag.items[var.bag.active_item_id].information[68:136]


class LabelInformation3(Label):
    def __init__(self, left_center, color = (0, 0, 0)):
        super().__init__(left_center, '', size=27, is_left_center=True, color = (0, 0, 0))

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.text = ''
        else:
            self.text = var.bag.items[var.bag.active_item_id].information[136:204]
