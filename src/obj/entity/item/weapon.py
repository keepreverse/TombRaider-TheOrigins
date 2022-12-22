import var
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.collectible import Collectible
from src.obj.entity.item.bubble_bullet import BubbleBullet
"""
It can shoot and reload.
The update() must be called every frame.
Like the armor, it can be used to equip in the bag.
"""


class Weapon(Collectible):
    def __init__(self, name, image, damage, interval, clip, reload):
        super().__init__(name, image, True)
        self.damage = damage
        # The minimum frames between two shoots
        self.interval = interval
        # clip == -1 means it has infinite bullet for one clip. It shouldn't be set to 0
        self.clip = clip
        # The reload time, it's better to greater than interval.
        self.reload = reload
        # The counter for the shoot, counter == -1 means it's ready
        self.__counter = 0
        # The remain bullets in the clip, remain == 0 means it's reloading
        self.remain = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = int(value)

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Weapon.interval can't less than zero.")
        self.__interval = value

    @property
    def clip(self):
        return self.__clip

    @clip.setter
    def clip(self, value):
        value = int(value)
        if value == 0:
            raise ValueError("Weapon.clip can't be zero.")
        self.__clip = value

    @property
    def reload(self):
        return self.__reload

    @reload.setter
    def reload(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Weapon.reload can't less than zero.")
        self.__reload = value

    @property
    def remain(self):
        return self.__remain

    @remain.setter
    def remain(self, value):
        value = int(value)
        if value > self.clip:
            raise ValueError("Weapon.remain should be less than Weapon.clip.")
        self.__remain = value

    def update(self):
        super().update()
        # reloading
        if self.remain == 0 and self.__counter >= self.reload and var.bag.has_bullet:
            for item in var.bag.items:
                if item.name == 'Bullet':
                    self.remain = min(self.clip, item.amount)
                    item.amount -= self.remain
                    self.__counter = -1
        # cold down
        if self.remain != 0 and self.__counter >= self.interval:
            self.__counter = -1
        if self.__counter != -1:
            self.__counter += 1

    def reload_bullet(self):
        if 0 != self.remain != self.clip and self.__counter == -1 and var.bag.has_bullet:
            var.bag.add_item(Bullet(self.remain))
            self.__counter = 0
            self.remain = 0

    def shoot(self, pos, shoot_dir, shooter):
        if self.remain == 0 or self.__counter != -1:
            return None
        else:
            self.remain -= 1
            self.__counter = 0
            return BubbleBullet(pos, shoot_dir, 10, self.damage, shooter)

    def use(self):
        var.bag.remove_item(self)
        var.bag.add_item(var.bag.weapon)
        var.bag.weapon = self
