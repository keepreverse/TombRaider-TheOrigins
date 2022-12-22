from src.animation.animation import Animation
from src.tool.vector import Vector
"""
This is another kind of animation.
It will be play in a uniform speed.
You should call add_uniform_frame rather than add_key_frame to add the key frame.
"""


class AnimationUniform(Animation):
    def __init__(self, interval_frames):
        super().__init__()
        self.__interval_frames = int(interval_frames)

    @property
    def interval_frames(self):
        return self.__interval_frames

    def add_key_frame(self, frame, image, vector=Vector(0, 0)):
        raise Exception("AnimationUniform should use add_uniform_frame instead of add_key_frame.")

    def add_uniform_frame(self, image, vector=Vector(0, 0)):
        super().add_key_frame(self.total_frames * self.__interval_frames, image, vector)
