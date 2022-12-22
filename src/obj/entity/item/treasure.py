import const
from src.obj.entity.item.collectible import Collectible
"""
It will be store in the terminal room.
If player get it and take it back to the entry door.
The game will win.
"""


class Treasure(Collectible):
    def __init__(self):
        super().__init__('Treasure', const.IMAGE['treasure'][0])

    @property
    def information(self):
        return '    The treasure in the maze. What a big ablaze diamond! Take it back to the entry and get out from ' \
                'the trash place. Hurry up!'
