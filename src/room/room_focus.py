import random
import const
from src.obj.building.chest import Chest
from src.obj.building.wall import Wall
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.key import Key
from src.obj.entity.item.potion import Potion
from src.room.room import Room


class RoomFocus(Room):
    def init_buildings(self):
        super().init_buildings()
        width = const.ROOM_SIZE[0] - 6
        height = const.ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if ((i == width * 2 // 5 or i == width * 3 // 5) and
                    (height // 5 <= j <= height * 2 // 5 or height * 3 // 5 <= j <=height * 4 // 5)) or \
                        ((j == height * 2 // 5 or j == height * 3 // 5) and
                         (width // 5 <= i <= width * 2 // 5 or width * 3 // 5 <= i <= width * 4 // 5)):
                    self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
        self.buildings[const.ROOM_SIZE[0] // 2][const.ROOM_SIZE[1] // 2] = \
            Chest((const.ROOM_SIZE[0] // 2, const.ROOM_SIZE[1] // 2),
                  Bullet(random.randint(1, 4) * 10), Potion(random.randint(1, 3)), Key(random.randint(1, 2)))
