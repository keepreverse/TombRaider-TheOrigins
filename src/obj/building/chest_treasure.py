import random
import var
from const import IMAGE
from src.obj.building.trigger_building import TriggerBuilding
from src.obj.entity.item.treasure import Treasure
from src.tool.vector import Vector
"""
If it was collided be player, it will open and explode the Collectible instances.
"""


class ChestTreasure(TriggerBuilding):
    def __init__(self, pos, *collectibles):
        super().__init__(pos, IMAGE['chest'][0], (0, 0), False, False, IMAGE['chest'][1], (0, 0))
        self.__collectibles = [*collectibles, Treasure()]

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
