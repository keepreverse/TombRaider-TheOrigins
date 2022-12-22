from src.obj.building.building import Building
from src.tool.vector import Vector
"""
Just a ground, not any special.
"""


class Ground(Building):
    def __init__(self, pos, image):
        super().__init__(pos, image, Vector(0, 0), True)
