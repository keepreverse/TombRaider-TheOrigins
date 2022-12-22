import var
from src.obj.entity.item.item import Item
from src.tool.vector import Vector
from src.tool.rect import Rect
from src.obj.building.wall import Wall
"""
When player collide with it and press space key, it will be picked up into the bag unless the bag is full.
"""


class Collectible(Item):
    def __init__(self, name, image, can_use=False, amount=1):
        super().__init__(Rect(0, 0, 30, 30), image, Vector(-6, -6), Vector(0, 0), 8, Vector(0, 0), 0)
        self.__name = name
        self.amount = amount
        # When the Collectible is explode in the Room, it will slide on the ground and finally stop.
        # The greater friction is, the faster it will stop.
        self.friction_mag = 0.5
        self.can_use = can_use

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Consumable.amount can't less than zero.")
        self.__amount = int(value)
        if self.__amount == 0:
            var.bag.remove_item(self)

    @property
    def friction_mag(self):
        return self.__friction_mag

    @friction_mag.setter
    def friction_mag(self, value):
        if value < 0:
            raise ValueError("friction_mag can't less than zero")
        self.__friction_mag = float(value)

    @property
    def information(self):
        """
        :return: str. This information will show on the bag when player select it.
        """
        return ""

    def move(self, delta_pos=None):
        if self.speed_mag == 0:
            return
        self.speed_mag = max(self.speed_mag - self.friction_mag, 0)
        super().move()

    def explode(self, pos, speed_dir):
        """
        Show on the room so player can see it and pick it up.
        :param pos: Vector. The position it will appear, in pixel level.
        :param speed_dir: Vector. The direction it will move to.
        :return:
        """
        self.rect.center = pos
        self.speed_dir = speed_dir

    def collide_building(self, *buildings):
        if self.speed_dir.length == 0 or self.speed_mag == 0:
            return
        # Sometimes it will collide with the wall, it should reflect in somehow.
        reflect_x, reflect_y = False, False
        for building in buildings:
            # It only collide with the wall.
            if not isinstance(building, Wall):
                continue
            # Decide whether reflect the x speed direction.
            if (self.speed_dir.x > 0 and self.rect.right >= building.rect.left) or \
                    (self.speed_dir.x < 0 and self.rect.left <= building.rect.right):
                reflect_x = True
            # Decide whether reflect the y speed direction.
            if (self.speed_dir.y > 0 and self.rect.bottom >= building.rect.top) or \
                    (self.speed_dir.y < 0 and self.rect.top <= building.rect.bottom):
                reflect_y = True
        # Reflect
        if reflect_x:
            self.speed_dir.x *= -1
        if reflect_y:
            self.speed_dir.y *= -1

    def use(self):
        self.amount -= 1
