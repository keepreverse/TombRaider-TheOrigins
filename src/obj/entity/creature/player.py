import var
import pygame
import const
from const import TILE_SIZE
from src.animation.animation_system import AnimationSystem
from src.obj.entity.creature.creature import Creature
from src.obj.entity.creature.monster import Monster
from src.obj.entity.item.collectible import Collectible
from src.obj.entity.item.shooting_bullet import ShootingBullet
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
The player, use keyboard and mouse to control.
"""


class Player(Creature):
    def __init__(self, pos):
        super().__init__(Rect(pos[0] * TILE_SIZE[0], pos[1] * TILE_SIZE[1], 24, 10),
                         AnimationSystem(**const.ANIMATION_REPOSITORY.animations['player']), 5, 10, 0, 0)
        self.rect.center = self.rect.left_top + Vector(TILE_SIZE[0] / 2, TILE_SIZE[1] / 2)
        # The corresponding key is pressing
        self.__w, self.__s, self.__a, self.__d,  self.__r, self.__space = False, False, False, False, False, False
        # Mouse left key.
        self.__b1 = False
        self.shoot_sound = pygame.mixer.Sound('data/music/shoot.wav')

    @property
    def defense(self):
        return var.bag.armor.defense

    @defense.setter
    def defense(self, value):
        pass

    @property
    def damage(self):
        return var.bag.weapon.damage

    @damage.setter
    def damage(self, value):
        pass

    @property
    def shoot_dir(self):
        return (var.mouse - Vector.init_one_arg(var.map.active_room.blit_point) - self.rect.center).normalize()

    @shoot_dir.setter
    def shoot_dir(self, value):
        pass

    def update(self):
        # Update the key.
        for event in var.key_down:
            if event.key == pygame.K_w:
                self.__w = True
            elif event.key == pygame.K_s:
                self.__s = True
            elif event.key == pygame.K_a:
                self.__a = True
            elif event.key == pygame.K_d:
                self.__d = True
            elif event.key == pygame.K_r:
                self.__r = True
            elif event.key == pygame.K_SPACE:
                self.__space = True
        for event in var.key_up:
            if event.key == pygame.K_w:
                self.__w = False
            elif event.key == pygame.K_s:
                self.__s = False
            elif event.key == pygame.K_a:
                self.__a = False
            elif event.key == pygame.K_d:
                self.__d = False
            elif event.key == pygame.K_SPACE:
                self.__space = False
        for event in var.mouse_down:
            if event.button == 1:
                self.__b1 = True
        for event in var.mouse_up:
            if event.button == 1:
                self.__b1 = False
        # Update the Creature part
        super().update()
        # Reload
        if self.__r:
            var.bag.weapon.reload_bullet()
            self.__r = False
        # Update weapon
        var.bag.weapon.update()

    @property
    def speed_dir(self):
        vector = Vector(0, 0)
        if self.__w:
            vector.y -= 1
        if self.__s:
            vector.y += 1
        if self.__a:
            vector.x -= 1
        if self.__d:
            vector.x += 1
        return vector.normalize()

    @speed_dir.setter
    def speed_dir(self, value):
        value = Vector.init_one_arg(value)
        if value.length != 0:
            raise AttributeError("Player.speed_dir can't be set.")

    def attack(self):
        if self.__b1:
            shooting_bullet = var.bag.weapon.shoot(self.rect.center, self.shoot_dir, self)
            if shooting_bullet is not None:
                self.shoot_sound.play()
                var.map.active_room.entities.append(shooting_bullet)

    def collide_entity(self, *entities):
        for entity in entities:
            # Pick up the Collectible
            if isinstance(entity, Collectible) and self.__space and var.bag.add_item(entity):
                var.map.active_room.entities.remove(entity)
            # Take bullet damage
            elif isinstance(entity, ShootingBullet) and entity.owner != self:
                self.take_bullet_damage(entity)
            # Take Monster damage
            elif isinstance(entity, Monster):
                self.take_creature_damage(entity)

    def refresh(self):
        # Refresh the key press, some times press key in PLAY but release in other interfaces.
        self.__w, self.__s, self.__a, self.__d,  self.__space, self.__b1 = (False for _ in range(6))

    def take_creature_damage(self, creature):
        if not self.can_take_damage:
            return
        damage = creature.damage
        if damage > 0:
            damage = max(damage - self.defense, 1)
        self.health -= damage
        self.reset_take_damage()
