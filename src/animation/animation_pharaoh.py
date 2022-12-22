import const
from src.animation.animation_uniform import AnimationUniform
from src.tool.vector import Vector


class AnimationPharaohStandLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["pharaoh"]["stand_left"][i % 4], Vector(-2, -38))


class AnimationPharaohStandRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["pharaoh"]["stand_right"][i % 4], Vector(-2, -38))


class AnimationPharaohMoveLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["pharaoh"]["move_left"][i % 4], Vector(-2, -38))


class AnimationPharaohMoveRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["pharaoh"]["move_right"][i % 4], Vector(-2, -38))
