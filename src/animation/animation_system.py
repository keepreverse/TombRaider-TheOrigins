from src.animation.animation import Animation
"""
Only the obj which has animation system can play an animation.
It should be initialized with the animation in the animation repository.
You can also call the add_animation() to add more animation.
Make sure that every frame call update() or the animation will not be play.
Get the image and delta_pos for the obj through AnimationSystem.image and AnimationSystem.delta_pos. 
Use AnimationSystem.play(name) to play the animation you want to play.
Like AnimationSystem.play("stand_left") to let the character show like standing left.
"""


class AnimationSystem:
    # animations should from const.ANIMATION_REPOSITORY
    def __init__(self, **animations):
        self.__animations = animations
        self.__animation = None
        self.__animation_name = ""
        self.__cnt = 0
        self.__now = 0

    @property
    def image(self):
        if self.__animation is None:
            raise ValueError("AnimationSystem animation is empty.")
        else:
            return self.__animation.images[self.__now]

    @property
    def vector(self):
        if self.__animation is None:
            raise ValueError("AnimationSystem animation is empty.")
        else:
            return self.__animation.vectors[self.__now]

    @property
    def animation_name(self):
        """
        :return: animation_name which is playing.
        """
        return self.__animation_name

    def add_animation(self, animation_name, animation):
        """
        Add another animation.
        :param animation_name: str
        :param animation: Animation
        :return:
        """
        if not isinstance(animation_name, str) or not isinstance(animation, Animation):
            raise TypeError("AnimationSystem.add_animation name: str, animation: animation")
        if self.__animations[animation_name] is not None:
            raise Exception("AnimationSystem %s animation is already exist." % animation_name)
        self.__animations[animation_name] = animation

    def play(self, animation_name):
        """
        Play the certain animation.
        If it's the same animation as just now, it make no sense.
        :param animation_name: str
        :return:
        """
        if self.__animations[animation_name] is None:
            raise ValueError("AnimationSystem %s animation is not exist." % animation_name)
        if self.__animation_name != animation_name:
            self.__animation = self.__animations[animation_name]
            self.__animation_name = animation_name
            self.reset()

    def reset(self):
        """
        Reset the animation.
        Every time you call play(), it would be called, too.
        :return:
        """
        self.__cnt = 0
        self.__now = 0

    def update(self):
        """
        It should be called every frame.
        :return:
        """
        if self.__animation is None:
            return
        if self.__animation.total_frames == 0:
            raise Exception("AnimationSystem animation not initialized.")
        if self.__now != self.__animation.total_frames - 1:
            if self.__cnt == self.__animation.frames[self.__now + 1]:
                self.__now += 1
            self.__cnt += 1
        else:
            self.reset()
