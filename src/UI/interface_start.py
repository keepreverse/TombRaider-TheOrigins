from const import SCREEN_SIZE
from src.UI.interface import Interface
from src.UI.image_start import ImageStart
from src.UI.button_play import ButtonPlay
from src.UI.button_option import ButtonOption
from src.UI.button_quit import ButtonQuit

class START(Interface):
    def __init__(self):
        super().__init__(ImageStart((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)),
                         ButtonPlay((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 - 30)),
                         ButtonOption((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 60)),
                         ButtonQuit((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 150)))
