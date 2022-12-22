import const
from src.obj.entity.item.collectible import Collectible
"""
Player can't shoot without bullet.
"""


class Bullet(Collectible):
    def __init__(self, amount=1):
        super().__init__('Bullet', const.IMAGE['bullet'][0], False, amount)

    @property
    def information(self):
        return '    They are just some bullets, but without them you can\'t shoot anymore, so please take a good ' \
               'use of it. '
