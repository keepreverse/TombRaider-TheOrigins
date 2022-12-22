import const
from src.UI.image import Image
from src.animation.animation_system import AnimationSystem


class ImagePlayer(Image):
    def __init__(self, center):
        self.__animation_system = AnimationSystem(**const.ANIMATION_REPOSITORY.animations['player'])
        self.__animation_system.play('stand_right')
        super().__init__(center, None)
        self.rect.size = self.image.get_size()
        self.rect.center = center

    @property
    def image(self):
        return self.__animation_system.image

    @image.setter
    def image(self, value):
        pass

    def update(self):
        self.__animation_system.update()
