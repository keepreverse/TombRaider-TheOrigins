from src.obj.building.building import Building
"""
When player collide with it, on_trigger() will be called.
The new_image, new_vector, old_image, old_vector just use to store the image and delta_pos.
They are not necessary, you can put None for new_image and (0, 0) for new_vector.
"""


class TriggerBuilding(Building):
    def __init__(self, pos, image, vector, can_access, can_destroy,
                 new_image, new_vector):
        super().__init__(pos, new_image, new_vector, can_access, can_destroy)
        self.can_trigger = True
        self.__new_image = self.image
        self.__new_vector = self.vector
        self.__old_image = self.image = image
        self.__old_vector = self.vector = vector

    @property
    def can_trigger(self):
        return self.__can_trigger

    @can_trigger.setter
    def can_trigger(self, value):
        if not isinstance(value, bool):
            raise TypeError("TriggerBuilding.can_trigger must be bool type.")
        self.__can_trigger = value

    @property
    def new_image(self):
        return self.__new_image

    @property
    def new_vector(self):
        return self.__new_vector

    @property
    def old_image(self):
        return self.__old_image

    @property
    def old_vector(self):
        return self.__old_vector

    def update(self):
        pass

    def on_trigger(self, entity):
        pass
