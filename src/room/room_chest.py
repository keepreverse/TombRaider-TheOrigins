import random
from src.obj.building.chest import Chest
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.key import Key
from src.obj.entity.item.potion import Potion
from src.obj.entity.item.treasure import Treasure
from src.room.room import Room
from const import ROOM_SIZE


class RoomChest(Room):
    def init_buildings(self):
        super().init_buildings()
        self.buildings[ROOM_SIZE[0] // 2][ROOM_SIZE[1] // 2] = \
            Chest((ROOM_SIZE[0] // 2, ROOM_SIZE[1] // 2),
                  Bullet(random.randint(1, 4) * 10), Potion(random.randint(1, 3)), Key(random.randint(1, 2)), Treasure())

    def init_entities(self):
        pass
