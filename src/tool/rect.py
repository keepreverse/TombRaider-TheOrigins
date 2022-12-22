from src.tool.vector import Vector
"""
It's a rectangle.
It can be initialize with four, two, one argument.
It's iterable.
It can check if a point is in it or if it intersect with the other rect.
"""


class Rect:
    def __init__(self, left=0., top=0., width=0., height=0.):
        if width < 0:
            left += width
            width = -width
        if height < 0:
            top += height
            height = -height
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.__stop = 0

    @classmethod
    def init_two_arg(cls, left_top, width_height):
        return cls(left_top[0], left_top[1], width_height[0], width_height[1])

    @classmethod
    def init_one_arg(cls, left_top_width_height):
        return cls(left_top_width_height[0], left_top_width_height[1], left_top_width_height[2],
                   left_top_width_height[3])

    def copy(self):
        return Rect(self.left, self.top, self.width, self.height)

    def __iter__(self):
        return self

    def __next__(self):
        self.__stop += 1
        if self.__stop == 5:
            raise StopIteration
        return (None, self.left, self.top, self.width, self.height)[self.__stop]

    def __getitem__(self, item):
        return (self.left, self.top, self.width, self.height)[item]

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = float(value)

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, value):
        self.__top = float(value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = float(value)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = float(value)

    @property
    def right(self):
        return self.left + self.width

    @right.setter
    def right(self, value):
        self.left = float(value) - self.width

    @property
    def bottom(self):
        return self.top + self.height

    @bottom.setter
    def bottom(self, value):
        self.top = float(value) - self.height

    @property
    def center_x(self):
        return self.left + self.width / 2

    @center_x.setter
    def center_x(self, value):
        self.left = float(value) - self.width / 2

    @property
    def center_y(self):
        return self.top + self.height / 2

    @center_y.setter
    def center_y(self, value):
        self.top = float(value) - self.height / 2

    @property
    def size(self):
        return Vector(self.width, self.height)

    @size.setter
    def size(self, value):
        self.width = value[0]
        self.height = value[1]

    @property
    def left_top(self):
        return Vector(self.left, self.top)

    @left_top.setter
    def left_top(self, value):
        self.left = value[0]
        self.top = value[1]

    @property
    def left_bottom(self):
        return Vector(self.left, self.bottom)

    @left_bottom.setter
    def left_bottom(self, value):
        self.left = value[0]
        self.bottom = value[1]

    @property
    def right_top(self):
        return Vector(self.right, self.top)

    @right_top.setter
    def right_top(self, value):
        self.right = value[0]
        self.top = value[1]

    @property
    def right_bottom(self):
        return Vector(self.right, self.bottom)

    @right_bottom.setter
    def right_bottom(self, value):
        self.right = value[0]
        self.bottom = value[1]

    @property
    def center(self):
        return Vector(self.center_x, self.center_y)

    @center.setter
    def center(self, value):
        self.center_x = value[0]
        self.center_y = value[1]

    @property
    def left_center(self):
        return Vector(self.left, self.center_y)

    @left_center.setter
    def left_center(self, value):
        self.left = value[0]
        self.center_y = value[1]

    @property
    def right_center(self):
        return Vector(self.right, self.center_y)

    @right_center.setter
    def right_center(self, value):
        self.right = value[0]
        self.center_y = value[1]

    @property
    def top_center(self):
        return Vector(self.center_x, self.top)

    @top_center.setter
    def top_center(self, value):
        self.center_x = value[0]
        self.top = value[1]

    @property
    def bottom_center(self):
        return Vector(self.center_x, self.bottom)

    @bottom_center.setter
    def bottom_center(self, value):
        self.center_x = value[0]
        self.bottom = value[1]

    def contain(self, point):
        return self.left < point[0] < self.right and self.top < point[1] < self.bottom

    def intersect(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError('Rect.intersect.rect must be Rect type.')
        if self.left > rect.right or self.right < rect.left:
            return False
        elif self.top > rect.bottom or self.bottom < rect.top:
            return False
        else:
            return True
