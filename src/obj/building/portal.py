import var
from src.obj.building.trigger_building import TriggerBuilding
"""
It's transparent.
When player collide with it, player will be put into the corresponding room.
"""


class Portal(TriggerBuilding):
    def __init__(self, pos, to):
        """
        :param pos: Vector.
        :param to: str. It has four value. left, right, up, down, represent the direction it will go.
        """
        super().__init__(pos, None, (0, 0), False, False, None, (0, 0))
        self.to = to

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        if value == 'left' or value == 'right' or value == 'up' or value == 'down':
            self.__to = value
        else:
            raise ValueError("SwitchRoom.to must be left right up down str.")

    def on_trigger(self,  entity):
        if entity == var.player:
            var.map.walk(self.to)
