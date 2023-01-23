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
        return '    You won\'t be able to shoot without them, so please aim better so you don\'t waste them all.'
    
    def use(self):
        return