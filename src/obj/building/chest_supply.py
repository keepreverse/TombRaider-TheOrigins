import random
import var
from const import IMAGE
from src.obj.building.trigger_building import TriggerBuilding
from src.tool.vector import Vector
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.potion import Potion
from src.obj.entity.item.key import Key
"""
Chest with ammo, heal and key(s)
"""


class ChestSupply(TriggerBuilding):
    def __init__(self, pos, *collectibles):
        super().__init__(pos, IMAGE['chest'][4], (0, 0), False, False, IMAGE['chest'][5], (0, 0))
        self.__collectibles = [*collectibles]
        self.__collectibles = [*collectibles]
        # Add the drop bullet and potion
        self.__collectibles.append(Bullet(random.randint(2, 3) * 10))
        self.__collectibles.append(Potion(random.randint(1, 3)))
        self.__collectibles.append(Key(random.randint(1, 2)))
    @property
    def collectibles(self):
        return self.__collectibles

    def on_trigger(self, entity):
        if entity != var.player:
            return
        if self.can_trigger is True:
            self.image = self.new_image
            self.vector = self.new_vector
            for collectible in self.__collectibles:
                collectible.explode(self.rect.center, Vector.random_normalized_vector())
                var.map.active_room.entities.append(collectible)
            self.can_trigger = False
