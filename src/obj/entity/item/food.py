import var
from src.obj.entity.item.collectible import Collectible
"""
When use it, the player's health will increase.
It can't be used when player is in full health.
"""


class Food(Collectible):
    def __init__(self, name, image, amount, recover_health):
        super().__init__(name, image, True, amount)
        self.recover_health = recover_health

    @property
    def can_use(self):
        return var.player.health != var.player.max_health

    @can_use.setter
    def can_use(self, value):
        pass

    @property
    def recover_health(self):
        return self.__recover_health

    @recover_health.setter
    def recover_health(self, value):
        self.__recover_health = int(value)

    def use(self):
        if var.player.health == var.player.max_health:
            return
        super().use()
        var.player.health += self.recover_health
