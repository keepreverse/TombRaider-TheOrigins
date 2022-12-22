import const
from src.UI.image import Image
from pygame.surface import Surface

class ImageStart(Image):
    def __init__(self, center):
        super().__init__(center, const.IMAGE['start'][3])