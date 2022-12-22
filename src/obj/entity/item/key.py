import const
from src.obj.entity.item.collectible import Collectible
"""
Use the key to open the door.
"""


class Key(Collectible):
    def __init__(self, amount=1):
        super().__init__("Key", const.IMAGE['key'][0], False, amount)

    @property
    def information(self):
        return '    Look at this golden key, it must be expensive. But there has more valuable treasure in this maze, '\
                'and the only way to open the door is to use this key. It\'s not reusable thought.'
