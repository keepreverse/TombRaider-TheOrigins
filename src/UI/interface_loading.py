import var
from const import ROOM_SIZE
from src.UI.interface_pause import PAUSE
from src.UI.progress_bar import ProgressBar
from src.UI.interface import Interface
from src.UI.label import Label
from src.bag import Bag
from src.map import Map
from src.obj.entity.creature.player import Player


class LOADING(Interface):
    def __init__(self):
        super().__init__(Label((480, 540), ''), ProgressBar((480, 600), (400, 20), 4))
        self.__cnt = 0

    def update(self):
        if self.__cnt == 0:
            self.components[0].text = "Creating the player."
        elif self.__cnt == 1:
            self.components[0].text = "Creating the player backpack."
            var.player = Player((ROOM_SIZE[0] // 2, 3))
        elif self.__cnt == 2:
            self.components[0].text = "Creating the maze."
            var.bag = Bag()
        elif self.__cnt == 3:
            self.components[0].text = "Put the player into the maze."
            var.map = Map()
        elif self.__cnt == 4:
            self.components[0].text = "Done."
            var.map.active_room.entities.append(var.player)
        elif self.__cnt == 5:
            var.interface = var.play
            var.pause = PAUSE()
        if self.__cnt == 5:
            self.__cnt = -1
        else:
            self.components[1].progress = self.__cnt
        self.__cnt += 1
