import var
from src.UI.label import Label


class LabelEnemiesNumber(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', is_left_center=True)

    def update(self):
        self.text = str(var.enemies_number)
