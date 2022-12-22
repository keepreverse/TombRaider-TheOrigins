import const
from const import ROOM_SIZE
from src.obj.building.trap import Trap
from src.obj.building.wall import Wall
from src.room.room import Room


class RoomX(Room):
    def init_buildings(self):
        super().init_buildings()
        width = ROOM_SIZE[0] - 6
        height = ROOM_SIZE[1] - 6
        for i in range(width):
            for j in range(height):
                if (width // 5 <= i <= width * 4 // 5) and \
                        (round(j + (height / width) * i) == height - 1 or j == round(height / width * i)):
                    self.buildings[i + 3][j + 3] = Trap((i + 3, j + 3))
                if (i == width // 5 and height * 4 // 5 <= j <= height) or \
                        (i == width * 4 // 5 and j <= height // 5) or \
                        (j == height // 5 and i <= width // 5) or \
                        (j == height * 4 // 5 and width * 4 // 5 <= i <= width):
                    self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))

