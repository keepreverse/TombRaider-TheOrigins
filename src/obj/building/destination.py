from pygame.surface import Surface
import var
from src.obj.building.trigger_building import TriggerBuilding
from const import TILE_SIZE
"""
If the player get the treasure and collide with it, the game win.
"""


class Destination(TriggerBuilding):
    def __init__(self, pos):
        image = Surface(TILE_SIZE)
        image.fill((255, 255, 255))
        super().__init__(pos, image, (0, 0), False, False, Surface(TILE_SIZE), (0, 0))

    def on_trigger(self, entity):
        if entity == var.player and var.bag.has_treasure:
            var.interface = var.start
