import var
from src.UI.button import CustomButton
"""
A item in the bag.
"""


class ButtonItem(CustomButton):
    def __init__(self, item_id):
        super().__init__((0, 0), (100, 200, 100), (200, 100, 200), (70, 70), '', 0, smooth=True)
        self.item_id = item_id
        self.rect.center = (55 + self.item_id * 90, 255) if item_id <= 3 else (55 + (self.item_id - 4) * 90, 345)

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        if not 0 <= value <= 7:
            raise ValueError("ButtonItem.item_id must from 0 to 7 inclusive.")
        self.__item_id = value

    def update(self):
        if len(var.mouse_down) > 0:
            if self.rect.contain(var.mouse):
                self.on_click()
        if var.bag.active_item_id != self.item_id:
            self.on_available()
        else:
            self.on_hover()

    def on_hover(self):
        self.image = self.images[1]

    def on_click(self):
        self.image = self.images[1]
        var.bag.active_item_id = self.item_id

    def on_available(self):
        self.image = self.images[0]
