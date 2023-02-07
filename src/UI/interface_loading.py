import var
from const import ROOM_SIZE, SCREEN_SIZE
from src.UI.progress_bar import ProgressBar
from src.UI.interface import Interface
from src.UI.label import Label
from src.bag import Bag
from src.map import Map
from src.obj.entity.creature.player import Player


class LOADING(Interface):
    def __init__(self):
        super().__init__(Label((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), ''), ProgressBar((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/1.8), ((SCREEN_SIZE[0]/2.2, SCREEN_SIZE[1]/54)), 5))
        self.__cnt = 0

    def update(self):
        if self.__cnt == 0:
            self.components[0].text = "Creating the player."
        elif self.__cnt == 1:
            self.components[0].text = "Creating the player backpack."
            var.player = Player((ROOM_SIZE[0] // 2, 3))
        elif self.__cnt == 2:
            self.components[0].text = "Loading the map."
            var.bag = Bag()
        elif self.__cnt == 3:
            self.components[0].text = "Put the player into the location."
            var.map = Map()
        elif self.__cnt == 4:
            self.components[0].text = "Done."
            var.map.active_room.entities.append(var.player)
        elif self.__cnt == 5:
            var.interface = var.play
        if self.__cnt == 5:
            self.__cnt = -1
        else:
            self.components[1].progress = self.__cnt
        self.__cnt += 1
