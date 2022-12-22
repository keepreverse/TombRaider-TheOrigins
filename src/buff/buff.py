"""
Only creature has the buff instance.
It's an abstract base class, you should not add it to the creature directly.
Update() should be called every frame.
"""


class Buff:
    def __init__(self, name, time, creature=None):
        self.__name = name
        self.time = time
        self.__creature = creature
        self.__flag = True

    @property
    def name(self):
        return self.__name

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = int(value)

    @property
    def creature(self):
        return self.__creature

    def update(self):
        if self.creature is None or self.time == 0:
            return
        if self.__flag:
            self.__flag = False
            self.take_effect()
        self.time -= 1

    def take_effect(self):
        pass

    def recover(self):
        pass
