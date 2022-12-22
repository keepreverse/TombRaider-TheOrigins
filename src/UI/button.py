import pygame
import var
from pygame.surface import Surface
from src.UI.component import Component
from src.UI.label import Label
"""
A button.
When mouse is not on it, on_available() will be called.
When mouse click on it, on_click() will be called.
When mouse is on it, on_hover() will be called.
"""


class Button(Component):
    def __init__(self, center, label, image_inactive, image_active, mysize=None):
        self.label = label
        self.mysize = mysize
        super().__init__(center, image_inactive, image_active)

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
            self.rect.size = self.mysize
        else:
            self.__image = value.copy()
            self.rect.size = self.__image.get_size()
        self.rect.center = center
        if self.label is not None:
            self.label.draw(self.__image)

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value):
        if value is not None and not isinstance(value, Label):
            raise TypeError("Button.label must be Label type.")
        self.__label = value

    def update(self):
        if self.rect.contain(var.mouse):
            if len(var.mouse_down) > 0:
                self.on_click()
            else:
                self.on_hover()
        else:
            self.on_available()

    def on_click(self):
        pass

    def on_hover(self):
        pass

    def on_available(self):
        pass


class CustomButton(Button):
    """
    It can create a button just use color but not image.
    It's a rectangle button.
    """
    def __init__(self, center, button_active_color, button_inactive_color, button_size,
                 label_text, label_size, label_color=(0, 0, 0), label_font_type=None, smooth=False):
        image_active = pygame.Surface(button_size).convert_alpha()
        image_inactive = pygame.Surface(button_size).convert_alpha()
        image_active.fill((0, 0, 0, 0))
        image_inactive.fill((0, 0, 0, 0))
        if not smooth:
            image_active.fill(button_active_color)
            image_inactive.fill(button_inactive_color)
        else:
            r = min(int(1/10*button_size[0]), int(1/10*button_size[1]))
            w = int(button_size[0])
            h = int(button_size[1])
            pygame.draw.circle(image_active, button_active_color, (r, r), r)
            pygame.draw.circle(image_active, button_active_color, (r, h - r), r)
            pygame.draw.circle(image_active, button_active_color, (w - r, r), r)
            pygame.draw.circle(image_active, button_active_color, (w - r, h - r), r)
            pygame.draw.rect(image_active, button_active_color, (0, r, w, h - 2 * r))
            pygame.draw.rect(image_active, button_active_color, (r, 0, w - 2 * r, h))
            pygame.draw.circle(image_inactive, button_inactive_color, (r, r), r)
            pygame.draw.circle(image_inactive, button_inactive_color, (r, h - r), r)
            pygame.draw.circle(image_inactive, button_inactive_color, (w - r, r), r)
            pygame.draw.circle(image_inactive, button_inactive_color, (w - r, h - r), r)
            pygame.draw.rect(image_inactive, button_inactive_color, (0, r, w, h - 2 * r))
            pygame.draw.rect(image_inactive, button_inactive_color, (r, 0, w - 2 * r, h))
        if label_text != '':
            label = Label((button_size[0]/2, button_size[1]/2), label_text, label_size, label_color, label_font_type)
        else:
            label = None
        super().__init__(center, label, image_inactive, image_active)
