import random
import var
from const import IMAGE
from src.obj.building.trigger_building import TriggerBuilding
from src.tool.vector import Vector
from src.obj.entity.item.weapons import SawedOff, AK47, AWP
from src.obj.entity.item.armor5_15 import Armor11, Armor13, Armor15
from src.obj.entity.item.bullet import Bullet
"""
Chest with the best armor/weapon
"""


class ChestMaze(TriggerBuilding):
    def __init__(self, pos, *collectibles):
        super().__init__(pos, IMAGE['chest'][2], (0, 0), False, False, IMAGE['chest'][3], (0, 0))
        self.__collectibles = [*collectibles]
        if random.randint(0, 2) == 0:
            if random.randint(0, 3) == 0:
                self.__collectibles.append(Armor11())
            elif random.randint(0, 2) == 0:
                self.__collectibles.append(Armor13())
            else:
                self.__collectibles.append(Armor15())
        else:
            if random.randint(0, 3) == 0:
                self.__collectibles.append(AK47())
            elif random.randint(0, 2) == 0:
                self.__collectibles.append(SawedOff())
            else:
                self.__collectibles.append(AWP())
            self.__collectibles.append(Bullet(random.randint(1, 2) * 10))
                

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
