import var
from src.debuff.debuff import Debuff
from src.debuff.debuff_slow import DebuffSlow
from src.obj.entity.item.collectible import Collectible
"""
When use it, the player's health will increase.
It can't be used when player is in full health.
"""


class FoodBuff(Collectible):
    def __init__(self, name, image, amount):
        super().__init__(name, image, True, amount)

    @property
    def debuff(self):
        return self.__debuff

    @debuff.setter
    def debuff(self, value):
        if value is not None and not isinstance(value, Debuff):
            raise TypeError("Creature.debuff must be Debuff or None type.")
        if value is not None and var.player.debuff is not None:
            return
        self.__debuff = value

    def use(self):
        if var.player.debuff is not None:
            if var.player.debuff.name == "Changed (2 points)":
                return
            if var.player.debuff.name == "Changed (-2 points)":
                var.player.debuff.recover()
                var.player.debuff = None
                super().use()
                return
        super().use()
        var.player.debuff = DebuffSlow(500, var.player, 4)
