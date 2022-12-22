import const
from src.obj.obj import Obj
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
Building is an obj which wouldn't change the position.
It's collide box depend on const.TILE_SIZE.
The can_destroy attribute make no sense temporarily, it will make sense if we have a boom. 
"""


class Building(Obj):
    def __init__(self, pos, image=None, vector=(0, 0), can_access=False, can_destroy=False):
        """
        :param pos: Vector. Represent the position on the room, in Tile level not on pixel level.
        :param image: Surface
        :param vector: Vector.
        :param can_access: bool
        :param can_destroy: bool
        """
        super().__init__(Rect(0, 0, const.TILE_SIZE[0], const.TILE_SIZE[1]), image, vector)
        self.pos = pos
        self.can_access = can_access
        self.can_destroy = can_destroy

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        self.__pos = Vector.init_one_arg(value)
        self.rect.left_top = (self.__pos[0] * const.TILE_SIZE[0], self.__pos[1] * const.TILE_SIZE[1])

    @property
    def can_access(self):
        return self.__can_access

    @can_access.setter
    def can_access(self, value):
        if not isinstance(value, bool):
            raise TypeError("Building.can_access must be bool type.")
        self.__can_access = value

    @property
    def can_destroy(self):
        return self.__can_destroy

    @can_destroy.setter
    def can_destroy(self, value):
        if not isinstance(value, bool):
            raise TypeError("Building.can_destroy must be bool type.")
        self.__can_destroy = value
