from src.tool.rect import Rect
from src.tool.vector import Vector
from pygame import Surface
"""
An obj can be display on the screen.
"""


class Obj:
    def __init__(self, rect, image, vector):
        """
        :param rect: Rect. Represent the position and the collide box for the obj.
        :param image: Image. The image the obj will display.
        :param vector: Vector. The relative position for the rect to draw the image.
        """
        self.rect = rect
        self.image = image
        # rect.top_left + delta_pos = image.top_left
        self.vector = vector

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = Rect.init_one_arg(value)

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if value is not None and not isinstance(value, Surface):
            raise TypeError("Obj.image must be Surface or None type.")
        self.__image = value

    @property
    def vector(self):
        return self.__vector

    @vector.setter
    def vector(self, value):
        self.__vector = Vector(value[0], value[1])

    def draw(self, surface):
        if self.image is not None:
            surface.blit(self.image, (int(self.rect.left + self.vector[0]), int(self.rect.top + self.vector[1])))
