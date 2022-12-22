from pygame.surface import Surface
from pygame import draw
from src.obj.entity.item.shooting_bullet import ShootingBullet
from src.tool.rect import Rect
from src.tool.vector import Vector
"""
The only kind of bullet in the game.
Red circle little bullet.
"""


class BubbleBullet(ShootingBullet):
    def __init__(self, pos, speed_dir, speed_mag, damage, owner):
        image = Surface((9, 9))
        image.set_colorkey((0, 0, 0))
        draw.circle(image, (255, 0, 0), (4, 4), 4)
        vector = Vector(-4, -4)
        super().__init__(Rect(pos[0], pos[1], 3, 3), image, vector, speed_dir, speed_mag, damage, owner)
