import const
import var
from src.UI.button import CustomButton
"""
Adjust the number of the enemies.
"""


class ButtonEnemiesIncrease(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (122, 122, 122), (40, 40), '+', 40, smooth=True)

    def on_available(self):
        self.image = self.images[0]

    def on_hover(self):
        if var.enemies_number == const.MAX_ENEMY:
            self.image = self.images[0]
            return
        self.image = self.images[1]

    def on_click(self):
        if var.enemies_number == const.MAX_ENEMY:
            return
        var.enemies_number += 1


class ButtonEnemiesDecrease(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (122, 122, 122), (40, 40), '-', 40, smooth=True)

    def on_available(self):
        self.image = self.images[0]

    def on_hover(self):
        if var.enemies_number == const.MIN_ENEMY:
            self.image = self.images[0]
            return
        self.image = self.images[1]

    def on_click(self):
        if var.enemies_number == const.MIN_ENEMY:
            return
        var.enemies_number -= 1
