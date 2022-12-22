import var
from src.UI.image import Image


class ImageActiveItem(Image):
    def __init__(self, center):
        super().__init__(center, None)

    def update(self):
        if var.bag.active_item_id >= len(var.bag.items):
            self.image = None
        else:
            self.image = var.bag.items[var.bag.active_item_id].image
