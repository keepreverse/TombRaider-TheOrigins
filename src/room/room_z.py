import const
from const import ROOM_SIZE
from src.obj.building.wall import Wall
from src.room.room import Room


class RoomZ(Room):
    def init_buildings(self):
        super().init_buildings()
        width = ROOM_SIZE[0] - 6
        height = ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if ((j == height // 5 or j == height * 4 // 5) and width // 5 <= i <= width * 4 // 5) or \
                        ((width // 5 <= i <= width * 4 // 5) and round(j + (height / width) * i) == height - 1):
                    self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
