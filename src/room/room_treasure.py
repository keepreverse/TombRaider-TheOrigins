import random
from src.obj.building.chest_treasure import ChestTreasure
from src.room.room import Room
from const import ROOM_SIZE


class RoomTreasure(Room):
    def init_buildings(self):
        super().init_buildings()
        self.buildings[ROOM_SIZE[0] // 2][ROOM_SIZE[1] // 2 - 1] = \
            ChestTreasure((ROOM_SIZE[0] // 2, ROOM_SIZE[1] // 2 - 1))

    def init_entities(self):
        pass
