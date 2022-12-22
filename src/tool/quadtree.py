from const import ENTITY_CAPACITY
from src.tool.rect import Rect
"""
Use to reduce the time complexity for collide checking.
"""


class QuadTree:
    def __init__(self, rect):
        self.__rect = rect
        self.__entities = []
        self.__children = None

    @property
    def rect(self):
        return self.__rect

    @property
    def left_top_rect(self):
        return Rect.init_two_arg(self.rect.left_top, self.rect.size/2)

    @property
    def right_top_rect(self):
        return Rect.init_two_arg(self.rect.top_center, self.rect.size/2)

    @property
    def left_bottom_rect(self):
        return Rect.init_two_arg(self.rect.left_center, self.rect.size/2)

    @property
    def right_bottom_rect(self):
        return Rect.init_two_arg(self.rect.center, self.rect.size/2)

    def __collide_child(self, entity):
        """
        See if the entity can put into any one of the children completely.
        :param entity: Entity.
        :return: int or None. The index in the __children list. None represent it can't put into any children rect.
        """
        if entity.rect.right < self.rect.center_x:
            if entity.rect.bottom < self.rect.center_y:
                return 0
            elif entity.rect.top > self.rect.center_y:
                return 2
            else:
                return None
        elif entity.rect.left > self.rect.center_x:
            if entity.rect.bottom < self.rect.center_y:
                return 1
            elif entity.rect.top > self.rect.center_y:
                return 3
            else:
                return None
        else:
            return None

    def add(self, entity):
        """
        Add an entity into the Tree.
        :param entity: Entity
        :return:
        """
        collide_child = self.__collide_child(entity)
        # If the entity can't put into any one of the children.
        # Then put into this node.
        if collide_child is None:
            self.__entities.append(entity)
            return
        # If the children not create.
        if self.__children is None:
            # If the number of the entities greater or equal to the capacity of one node.
            if len(self.__entities) >= ENTITY_CAPACITY:
                self.__children = [QuadTree(self.left_top_rect), QuadTree(self.right_top_rect),
                                   QuadTree(self.left_bottom_rect), QuadTree(self.right_bottom_rect)]
                # Put into the child.
                self.__children[collide_child].add(entity)
                # Put the original entities in this node into the child if they can.
                for entity in self.__entities:
                    collide_child = self.__collide_child(entity)
                    if collide_child is not None:
                        self.__children[collide_child].add(entity)
                        self.__entities.remove(entity)
            # Put into this node.
            else:
                self.__entities.append(entity)
        # Put into child.
        else:
            self.__children[collide_child].add(entity)

    def qry(self, entity):
        """
        Query the entity which MAY collide with the given entity.
        :param entity: Entity
        :return: [Entity]
        """
        entities = []
        if self.__children is not None:
            collide_child = self.__collide_child(entity)
            # If it collide with not only one child.
            if collide_child is None:
                # Check the child and add the entities.
                if entity.rect.left < self.rect.center_x:
                    if entity.rect.top < self.rect.center_y:
                        entities += self.__children[0].__get_all_entities()
                    if entity.rect.bottom > self.rect.center_y:
                        entities += self.__children[2].__get_all_entities()
                if entity.rect.right > self.rect.center_x:
                    if entity.rect.top < self.rect.center_y:
                        entities += self.__children[1].__get_all_entities()
                    if entity.rect.bottom > self.rect.center_y:
                        entities += self.__children[3].__get_all_entities()
            else:
                entities += self.__children[collide_child].qry(entity)
        # Add the entities in this node.
        entities += self.__entities
        return entities

    def __get_all_entities(self):
        entities = []
        if self.__children is not None:
            for child in self.__children:
                entities += child.__get_all_entities()
        entities += self.__entities
        return entities
