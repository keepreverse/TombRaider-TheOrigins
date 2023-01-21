from const import SCREEN_SIZE
from src.UI.interface import Interface
from src.UI.image_end import ImageEnd
from src.UI.button_menu import ButtonMenu

class END(Interface):
    def __init__(self):
        super().__init__(ImageEnd((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)),
                         ButtonMenu((SCREEN_SIZE[0]/7.2, SCREEN_SIZE[1] - 80)))