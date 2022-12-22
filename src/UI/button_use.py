import var
from src.UI.button import CustomButton
"""
Use the Collectible item if they can be use.
"""


class ButtonUse(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (150, 150, 150), (120, 40), "Use", 25, smooth=True)

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.on_available()
        else:
            if var.bag.items[var.bag.active_item_id].can_use:
                self.on_hover()
            else:
                self.on_available()
            if len(var.mouse_down) > 0 and self.rect.contain(var.mouse):
                self.on_click()

    def on_click(self):
        var.bag.items[var.bag.active_item_id].use()
        self.image = self.images[1]

    def on_available(self):
        self.image = self.images[0]

    def on_hover(self):
        self.image = self.images[1]
