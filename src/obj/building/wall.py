from src.obj.building.building import Building
"""
Any entity can't can through it.
"""


class Wall(Building):
    def __init__(self, pos, image, vector):
        super().__init__(pos, image, vector)
