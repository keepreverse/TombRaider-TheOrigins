import var
from src.tool.vector import Vector
from src.obj.entity.item.item import Item
from src.obj.entity.creature.creature import Creature
"""
It can hurt player or Monster.
It will disappear will collide with the wall.
"""


class ShootingBullet(Item):
    def __init__(self, rect, image, vector, speed_dir, speed_mag,
                 damage, owner, accelerate_dir=Vector(1, 0), accelerate_mag=0):
        super().__init__(rect, image, vector, speed_dir, speed_mag, accelerate_dir, accelerate_mag)
        self.damage = damage
        self.owner = owner
        self.__is_dead = False

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = int(value)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Creature):
            raise TypeError("ShootingBullet.owner must be Creature or None type.")
        self.__owner = value

    def update(self):
        if self.__is_dead:
            try:
                var.map.active_room.entities.remove(self)
            except:
                pass
        super().update()

    def collide_building(self, *buildings):
        for building in buildings:
            if not building.can_access:
                self.__is_dead = True
                break

