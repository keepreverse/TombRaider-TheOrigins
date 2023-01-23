from src.UI.image_background import ImageBackground


class ImageArmorBackground(ImageBackground):
    def __init__(self, center):
        super().__init__(center, (70, 70), (60, 60, 60), True)
