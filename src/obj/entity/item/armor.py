import var
from src.obj.entity.item.collectible import Collectible
"""
The Armor only has one attribute defense.
It can be used in the bag, the same as be equipped. 
Only the player has armor.
"""


class Armor(Collectible):
    def __init__(self, name, image, defense):
        super().__init__(name, image, True)
        self.defense = defense

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value <= 0:
            raise ValueError("Armor.defense can't less than zero.")
        self.__defense = int(value)

    def use(self):
        var.bag.remove_item(self)
        var.bag.add_item(var.bag.armor)
        var.bag.armor = self


