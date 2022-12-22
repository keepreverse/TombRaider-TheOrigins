import var
from src.UI.button import CustomButton
"""
Drop the Collectible.
"""


class ButtonDrop(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (150, 150, 150), (120, 40), "Drop", 25, smooth=True)

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.on_available()
        else:
            self.on_hover()
            if len(var.mouse_down) > 0 and self.rect.contain(var.mouse):
                self.on_click()

    def on_click(self):
        item = var.bag.items[var.bag.active_item_id]
        var.bag.remove_item(item)
        item.rect.center = var.player.rect.center
        var.map.active_room.entities.append(item)
        self.image = self.images[1]

    def on_available(self):
        self.image = self.images[0]

    def on_hover(self):
        self.image = self.images[1]
