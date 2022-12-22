import const
import var
from const import TILE_SIZE
from src.animation.animation_system import AnimationSystem
from src.obj.entity.creature.monster import Monster
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
It will move to player forever in a slower speed until it is dead.
"""


class Mummy(Monster):
    def __init__(self, pos, *collectibles):
        super().__init__(Rect(pos[0] * TILE_SIZE[0], pos[1] * TILE_SIZE[1], 35, 20),
                         AnimationSystem(**const.ANIMATION_REPOSITORY.animations['mummy']), 2, 10, 5, 1, *collectibles)
        self.rect.center = self.rect.left_top + Vector(TILE_SIZE[0] / 2, TILE_SIZE[1] / 2)
        self.move_interval = 80
        self.move_time = 0
        self.Vector = Vector(0, 0)

    @property
    def speed_dir(self):
        if self.move_time == self.move_interval:
            self.move_time = 0
            self.Vector = (var.player.rect.center - self.rect.center).normalize()
        else:
            self.move_time += 1
        return self.Vector

    @speed_dir.setter
    def speed_dir(self, value):
        value = Vector.init_one_arg(value)
        if value.length != 0:
            raise AttributeError("Pharaoh.speed_dir can't be set.")
