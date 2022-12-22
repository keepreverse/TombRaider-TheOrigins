import random
import var
from const import IMAGE
from src.obj.building.trigger_building import TriggerBuilding
from src.tool.vector import Vector
from src.obj.entity.item.weapon7_15 import Weapon7, Weapon9, Weapon11, Weapon13, Weapon15
from src.obj.entity.item.armor5_15 import Armor7, Armor9, Armor11, Armor13, Armor15
"""
If it was collided be player, it will open and explode the Collectible instances.
"""


class Chest(TriggerBuilding):
    def __init__(self, pos, *collectibles):
        super().__init__(pos, IMAGE['chest'][0], (0, 0), False, False, IMAGE['chest'][2], (0, 0))
        self.__collectibles = [*collectibles]
        if random.randint(0, 1) == 0:
            self.__collectibles.append(Armor7())
        elif random.randint(0, 1) == 0:
            self.__collectibles.append(Armor9())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Armor11())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Armor13())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Armor15())

        if random.randint(0, 1) == 0:
            self.__collectibles.append(Weapon7())
        elif random.randint(0, 1) == 0:
            self.__collectibles.append(Weapon9())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Weapon11())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Weapon13())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Weapon15())

    @property
    def collectibles(self):
        return self.__collectibles

    def on_trigger(self, entity):
        if entity != var.player:
            return
        if self.can_trigger is True:
            self.image = self.new_image
            self.vector = self.new_vector
            for collectible in self.collectibles:
                collectible.explode(self.rect.center, Vector.random_normalized_vector())
                var.map.active_room.entities.append(collectible)
            self.can_trigger = False
