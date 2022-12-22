from const import TILE_SIZE
from src.obj.obj import Obj
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
The entity which can move, collide with building.
update() should be called every frame.
"""


class Entity(Obj):
    def __init__(self, rect, image, vector, speed_dir, speed_mag):
        """
        :param rect: Rect.
        :param image: Image.
        :param vector: Vector.
        :param speed_dir: Vector. The direction the entity will move to.
        :param speed_mag: Float. The speed magnitude of the entity.
        """
        super().__init__(rect, image, vector)
        self.speed_dir = speed_dir
        self.speed_mag = speed_mag
        # This frame the position change of the entity.
        # It can only be changed by calling move().
        self.__delta_pos = Vector(0, 0)
        # Next frame the entity will move.
        self.__next_move = None

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        value = Rect.init_one_arg(value)
        if value.width > TILE_SIZE[0] or value.height > TILE_SIZE[1]:
            raise ValueError("Creature.rect shouldn't greater than const.TILE_SIZE.")
        self.__rect = value

    @property
    def speed_dir(self):
        return self.__speed_dir

    @speed_dir.setter
    def speed_dir(self, value):
        self.__speed_dir = Vector.init_one_arg(value).normalize()

    @property
    def speed_mag(self):
        return self.__speed_mag

    @speed_mag.setter
    def speed_mag(self, value):
        if value < 0:
            raise ValueError("speed_mag can't less than zero.")
        self.__speed_mag = float(value)

    @property
    def delta_pos(self):
        return self.__delta_pos

    @property
    def next_move(self):
        return self.__next_move

    @next_move.setter
    def next_move(self, value):
        if value is None:
            self.__next_move = None
        else:
            self.__next_move = Vector.init_one_arg(value)

    def move(self, delta_pos=None):
        """
        If delta_pos is not None, it will move by the delta_pos.
        Else if the next_move is not None, it will move by the next_move.
        Else move according to the speed_dir and speed_mag.
        :param delta_pos: Vector. The specified delta_pos
        :return:
        """
        if delta_pos is not None:
            self.__delta_pos = Vector.init_one_arg(delta_pos)
        elif self.next_move is not None:
            self.__delta_pos = self.next_move
            self.next_move = None
        else:
            self.__delta_pos = self.speed_dir * self.speed_mag
        self.rect.center += self.__delta_pos

    def collide_building(self, *buildings):
        """
        Process the collide with the buildings.
        :param buildings: [Building]
        :return:
        """
        pass

    def collide_entity(self, *entities):
        """
        Process the collide with the entities.
        :param entities: [Entity]
        :return:
        """
        pass

    def update(self):
        """
        Each frame the entity do.
        :return:
        """
        self.move()
