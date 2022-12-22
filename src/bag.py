from src.obj.entity.item.armor import Armor
from src.obj.entity.item.armor5_15 import Armor5
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.key import Key
from src.obj.entity.item.potion import Potion
from src.obj.entity.item.weapon import Weapon
from src.obj.entity.item.weapon7_15 import Weapon7
"""
The bag.
All the operation of the bag is in O(n) time complexity.
"""


class Bag:
    def __init__(self):
        self.__items = [Bullet(40), Key(3), Potion(2)]
        self.__has_bullet = True
        self.__has_key = True
        self.__has_treasure = False
        self.active_item_id = 0
        # Initial weapon the armor.
        self.weapon = Weapon7()
        self.armor = Armor5()

    @property
    def items(self):
        return self.__items

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        if not isinstance(value, Weapon):
            raise TypeError("Bag.weapon must be weapon type.")
        self.__weapon = value

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        if not isinstance(value, Armor):
            raise TypeError("Bag.armor must be Armor type.")
        self.__armor = value

    @property
    def active_item_id(self):
        return self.__active_item_id

    @active_item_id.setter
    def active_item_id(self, value):
        if not 0 <= value <= 7:
            raise ValueError("Bag.active_item_id must from 0 to 7.")
        self.__active_item_id = value

    @property
    def has_key(self):
        return self.__has_key

    @property
    def has_bullet(self):
        return self.__has_bullet

    @property
    def has_treasure(self):
        return self.__has_treasure

    def add_item(self, collectible):
        if isinstance(collectible, (Armor, Weapon)):
            if len(self.__items) < 8:
                self.__items.append(collectible)
                return True
            else:
                return False
        else:
            for item in self.__items:
                if item.name == collectible.name:
                    item.amount += collectible.amount
                    return True
            if len(self.__items) < 8:
                self.__items.append(collectible)
                if not self.has_key and collectible.name == 'Key':
                    self.__has_key = True
                if not self.has_bullet and collectible.name == 'Bullet':
                    self.__has_bullet = True
                if not self.has_treasure and collectible.name == 'Treasure':
                    self.__has_treasure = True
                return True
            else:
                return False

    def remove_item(self, collectible):
        if isinstance(collectible, (Armor, Weapon)):
            for _, item in enumerate(self.__items):
                if item.name == collectible.name:
                    self.__items.pop(_)
                    return True
        else:
            for _, item in enumerate(self.__items):
                if item.name == collectible.name:
                    if item.amount > collectible.amount:
                        item.amount -= collectible.amount
                        return True
                    elif item.amount == collectible.amount:
                        if item.name == 'Bullet':
                            self.__has_bullet = False
                        elif item.name == 'Key':
                            self.__has_key = False
                        elif item.name == 'Treasure':
                            self.__has_treasure = False
                        self.__items.pop(_)
                        return True
                    else:
                        return False
        return False
