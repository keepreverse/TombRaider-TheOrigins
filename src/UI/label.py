from pygame.surface import Surface
from src.UI.component import Component
from pygame.font import SysFont
"""
Display a label.
"""


class Label(Component):
    def __init__(self, center, text, size=40, color=(255, 255, 255), font_type=None, background=None, is_left_center=False):
        super().__init__(center)
        self.is_left_center = is_left_center
        self.size = size
        self.color = color
        self.font_type = font_type
        self.background = background
        self.__text = ''
        self.text = text
        if self.image is not None:
            self.rect.size = self.image.get_size()
            if not self.is_left_center:
                self.rect.center = center
            else:
                self.rect.left_center = center

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise ValueError("Label.text must be str type.")
        if self.__text == value:
            return
        self.__text = value
        if value == '':
            self.image = None
            return
        self.image = SysFont(self.font_type, self.size, False).render(self.__text, True, self.color)
        if not self.is_left_center:
            center = self.rect.center
            self.rect.size = self.image.get_size()
            self.rect.center = center
        else:
            left_center = self.rect.left_center
            self.rect.size = self.image.get_size()
            self.rect.left_center = left_center

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if value is not None and not isinstance(value, Surface):
            raise TypeError("Label.image must be Surface or None type.")
        self.__image = value

    @property
    def is_left_center(self):
        return self.__is_left_center

    @is_left_center.setter
    def is_left_center(self, value):
        if not isinstance(value, bool):
            raise TypeError('Label.is_left_center must be bool type.')
        self.__is_left_center = value
