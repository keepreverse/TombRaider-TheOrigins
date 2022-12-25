from const import SCREEN_SIZE
from src.UI.interface import Interface
from src.UI.image_death import ImageDeath
from src.UI.button_again import ButtonTryAgain
from src.UI.button_menu import ButtonMenu

class DEATH(Interface):
    def __init__(self):
        super().__init__(ImageDeath((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)),
                         ButtonTryAgain((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 - 40)),
                         ButtonMenu((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2 + 60)))