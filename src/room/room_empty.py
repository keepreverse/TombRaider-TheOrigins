from src.room.room import Room


class RoomEmpty(Room):
    def init_buildings(self):
        super().init_buildings()

    def init_entities(self):
        pass
