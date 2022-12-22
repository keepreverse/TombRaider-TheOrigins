import const
from src.obj.building.wall import Wall
from src.room.room import Room


class RoomH(Room):
    def init_buildings(self):
        super().init_buildings()
        width = const.ROOM_SIZE[0] - 6
        height = const.ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if ((i == width // 3 or i == width * 2 // 3) and height // 6 <= j <= height * 5 // 6) or \
                        (j == height // 2 - 1 and width // 3 <= i <= width * 2 // 3):
                    self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
