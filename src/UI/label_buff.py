import var
from src.UI.label import Label


class LabelBuffName(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=30, is_left_center=True)

    def update(self):
        if var.player.buff is not None:
            self.text = 'Buff: ' + var.player.buff.name
        else:
            self.text = 'Buff: ' + 'None'


class LabelBuffTime(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=30, is_left_center=True)

    def update(self):
        if var.player.buff is not None:
            self.text = 'Time: ' + str(var.player.buff.time) + ' ticks'
        else:
            self.text = ''
