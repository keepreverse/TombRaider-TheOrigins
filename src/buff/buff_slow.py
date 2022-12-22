from src.buff.buff import Buff
"""
The buff which will make creature move slow for a while.
"""


class BuffSlow(Buff):
    def __init__(self, time, creature, level=1):
        super().__init__('Slow - ' + str(level), time, creature)
        self.level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError("BuffSlow.level must be int type.")
        elif not 1 <= value <= 4:
            raise ValueError("BuffSlow.level should be 1 to 4.")
        self.__level = value

    def take_effect(self):
        self.creature.speed_mag *= 1 - 0.2 * self.level

    def recover(self):
        self.creature.speed_mag /= 1 - 0.2 * self.level
