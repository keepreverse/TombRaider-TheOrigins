import var
import const
from src.UI.button import Button
from src.UI.interface_loading import LOADING


class ButtonPlay(Button):
    def __init__(self, center):
        super().__init__(center, None, const.IMAGE['start'][0], const.IMAGE['start'][4])

    def on_available(self):
        self.image = self.images[1]

    def on_hover(self):
        self.image = self.images[0]

    def on_click(self):
        self.image = self.images[1]
        var.interface = var.loading = LOADING()
