import var
from src.UI.label import Label


class LabelItem(Label):
    def __init__(self, item_id):
        super().__init__((0, 0), '', 20)
        self.item_id = item_id
        self.rect.center = (80 + self.item_id * 90, 280) if item_id <= 3 else (80 + (self.item_id - 4) * 90, 370)

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
            self.text = str(var.bag.items[self.item_id].amount)
        else:
            self.text = ''
