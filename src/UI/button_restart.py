import var
from const import Init, SOUND
from src.UI.button import CustomButton


class ButtonRestart(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (150, 150, 150), (120, 40), "Restart", 25, smooth=True)

    def on_click(self):
        var.interface = var.loading
        Init.init_music(SOUND, "game", 0.12)
        
    def on_hover(self):
        self.image = self.images[1]

    def on_available(self):
        self.image = self.images[0]