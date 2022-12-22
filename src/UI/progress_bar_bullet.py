import var
from src.UI.progress_bar import ProgressBar


class ProgressBarBullet(ProgressBar):
    def __init__(self, center):
        super().__init__(center, (100, 20), 100, active_color=(150, 150, 150))

    def update(self):
        if var.player is not None:
            self.progress = round(var.bag.weapon.remain / var.bag.weapon.clip * self.length)
