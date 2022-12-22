import var
from src.UI.image import Image


class ImageArmor(Image):
    def __init__(self, center):
        super().__init__(center, None)
        center = self.rect.center
        self.rect.size = self.image.get_size()
        self.rect.center = center

    @property
    def image(self):
        if var.bag.armor is not None:
            return var.bag.armor.image
        else:
            return None

    @image.setter
    def image(self, value):
        pass
