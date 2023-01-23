import var
from src.UI.label import Label


class LabelDebuffName(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=30, is_left_center=True)

    def update(self):
        if var.player.debuff is not None:
            self.text = 'Speed:   ' + var.player.debuff.name
        else:
            self.text = 'Speed:   ' + 'Normal'


class LabelDebuffTime(Label):
    def __init__(self, left_center):
        super().__init__(left_center, '', size=30, is_left_center=True)

    def update(self):
        if var.player.debuff is not None:
            self.text = 'Time:     ' + str(('%.3f' % (var.player.debuff.time/60))) + ' secs'
        else:
            self.text = ''
