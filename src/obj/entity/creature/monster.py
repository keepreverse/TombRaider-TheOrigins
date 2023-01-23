import random
import var
from src.tool.vector import Vector
from src.obj.entity.creature.creature import Creature
from src.obj.entity.item.collectible import Collectible
from src.obj.entity.item.shooting_bullet import ShootingBullet
from src.obj.entity.item.weapons import Deagle, HKUMP, SawedOff, AK47
from src.obj.entity.item.armors import ArmorPolice, ArmorTiger, ArmorSapphire, ArmorSandstorm
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.potion_hp import PotionHP
from src.obj.entity.item.potion_buff import PotionBuff
from src.obj.entity.item.treasure import Treasure
"""
It will attack the player.
It will drop the Collectible instances when they are killed.
"""


class Monster(Creature):
    def __init__(self, rect, animation_system, speed_mag, max_health, defense, damage, *collectibles):
        super().__init__(rect, animation_system, speed_mag, max_health, defense, damage)
        self.__collectibles = [*collectibles]
        # Add the drop bullet and potion_hp
        self.__collectibles.append(Bullet(random.randint(2, 3) * 8))
        if random.randint(0, 1) == 0:
            self.__collectibles.append(PotionHP())
        if random.randint(0, 5) == 0:
            self.__collectibles.append(PotionBuff())
        # Add the drop weapon
        if random.randint(0, 4) == 0:
            self.__collectibles.append(Deagle())
        elif random.randint(0, 4) == 0:
            self.__collectibles.append(HKUMP())
        elif random.randint(0, 6) == 0:
            self.__collectibles.append(SawedOff())
        elif random.randint(0, 8) == 0:
            self.__collectibles.append(AK47())
        # Add the drop armor
        if random.randint(0, 4) == 0:
            self.__collectibles.append(ArmorPolice())
        elif random.randint(0, 4) == 0:
            self.__collectibles.append(ArmorTiger())
        elif random.randint(0, 6) == 0:
            self.__collectibles.append(ArmorSapphire())
        elif random.randint(0, 8) == 0:
            self.__collectibles.append(ArmorSandstorm())
        # Add the treasure
        elif random.randint(0, 50) == 0:
            self.__collectibles.append(Treasure())

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
            for collectible in self.__collectibles:
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
