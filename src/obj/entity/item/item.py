from src.obj.entity.entity import Entity
from src.tool.vector import Vector
"""
This entity can't be control by player or AI.
It move automatically.
It has acceleration.
"""


class Item(Entity):
    def __init__(self, rect, image, vector, speed_dir, speed_mag, accelerate_dir, accelerate_mag):
        super().__init__(rect, image, vector, speed_dir, speed_mag)
        self.accelerate_dir = accelerate_dir
        self.accelerate_mag = accelerate_mag

    @property
    def accelerate_dir(self):
        return self.__accelerate_dir

    @accelerate_dir.setter
    def accelerate_dir(self, value):
        self.__accelerate_dir = Vector.init_one_arg(value).normalize()

    @property
    def accelerate_mag(self):
        return self.__accelerate_mag

    @accelerate_mag.setter
    def accelerate_mag(self, value):
        if value < 0:
            raise ValueError("accelerate_mag can't less than zero.")
        self.__accelerate_mag = float(value)

    def move(self, delta_pos=None):
        speed_vector = self.speed_dir * self.speed_mag
        accelerate_vector = self.accelerate_dir * self.accelerate_mag
        speed_vector = speed_vector + accelerate_vector
        self.speed_dir = speed_vector.normalize()
        self.speed_mag = speed_vector.length
        super().move(delta_pos)
