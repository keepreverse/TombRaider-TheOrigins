import const
from src.animation.animation_uniform import AnimationUniform
from src.tool.vector import Vector


class AnimationTrap(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(3):
            super().add_uniform_frame(const.IMAGE['trap'][0], Vector(0, 0))
        super().add_uniform_frame(const.IMAGE["trap"][1], Vector(0, 0))
        super().add_uniform_frame(const.IMAGE["trap"][2], Vector(0, 0))
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["trap"][3], Vector(0, 0))
        super().add_uniform_frame(const.IMAGE["trap"][4], Vector(0, 0))
        super().add_uniform_frame(const.IMAGE["trap"][5], Vector(0, 0))
