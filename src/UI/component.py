from src.tool.rect import Rect
from pygame import Surface
"""
The base class for button image label...
"""


class Component:
    def __init__(self, center, *images):
        self.images = images
        self.rect = Rect()
        if len(self.images) == 0:
            self.image = None
        else:
            self.image = self.images[0]
            self.rect.size = self.image.get_size()
        self.rect.center = center

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if value is not None and not isinstance(value, Surface):
            raise TypeError("Component.image must be Surface type.")
        center = self.rect.center
        if value is None:
            self.__image = None
            self.rect.size = (0, 0)
        else:
            self.__image = value.copy()
            self.rect.size = self.__image.get_size()
        self.rect.center = center

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = [_ for _ in value if isinstance(_, Surface)]

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = Rect.init_one_arg(value)

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, (int(self.rect.left), int(self.rect.top)))

    def update(self):
        pass
