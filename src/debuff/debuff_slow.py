from src.debuff.debuff import Debuff
"""
The debuff which will make creature move slow for a while.
"""


class DebuffSlow(Debuff):
    def __init__(self, time, creature, level=1):
        super().__init__("Changed (" + str(level) + " points)", time, creature)
        self.level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError("DebuffSlow.level must be int type.")
        elif not -3 <= value <= 4:
            raise ValueError("DebuffSlow.level should be -3 to 4.")
        self.__level = value

    def take_effect(self):
        self.creature.speed_mag *= 1 + 0.2 * self.level

    def recover(self):
        self.creature.speed_mag /= 1 + 0.2 * self.level