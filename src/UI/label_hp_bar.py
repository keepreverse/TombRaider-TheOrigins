import var
from src.UI.label import Label


class LabelHPBar(Label):
    def __init__(self, center):
        super().__init__(center, "", size=23)

    def update(self):
        if var.player is not None:
            self.text = str(var.player.health) + ' / ' + str(var.player.max_health)