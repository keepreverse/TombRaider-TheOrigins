import var
from src.UI.label import Label


class LabelWeaponName(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Name: ' + var.bag.weapon.name


class LabelWeaponDamage(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Damage: ' + str(var.bag.weapon.damage)


class LabelWeaponInterval(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Interval: ' + str(var.bag.weapon.interval) + ' ticks'


class LabelWeaponClip(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Clip: ' + str(var.bag.weapon.clip)


class LabelWeaponReload(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=25, is_left_center=True)

    def update(self):
        self.text = 'Reload: ' + str(var.bag.weapon.reload) + ' ticks'
