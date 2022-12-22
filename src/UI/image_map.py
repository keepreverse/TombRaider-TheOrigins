from pygame.surface import Surface

import var
from src.UI.image import Image


class ImageMap(Image):
    def __init__(self, center):
        super().__init__(center, Surface((200, 200)))

    def update(self):
        self.image = var.map.to_surface()
