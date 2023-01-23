from src.UI.image_background import ImageBackground


class ImagePlayerBackground(ImageBackground):
    def __init__(self):
        super().__init__((160, 130), (120, 120), (60, 60, 60))