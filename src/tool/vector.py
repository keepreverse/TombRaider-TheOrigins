import math
import random
"""
The vector which has x and y attribute.
See the code in detail.
"""


class Vector:
    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y
        self.__stop = 0

    @classmethod
    def init_one_arg(cls, x_y):
        return cls(x_y[0], x_y[1])

    @classmethod
    def random_normalized_vector(cls):
        degree = random.randint(0, 359) / 180 * math.pi
        return cls(math.cos(degree), math.sin(degree))

    def copy(self):
        return Vector(self.x, self.y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = float(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = float(value)

    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("The length of Vector can't less than zero.")
        length, value = self.length, float(value)
        if self.length == 0:
            return
        self.x *= value / length
        self.y *= value / length

    @property
    def sin(self):
        if self.length == 0:
            raise Exception("The sin for the Vector doesn't exist.")
        return self.y / self.length

    @property
    def cos(self):
        if self.length == 0:
            raise Exception("The cos for the Vector doesn't exist.")
        return self.x / self.length

    @property
    def tan(self):
        if self.x == 0:
            raise Exception("The sin for the Vector doesn't exist.")
        return self.y / self.x

    def __add__(self, vector):
        return Vector(self.x + vector[0], self.y + vector[1])

    def __sub__(self, vector):
        return Vector(self.x - vector[0], self.y - vector[1])

    def __mul__(self, number):
        number = float(number)
        return Vector(self.x*number, self.y*number)

    def __truediv__(self, number):
        number = float(number)
        return self*(1/number)

    def __iter__(self):
        return self

    def __next__(self):
        self.__stop += 1
        if self.__stop == 3:
            raise StopIteration
        return (None, self.x, self.y)[self.__stop]

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise ValueError("Vector.__getitem__.item must be 0 or 1.")

    def rotate(self, angle):
        """
        When angle is positive, it rotate counter clockwise.
        :param angle: float or int.
        :return: Vector
        """
        if self.length == 0:
            return Vector(0, 0)
        angle = angle / 180 * math.pi
        x = self.y * math.cos(angle) + self.x * math.sin(angle)
        y = self.x * math.cos(angle) - self.y * math.sin(angle)
        return Vector(x, y)

    def dot(self, vector):
        return self.x * vector[0] + self.y * vector[1]

    def cross(self, vector):
        return self.x * vector[1] - self.y * vector[0]

    def normalize(self):
        if self.length == 0:
            return self
        else:
            return self / self.length

    def angle_to(self, vector):
        """
        When angle is positive, it rotate counter clockwise.
        :param vector: Vector
        :return: Vector
        """
        vector = Vector.init_one_arg(vector)
        if self.length == 0 or vector.length == 0:
            return 0
        sin = self.sin * vector.cos - self.cos * vector.sin
        cos = self.cos * vector.cos + self.sin * vector.sin
        if cos > 0:
            ans = math.asin(sin)
        elif sin >= 0:
            ans = math.acos(cos)
        else:
            ans = -math.acos(cos)
        ans = ans/math.pi*180
        return ans

    def dis_to(self, vector):
        return (self - vector).length
