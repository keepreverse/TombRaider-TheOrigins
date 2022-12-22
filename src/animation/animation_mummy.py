import const
from src.animation.animation_uniform import AnimationUniform
from src.tool.vector import Vector


class AnimationMummyStandLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["mummy"]["stand_left"][i % 4], Vector(-10, -46))


class AnimationMummyStandRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["mummy"]["stand_right"][i % 4], Vector(-10, -46))


class AnimationMummyMoveLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["mummy"]["move_left"][i % 4], Vector(-10, -46))


class AnimationMummyMoveRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["mummy"]["move_right"][i % 4], Vector(-10, -46))
