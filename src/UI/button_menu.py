import var
import const
from const import Init, SOUND
from src.UI.button import Button

class ButtonMenu(Button):
    def __init__(self, center):
        super().__init__(center, None, const.IMAGE['start'][8], const.IMAGE['start'][9])

    def on_available(self):
        self.image = self.images[1]

    def on_hover(self):
        self.image = self.images[0]

    def on_click(self):
        self.image = self.images[1]
        var.interface = var.start
        Init.init_music(SOUND, "menu", 0.2)