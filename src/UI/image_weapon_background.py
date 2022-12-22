from src.UI.image_background import ImageBackground


class ImageWeaponBackground(ImageBackground):
    def __init__(self, center):
        super().__init__(center, (70, 70), (100, 100, 100, 200), True)
