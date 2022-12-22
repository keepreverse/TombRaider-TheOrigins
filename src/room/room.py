import random
from pygame.surface import Surface
import const
import var
from const import ROOM_SIZE, TILE_SIZE, IMAGE, DOOR_POS, PORTAL_POS
from src.obj.building.building import Building
from src.obj.building.door import Door
from src.obj.building.ground import Ground
from src.obj.building.portal import Portal
from src.obj.building.trigger_building import TriggerBuilding
from src.obj.building.wall import Wall
from src.obj.entity.creature.creature import Creature
from src.obj.entity.creature.guard import Guard
from src.obj.entity.creature.monster import Monster
from src.obj.entity.creature.mummy import Mummy
from src.obj.entity.creature.pharaoh import Pharaoh
from src.obj.entity.item.collectible import Collectible
from src.obj.entity.item.key import Key
from src.tool.bubble_sort import bubble_sort
from src.tool.quadtree import QuadTree
from src.tool.rect import Rect
"""
The init_buildings() and init_entities() determine what the room look like and what monsters it has.
It update all the things display in the screen.
The trigger building update, the entity update.
The collide checking between entity and building. O(n)
The collide checking between entity and entity. Using QuadTree. O(n*log(n)) 
"""


class Room:
    def __init__(self):
        # Store the buildings. __buildings[i][j] represent a certain building.
        self.__buildings = [[Building((i, j)) for j in range(ROOM_SIZE[1])] for i in range(ROOM_SIZE[0])]
        # Store the entities in the Room.
        self.__entities = []
        # Store the trigger buildings in the Room.
        self.__trigger_buildings = []
        # Initialize the Room.
        self.init_buildings()
        self.init_entities()
        # Add the trigger buildings.
        for _ in self.__buildings:
            for building in _:
                if isinstance(building, TriggerBuilding):
                    self.__trigger_buildings.append(building)
        # Room draw all the things on the __surface and return it to interface, finally show on the screen.
        self.__surface = Surface((TILE_SIZE[0] * ROOM_SIZE[0], TILE_SIZE[1] * ROOM_SIZE[1]))
        self.__surface.set_colorkey((0, 0, 0))
        # The blit point on the screen, use to calculate the player's shoot direction.
        self.__blit_point = (0, 0)

    @property
    def buildings(self):
        return self.__buildings

    @property
    def entities(self):
        return self.__entities

    @property
    def blit_point(self):
        return self.__blit_point

    def init_buildings(self):
        """
        It just initialize the wall around the room and create ground within the room.
        :return:
        """
        for i, row in enumerate(self.buildings):
            for j, col in enumerate(row):
                if i == 2 and 2 <= j <= ROOM_SIZE[1] - 4:
                    self.buildings[i][j] = Wall((i, j), IMAGE['wall'][0], (0, -12))
                elif i == 2 and j == ROOM_SIZE[1] - 3:
                    self.buildings[i][j] = Wall((i, j), IMAGE['wall'][4], (0, -12))
                elif i == ROOM_SIZE[0] - 3 and 2 <= j <= ROOM_SIZE[1] - 4:
                    self.buildings[i][j] = Wall((i, j), IMAGE['wall'][1], (0, -12))
                elif i == ROOM_SIZE[0] - 3 and j == ROOM_SIZE[1] - 3:
                    self.buildings[i][j] = Wall((i, j), IMAGE['wall'][3], (0, -12))
                elif (j == 2 or j == ROOM_SIZE[1] - 3) and 2 <= i <= ROOM_SIZE[0] - 3:
                    self.buildings[i][j] = Wall((i, j), IMAGE['wall'][2], (0, -12))
                elif 2 < i < ROOM_SIZE[0] - 3 and 2 < j < ROOM_SIZE[1] - 3:
                    self.buildings[i][j] = Ground((i, j), IMAGE['ground'][random.randint(0, 7)])

    def init_entities(self):
        """
        Randomly create the monster in the room if it's on the ground.
        One monster among them has a key.
        :return:
        """
        cnt = 0
        while cnt != var.enemies_number:
            pos = (random.randint(0, ROOM_SIZE[0] - 1), random.randint(0, ROOM_SIZE[1] - 1))
            if not isinstance(self.buildings[pos[0]][pos[1]], Ground):
                continue
            _ = random.randint(1, 3)
            if _ == 1:
                self.entities.append(Guard(pos))
            elif _ == 2:
                self.entities.append(Mummy(pos))
            elif _ == 3:
                self.entities.append(Pharaoh(pos))
            cnt += 1
        self.entities[random.randint(0, var.enemies_number - 1)].collectibles.append(Key())

    def add_door(self, to):
        """
        Add door for the room. It should be called by map.
        The portal will be added at the same time.
        :param to: str. It only has four value: left, right, up, down. Represent which door should be add.
        :return:
        """
        x1, y1 = DOOR_POS[to]
        x2, y2 = DOOR_POS[to][0] + PORTAL_POS[to][0], DOOR_POS[to][1] + PORTAL_POS[to][1]
        if to == 'left':
            closed_image = const.IMAGE['door'][2]
            opened_image = const.IMAGE['door'][3]
        elif to == 'right':
            closed_image = const.IMAGE['door'][4]
            opened_image = const.IMAGE['door'][5]
        else:
            closed_image = const.IMAGE['door'][0]
            opened_image = const.IMAGE['door'][1].copy()
            opened_image.blit(const.IMAGE['ground'][random.randint(0, 7)], (0, 24))
            opened_image.blit(const.IMAGE['door'][1], (0, 0))
        self.buildings[x1][y1] = Door((x1, y1), closed_image, opened_image)
        self.buildings[x2][y2] = Portal((x2, y2), to)

    def update(self):
        self.__update_entities()
        self.__update_collide()
        self.__update_trigger_buildings()

    def __update_entities(self):
        for entity in self.entities:
            entity.update()

    def __update_collide(self):
        """
        First check the collide between entity and buildings.
        Then check the collide between entity and entities.
        :return:
        """
        # entities with buildings:
        for entity in self.entities:
            buildings = []
            # find all the buildings collide with entity
            _left = int(entity.rect.left) // TILE_SIZE[0]
            _right = int(entity.rect.right) // TILE_SIZE[0]
            _top = int(entity.rect.top) // TILE_SIZE[1]
            _bottom = int(entity.rect.bottom) // TILE_SIZE[1]
            # left_top
            buildings.append(self.buildings[_left][_top])
            # right_top
            if _left != _right:
                buildings.append(self.buildings[_right][_top])
            # left_bottom
            if _top != _bottom:
                buildings.append(self.buildings[_left][_bottom])
            # right_bottom
            if _left != _right and _top != _bottom:
                buildings.append(self.buildings[_right][_bottom])
            # process the collide.
            entity.collide_building(*buildings)
        # entity and entity, use quadtree.
        quadtree = QuadTree(Rect.init_two_arg((0, 0), self.__surface.get_size()))
        for entity in self.entities:
            quadtree.add(entity)
        for entity in self.entities:
            # Only checking the creature will other entity.
            if not isinstance(entity, Creature):
                continue
            entities = []
            for collide_entity in quadtree.qry(entity):
                # Only check the different type of entity collide.
                # Monsters don't collide with Collectible.(They can't pick them up.)
                if type(collide_entity) == type(entity) or \
                        (isinstance(entity, Monster) and isinstance(collide_entity, Collectible)):
                    continue
                if entity.rect.intersect(collide_entity.rect):
                    entities.append(collide_entity)
            # Process the collide.
            entity.collide_entity(*entities)

    def __update_trigger_buildings(self):
        for trigger_building in self.__trigger_buildings:
            trigger_building.update()

    def draw(self, surface):
        """
        Use bubble_sort to sort the entity according to the rect.bottom value in ascending order.
        :param surface: Surface.
        :return:
        """
        if not isinstance(surface, Surface):
            raise TypeError("Room.draw.surface must be Surface type.")
        # bubble sort.
        bubble_sort(self.entities, lambda entity1, entity2: entity1.rect.bottom - entity2.rect.bottom)
        self.__surface.fill((0, 0, 0))
        cnt = 0
        for j in range(ROOM_SIZE[1]):
            # draw the buildings
            for i in range(ROOM_SIZE[0]):
                if self.buildings[i][j] is not None:
                    self.buildings[i][j].draw(self.__surface)
            # draw the entities
            while cnt < len(self.entities) and self.entities[cnt].rect.bottom // TILE_SIZE[1] == j:
                self.entities[cnt].draw(self.__surface)
                cnt += 1
        # calculate the blit point. (Though it's the same every frame.)
        self.__blit_point = ((surface.get_width() - self.__surface.get_width()) // 2,
                             (surface.get_height() - self.__surface.get_height()) // 2)
        surface.blit(self.__surface, self.__blit_point)
