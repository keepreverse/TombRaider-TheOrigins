import pygame
from pygame.surface import Surface
from src.UI.image import Image


class ImageBackground(Image):
    def __init__(self, center, size, color=(0, 0, 0), smooth=False):
        super().__init__(center, Surface(size))
        if len(color) == 4 or smooth:
            self.image = self.image.convert_alpha()
        if not smooth:
            self.image.fill(color)
        else:
            self.image.fill((0, 0, 0, 0))
            r = min(int(1 / 10 * size[0]), int(1 / 10 * size[1]))
            w = int(size[0])
            h = int(size[1])
            pygame.draw.circle(self.image, color, (r, r), r)
            pygame.draw.circle(self.image, color, (r, h - r), r)
            pygame.draw.circle(self.image, color, (w - r, r), r)
            pygame.draw.circle(self.image, color, (w - r, h - r), r)
            pygame.draw.rect(self.image, color, (0, r, w, h - 2 * r))
            pygame.draw.rect(self.image, color, (r, 0, w - 2 * r, h))
