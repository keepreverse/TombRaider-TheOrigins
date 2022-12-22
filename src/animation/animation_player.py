import const
from src.animation.animation_uniform import AnimationUniform
from src.tool.vector import Vector


class AnimationPlayerStandLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["player"]["stand_left"][i % 4], Vector(-4, -32))


class AnimationPlayerStandRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["player"]["stand_right"][i % 4], Vector(-4, -32))


class AnimationPlayerMoveLeft(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["player"]["move_left"][i % 4], Vector(-4, -32))


class AnimationPlayerMoveRight(AnimationUniform):
    def __init__(self):
        super().__init__(6)
        for i in range(5):
            super().add_uniform_frame(const.IMAGE["player"]["move_right"][i % 4], Vector(-4, -32))
