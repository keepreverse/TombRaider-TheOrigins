import const
from src.animation.animation_uniform import AnimationUniform
from src.tool.vector import Vector


class AnimationGuardStandLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(4):
            super().add_uniform_frame(const.IMAGE["guard"]["stand_left"][i % 3], Vector(-2, -36))


class AnimationGuardStandRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(4):
            super().add_uniform_frame(const.IMAGE["guard"]["stand_right"][i % 3], Vector(-2, -36))


class AnimationGuardMoveLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["guard"]["move_left"][i % 4], Vector(-2, -36))


class AnimationGuardMoveRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["guard"]["move_right"][i % 4], Vector(-2, -36))
