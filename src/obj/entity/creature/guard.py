import const
import var
from const import TILE_SIZE
from src.animation.animation_system import AnimationSystem
from src.obj.entity.creature.monster import Monster
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
It will dash to the player but not change it's direction until the dash is ended.
"""


class Guard(Monster):
    def __init__(self, pos, *collectibles):
        super().__init__(Rect(pos[0] * TILE_SIZE[0], pos[1] * TILE_SIZE[1], 28, 18),
                         AnimationSystem(**const.ANIMATION_REPOSITORY.animations['guard']), 5, 10, 5, 1, *collectibles)
        self.rect.center = self.rect.left_top + Vector(TILE_SIZE[0] / 2, TILE_SIZE[1] / 2)
        self.move_interval = 250
        self.move_time = 0
        self.Vector = Vector(0, 0)

    @property
    def speed_dir(self):
        vector = (var.player.rect.center - self.rect.center).normalize()
        if self.move_time == self.move_interval:
            self.move_time = 0
            self.Vector = vector
        else:
            self.move_time += 1
            vector = self.Vector

        return vector.normalize()

    @speed_dir.setter
    def speed_dir(self, value):
        value = Vector.init_one_arg(value)
        if value.length != 0:
            raise AttributeError("Pharaoh.speed_dir can't be set.")
