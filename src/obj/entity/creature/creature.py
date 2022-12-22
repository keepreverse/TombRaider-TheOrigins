import var
from src.animation.animation_system import AnimationSystem
from src.buff.buff import Buff
from src.obj.building.trigger_building import TriggerBuilding
from src.obj.entity.entity import Entity
from src.tool.vector import Vector
"""
Every creature has health, buff, damage, defense and animation_system.
Every creature can do attack or take damage.
"""


class Creature(Entity):
    def __init__(self, rect, animation_system, speed_mag, max_health, defense, damage):
        """
        :param rect: Rect
        :param animation_system: AnimationSystem
        :param speed_mag: float
        :param max_health: int
        :param defense: int
        :param damage: int
        """
        super().__init__(rect, None, None, Vector(0, 0), speed_mag)
        self.max_health = max_health
        self.defense = defense
        self.damage = damage
        self.shoot_dir = Vector(1, 0)
        self.health = self.max_health
        self.animation_system = animation_system
        self.animation_system.play("stand_left")
        # The counter for taking damage.
        self.__cnt_take_damage = 0
        # The minimum frames two damage taking.
        self.__interval_take_damage = 30
        # Buff of the creature.
        self.__buff = None

    @property
    def image(self):
        return self.__animation_system.image

    @image.setter
    def image(self, value):
        pass

    @property
    def vector(self):
        return self.__animation_system.vector

    @vector.setter
    def vector(self, value):
        pass

    @property
    def animation_system(self):
        return self.__animation_system

    @animation_system.setter
    def animation_system(self, value):
        if not isinstance(value, AnimationSystem):
            raise TypeError("Creature.animation_system must be AnimationSystem type.")
        self.__animation_system = value

    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Creature.max_health can't be less than zero.")
        self.__max_health = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Creature.defense can't be less than zero.")
        self.__defense = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = int(value)

    @property
    def shoot_dir(self):
        return self.__shoot_dir

    @shoot_dir.setter
    def shoot_dir(self, value):
        self.__shoot_dir = Vector.init_one_arg(value).normalize()

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        value = int(value)
        self.__health = min(max(value, 0), self.max_health)

    @property
    def buff(self):
        return self.__buff

    @buff.setter
    def buff(self, value):
        if value is not None and not isinstance(value, Buff):
            raise TypeError("Creature.buff must be Buff or None type.")
        if value is not None and self.buff is not None:
            return
        self.__buff = value

    @property
    def is_dead(self):
        return self.health == 0

    @property
    def can_take_damage(self):
        return not self.is_dead and self.__cnt_take_damage >= self.__interval_take_damage

    def reset_take_damage(self):
        """
        It should be called in all kinds of taking damage.
        :return:
        """
        self.__cnt_take_damage = 0

    def update(self):
        # Update the buff.
        if self.buff is not None:
            self.buff.update()
            if self.buff.time == 0:
                self.buff.recover()
                self.buff = None
        # Update the counter for taking damage.
        self.__cnt_take_damage += 1
        # Move and attack
        self.move()
        self.attack()
        # Decide which animation to be played through the speed_dir and shoot_dir.
        if self.speed_dir.length == 0:
            if 0 <= self.shoot_dir.angle_to(Vector(0, 1)) < 180:
                self.__animation_system.play("stand_left")
            else:
                self.__animation_system.play("stand_right")
        elif 0 <= self.speed_dir.angle_to(Vector(0, 1)) < 180:
            self.__animation_system.play("move_left")
        else:
            self.__animation_system.play("move_right")
        # Update the animation system.
        self.__animation_system.update()
        # Is dead
        if self.is_dead:
            var.map.active_room.entities.remove(self)

    def attack(self):
        pass

    def take_bullet_damage(self, shootingbullet):
        if not self.can_take_damage:
            return
        damage = shootingbullet.damage
        if damage > 0:
            damage = max(damage - self.defense, 1)
        self.health -= damage
        # The bullet damage will cause creature move to the bullet direction.
        self.next_move = shootingbullet.speed_dir * 10
        self.reset_take_damage()
        try:
            var.map.active_room.entities.remove(shootingbullet)
        except ValueError:
            pass

    def take_creature_damage(self, creature):
        pass

    def take_damage(self, damage):
        """
        Directly take damage, usually from the trap.
        :param damage: int
        :return:
        """
        if self.can_take_damage:
            self.health -= damage
            self.reset_take_damage()

    def collide_building(self, *buildings):
        # A flag that check whether the entity can move finally like original move.
        # 标志实体最后能否像最开始那样移动
        can_access = True

        for building in buildings:
            # If the entity don't move, just skip.
            if self.delta_pos.length == 0:
                break
            # The building can't access and entity collide with it.
            if not building.can_access and self.rect.intersect(building.rect):

                # It can't move like original move.
                can_access = False

                # First cancel the move.
                delta_pos = self.delta_pos
                self.move(delta_pos * -1)

                # Try to move only in x or y direction, see if they still collide with building.
                # If it is, just set the corresponding direction move to zero.
                x, y = 1, 1
                # Try to move only in y direction.
                self.move((0, delta_pos[1]))
                if self.rect.intersect(building.rect):
                    y = 0
                self.move((0, delta_pos[1] * -1))
                # Try to move only in x direction.
                self.move((delta_pos[0], 0))
                if self.rect.intersect(building.rect):
                    x = 0
                self.move((delta_pos[0] * -1, 0))
                # Now move according to x and y.
                self.move((delta_pos[0] * x, delta_pos[1] * y))

            if isinstance(building, TriggerBuilding):
                building.on_trigger(self)
        # It process the special case for the collide.
        # Two rect has a overlapped corner.
        # In this case entity can move x or y direction without collide with the rect.
        # But if it move together, it will collide, cancel this move.
        if not can_access and self.delta_pos[0] != 0 and self.delta_pos[1] != 0:
            self.move(self.delta_pos * -1)
            self.move((0, 0))
