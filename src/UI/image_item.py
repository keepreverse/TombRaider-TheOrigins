import var
from src.UI.image import Image


class ImageItem(Image):
    def __init__(self, item_id):
        super().__init__((0, 0), None)
        self.item_id = item_id
        self.rect.center = (55 + self.item_id * 90, 255) if item_id <= 3 else (55 + (self.item_id - 4) * 90, 345)

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        if not 0 <= value <= 7:
            raise ValueError("ImageItem.item_id must from 0 to 7.")
        self.__item_id = value

    def update(self):
        if self.item_id < len(var.bag.items):
            self.image = var.bag.items[self.item_id].image
        else:
            self.image = None
