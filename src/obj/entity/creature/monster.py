import random
import var
from src.obj.entity.creature.creature import Creature
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.collectible import Collectible
from src.obj.entity.item.potion import Potion
from src.obj.entity.item.shooting_bullet import ShootingBullet
from src.tool.vector import Vector
from src.obj.entity.item.weapon7_15 import Weapon7, Weapon9, Weapon11, Weapon13
from src.obj.entity.item.armor5_15 import Armor7, Armor9, Armor11, Armor13
"""
It will attack the player.
It will drop the Collectible instances when they are killed.
"""


class Monster(Creature):
    def __init__(self, rect, animation_system, speed_mag, max_health, defense, damage, *collectibles):
        super().__init__(rect, animation_system, speed_mag, max_health, defense, damage)
        self.collectibles = [*collectibles]
        # Add the drop bullet and potion
        if random.randint(0, 0) == 0:
            self.collectibles.append(Bullet(random.randint(1, 3) * 10))
        if random.randint(0, 1) == 0:
            self.collectibles.append(Potion())
        # Add the drop weapon
        if random.randint(0, 1) == 0:
            self.collectibles.append(Weapon7())
        elif random.randint(0, 2) == 0:
            self.collectibles.append(Weapon9())
        elif random.randint(0, 4) == 0:
            self.collectibles.append(Weapon11())
        elif random.randint(0, 8) == 0:
            self.collectibles.append(Weapon13())
        # Add the drop armor
        if random.randint(0, 1) == 0:
            self.__collectibles.append(Armor7())
        elif random.randint(0, 2) == 0:
            self.__collectibles.append(Armor9())
        elif random.randint(0, 4) == 0:
            self.__collectibles.append(Armor11())
        elif random.randint(0, 8) == 0:
            self.__collectibles.append(Armor13())

    @property
    def collectibles(self):
        return self.__collectibles

    @collectibles.setter
    def collectibles(self, value):
        for collectible in value:
            if not isinstance(collectible, Collectible):
                raise TypeError("Monster.collectibles must be a list of Collectible type instance.")
        self.__collectibles = value

    def update(self):
        super().update()
        # If it is killed, the Collectible instances drop
        if self.is_dead:
            for collectible in self.collectibles:
                collectible.explode(self.rect.center, Vector.random_normalized_vector())
                var.map.active_room.entities.append(collectible)

    @property
    def can_see_player(self):
        return True

    def collide_entity(self, *entities):
        for entity in entities:
            if isinstance(entity, ShootingBullet) and entity.owner == var.player:
                self.take_bullet_damage(entity)
            elif entity == var.player:
                var.player.collide_entity(self)
