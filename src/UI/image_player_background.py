from src.UI.image_background import ImageBackground


class ImagePlayerBackground(ImageBackground):
    def __init__(self):
        super().__init__((80, 100), (120, 120), (0, 0, 0, 200))