import var
from src.UI.button import CustomButton


class ButtonContinue(CustomButton):
    def __init__(self, center):
        super().__init__(center, (255, 255, 255), (150, 150, 150), (120, 40), "Continue", 25, smooth=True)

    def on_click(self):
        var.interface = var.play

    def on_hover(self):
        self.image = self.images[1]

    def on_available(self):
        self.image = self.images[0]