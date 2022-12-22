import var
from src.UI.progress_bar import ProgressBar


class ProgressBarHP(ProgressBar):
    def __init__(self, center):
        super().__init__(center, (100, 20), 100, active_color=(255, 0, 0))

    def update(self):
        if var.player is not None:
            self.progress = round(var.player.health / var.player.max_health * self.length)
