import var
from const import SCREEN_SIZE
from src.UI.image import Image


class ImageItem(Image):
    def __init__(self, item_id):
        super().__init__((0, 0), None)
        self.item_id = item_id
        self.rect.center = (130 + self.item_id * 110, SCREEN_SIZE[1]/3.3 + SCREEN_SIZE[1]/14.25)

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
