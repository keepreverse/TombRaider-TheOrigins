from pygame.surface import Surface
from src.tool.vector import Vector
"""
Just use add_key_frames function.
The animation will be play as a sequence.
"""


class Animation:
    def __init__(self):
        self.__frames = []
        self.__images = []
        self.__vectors = []
        self.__tot = 0

    @property
    def total_frames(self):
        return self.__tot

    @property
    def images(self):
        return self.__images

    @property
    def vectors(self):
        return self.__vectors

    @property
    def frames(self):
        return self.__frames

    def add_key_frame(self, frame, image, vector=Vector(0, 0)):
        """
        Add the key frame for the animation.
        Each time call it, it should be promise the frame is greater than the last call except the first call.
        :param frame: int
        :param image: Surface
        :param vector: Vector
        :return: None
        """
        if not isinstance(frame, int) or not isinstance(image, Surface) or not isinstance(vector, Vector):
            raise ValueError("animation.add_frame, frame: int, image: Surface, delta_pos: Vector")
        self.__frames.append(frame)
        self.__images.append(image)
        self.__vectors.append(vector)
        self.__tot += 1
