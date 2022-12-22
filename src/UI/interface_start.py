from src.UI.button_option import ButtonOption
from src.UI.interface import Interface
from src.UI.button_play import ButtonPlay
from src.UI.button_quit import ButtonQuit
from src.UI.image_start import ImageStart


class START(Interface):
    def __init__(self):
        super().__init__(ImageStart((480, 320)), ButtonPlay((480, 250)), ButtonQuit((480, 390)), ButtonOption((480, 320)))
