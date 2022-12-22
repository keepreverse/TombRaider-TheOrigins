import random

import const
from const import ROOM_SIZE
from src.obj.building.chest import Chest
from src.obj.building.trap import Trap
from src.obj.building.wall import Wall
from src.obj.entity.item.bullet import Bullet
from src.obj.entity.item.key import Key
from src.obj.entity.item.potion import Potion
from src.room.room import Room


class RoomMaze(Room):
    def init_buildings(self):
        super().init_buildings()
        width = ROOM_SIZE[0] - 6
        height = ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if (j == height // 7 and (width // 7 <= i <= width * 2 // 7 or width * 3 // 7 <= i <= width * 6 // 7)) or \
                        (j == height * 2 // 7 and (width * 2 // 7 <= i <= width * 3 // 7 or width * 4 // 7 <= i <= width * 5 // 7)) or \
                        (j == height * 3 // 7 and width * 5 // 7 <= i <= width) or \
                        (j == height * 4 // 7 and i <= width * 2 // 7) or \
                        (j == height * 5 // 7 and (width * 2 // 7 <= i <= width * 3 // 7 or width * 4 // 7 <= i <= width * 5 // 7)) or \
                        (j == height * 6 // 7 and (width // 7 <= i <= width * 4 // 7 or width * 5 // 7 <= i <= width * 6 // 7)) or \
                        (i == width // 7 and (height // 7 <= j <= height * 4 // 7 or height * 5 // 7 <= j <= height * 6 // 7)) or \
                        (i == width * 2 // 7 and (height * 2 // 7 <= j <= height * 3 // 7 or height * 4 // 7 <= j <= height * 5 // 7)) or \
                        (i == width * 3 // 7 and j <= height * 2 // 7) or \
                        (i == width * 4 // 7 and height * 5 // 7 <= j <= height) or \
                        (i == width * 5 // 7 and (height * 2 // 7 <= j <= height * 3 // 7 or height * 4 // 7 <= j <= height * 5 // 7)) or \
                        (i == width * 6 // 7 and (height // 7 <= j <= height * 2 // 7 or height * 3 // 6 <= j <= height * 6 // 7)):
                    self.buildings[3 + i][3 + j] = Wall((3 + i, 3 + j), const.IMAGE['wall'][5], (0, -12))
                if (j == height * 2 // 7 and width * 3 // 7 < i < width * 4 // 7) or \
                        (j == height * 5 // 7 and width * 3 // 7 < i < width * 4 // 7) or \
                        (i == width * 2 // 7 and height * 3 // 7 < j < height * 4 // 7) or \
                        (i == width * 5 // 7 and height * 3 // 7 < j < height * 4 // 7):
                    self.buildings[3 + i][3 + j] = Trap((3 + i, 3 + j))
        self.buildings[ROOM_SIZE[0] // 2][ROOM_SIZE[1] // 2] = \
            Chest((ROOM_SIZE[0] // 2, ROOM_SIZE[1] // 2),
                  Bullet(random.randint(1, 4) * 10), Potion(random.randint(1, 3)), Key(random.randint(1, 2)))
