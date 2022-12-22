import const
from src.obj.building.trap import Trap
from src.obj.building.wall import Wall
from src.room.room import Room
from const import ROOM_SIZE


class RoomSquare(Room):
    def init_buildings(self):
        super().init_buildings()
        width = ROOM_SIZE[0] - 6
        height = ROOM_SIZE[1] - 6
        for i in range(height):
            if i < height // 5 or height * 2 // 5 < i < height * 3 // 5 or height * 4 // 5 < i < height:
                self.buildings[3 + width // 5][3 + i] = Trap((3 + width // 5, 3 + i))
                self.buildings[3 + width * 4 // 5][3 + i] = Trap((3 + width * 4 // 5, 3 + i))
            else:
                self.buildings[3 + width // 5][3 + i] = Wall((3 + width // 5, 3 + i), const.IMAGE['wall'][5], (0, -12))
                self.buildings[3 + width * 4 // 5][3 + i] = Wall((3 + width * 4 // 5, 3 + i), const.IMAGE['wall'][5], (0, -12))

        for i in range(width):
            if i < width // 5 or width * 2 // 5 < i < width * 3 // 5 or width * 4 // 5 < i < width:
                self.buildings[3 + i][3 + height // 5] = Trap((3 + i, 3 + height // 5))
                self.buildings[3 + i][3 + height * 4 // 5] = Trap((3 + i, 3 + height * 4 // 5))
            else:
                self.buildings[3 + i][3 + height // 5] = Wall((3 + i, 3 + height // 5), const.IMAGE['wall'][5], (0, -12))
                self.buildings[3 + i][3 + height * 4 // 5] = Wall((3 + i, 3 + height * 4 // 5), const.IMAGE['wall'][5], (0, -12))

        for i in range(width * 2 // 5, width * 3 // 5 + 1):
            for j in range(height * 2 // 5, height * 3 // 5 + 1):
                self.buildings[3 + i][3 + j] = Wall((3 + i, 3 + j), const.IMAGE['wall'][5], (0, -12))
