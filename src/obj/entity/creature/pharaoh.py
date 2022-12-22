import const
import random
import var
from const import TILE_SIZE
from src.animation.animation_system import AnimationSystem
from src.obj.entity.creature.monster import Monster
from src.tool.rect import Rect
from src.tool.vector import Vector
from src.obj.entity.item.bubble_bullet import BubbleBullet
"""
It will shoot to the player while walk randomly.
"""


class Pharaoh(Monster):
    def __init__(self, pos, *collectibles):
        super().__init__(Rect(pos[0] * TILE_SIZE[0], pos[1] * TILE_SIZE[1], 28, 18),
                         AnimationSystem(**const.ANIMATION_REPOSITORY.animations['pharaoh']), 3, 10, 5, 1, *collectibles)
        self.rect.center = self.rect.left_top + Vector(TILE_SIZE[0] / 2, TILE_SIZE[1] / 2)
        self.move_interval = 50
        self.move_time = 0
        self.Vector = Vector(0, 0)
        self.shoot_interval = 60
        self.shoot_time = 0
        self.shoot_damage = 2

    @property
    def shoot_dir(self):
        return (var.player.rect.center - self.rect.center).normalize()

    @shoot_dir.setter
    def shoot_dir(self, value):
        pass

    @property
    def speed_dir(self):
        if self.move_time == self.move_interval:
            vector = Vector(0, 0)
            vector.x += random.randint(-1, 1)
            vector.y += random.randint(-1, 1)
            self.move_time = 0
            self.Vector = vector.normalize()
        else:
            self.move_time += 1
        return self.Vector

    @speed_dir.setter
    def speed_dir(self, value):
        value = Vector.init_one_arg(value)
        if value.length != 0:
            raise AttributeError("Pharaoh.speed_dir can't be set.")

    def attack(self):
        if self.shoot_time > self.shoot_interval:
            shooting_bullet = BubbleBullet(self.rect.center, self.shoot_dir, 5, self.shoot_damage, self)
            self.shoot_time = 0
            var.map.active_room.entities.append(shooting_bullet)
        else:
            self.shoot_time += 1
