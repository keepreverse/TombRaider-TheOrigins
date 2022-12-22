import const
from src.obj.building.trap import Trap
from src.obj.building.wall import Wall
from src.room.room import Room


class RoomTrap(Room):
    def init_buildings(self):
        super().init_buildings()
        width = const.ROOM_SIZE[0] - 6
        height = const.ROOM_SIZE[1] - 6
        for i in range(width // 6, width * 2 // 6 + 1):
            for j in range(height // 6, height * 2 // 6 + 1):
                self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
            for j in range(height * 4 // 6, height * 5 // 6 + 1):
                self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
        for i in range(width * 4 // 6, width * 5 // 6 + 1):
            for j in range(height // 6, height * 2 // 6 + 1):
                self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
            for j in range(height * 4 // 6, height * 5 // 6 + 1):
                self.buildings[i + 3][j + 3] = Wall((i + 3, j + 3), const.IMAGE['wall'][5], (0, -12))
        for i in range(width * 2 // 6 + 1, width * 4 // 6):
            j = height * 2 // 6 + 1
            self.buildings[i + 3][j + 3] = Trap((i + 3, j + 3))
            j = height * 4 // 6 - 1
            self.buildings[i + 3][j + 3] = Trap((i + 3, j + 3))
        for j in range(height * 2 // 6 + 1, height * 4 // 6):
            i = width * 2 // 6 + 1
            self.buildings[i + 3][j + 3] = Trap((i + 3, j + 3))
            i = width * 4 // 6 - 1
            self.buildings[i + 3][j + 3] = Trap((i + 3, j + 3))
