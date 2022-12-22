import const
from src.obj.building.wall import Wall
from src.room.room import Room


class RoomT(Room):
    def init_buildings(self):
        super().init_buildings()
        width = const.ROOM_SIZE[0] - 6
        height = const.ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if (i == width // 2 and height // 5 <= j <= height * 4 // 5) or \
                        (j == height // 5 and width // 5 <= i <= width * 4 // 5):
                    self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
