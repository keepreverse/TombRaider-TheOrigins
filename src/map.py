import random
import var
import pygame
from pygame.surface import Surface
from const import MAP_SIZE, DOOR_POS, PORTAL_POS, ROOM_SIZE
from src.obj.building.destination import Destination
from src.obj.building.door import Door
from src.obj.entity.item.treasure import Treasure
from src.room.room_empty import RoomEmpty
from src.room.room_path import RoomPath
from src.room.room_focus import RoomFocus
from src.room.room_maze import RoomMaze
from src.room.room_square import RoomSquare
from src.room.room_chest import RoomChest
from src.room.room_h import RoomH
from src.room.room_t import RoomT
from src.room.room_x import RoomX
from src.room.room_z import RoomZ
from src.room.room_trap import RoomTrap
from src.room.room_wall import RoomWall
"""
Map create Room.
It decide the door, entry and terminal room.
It switch the room for player.
"""


class Map:
    # The all kinds of room can choose
    __ROOM_KIND = [RoomEmpty, RoomChest, RoomTrap, RoomZ, RoomT, RoomX,
                   RoomH, RoomFocus, RoomSquare, RoomMaze, RoomPath, RoomWall]

    def __init__(self):
        # If the room number is less than 20, then create another new map again.
        while not self.__init_map():
            continue
        self.__active_room_pos = self.__entry_room_pos
        # The room which has been discover.
        self.__discover_set = set()
        self.__discover_set.add(self.__entry_room_pos)
        self.__surface = Surface((200, 200)).convert_alpha()
        self.__surface.fill((255, 255, 255, 100))

    @property
    def entry_room(self):
        return self.__map[self.__entry_room_pos[0]][self.__entry_room_pos[1]]

    @property
    def active_room(self):
        return self.__map[self.__active_room_pos[0]][self.__active_room_pos[1]]

    @property
    def end_room(self):
        return self.__map[self.__end_room_pos[0]][self.__end_room_pos[1]]

    def __init_map(self):
        self.__map = [[None for j in range(MAP_SIZE[1])] for i in range(MAP_SIZE[0])]
        self.__graph = [[[] for j in range(MAP_SIZE[1])] for i in range(MAP_SIZE[0])]
        self.__entry_room_pos = (random.randint(0, MAP_SIZE[0] - 1), 0)
        self.__end_room_pos = None
        end_rooms = []
        dire = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # Use dfs to create the whole map.

        def dfs(now, prev, graph, cnt_room, depth):
            if now[0] < 0 or now[0] >= MAP_SIZE[0] or \
                    now[1] < 0 or now[1] >= MAP_SIZE[1]:
                return 0
            if prev != now:
                graph[prev[0]][prev[1]].append(now)
                graph[now[0]][now[1]].append(prev)
            if random.randint(1, 2) == 1 and depth >= 9:
                end_rooms.append(now)
                return 1
            else:
                if depth >= 7 or len(end_rooms) <= 4 or cnt_room <= 25:
                    spread_path = random.randint(2, 3)
                else:
                    spread_path = 1
                random.shuffle(dire)
                for d in dire:
                    if spread_path == 0:
                        break
                    nxt = (now[0] + d[0], now[1] + d[1])
                    if nxt[0] < 0 or nxt[0] >= MAP_SIZE[0] or \
                            nxt[1] < 0 or nxt[1] >= MAP_SIZE[1]:
                        continue
                    if nxt in end_rooms or now in graph[nxt[0]][nxt[1]]:
                        continue
                    if len(graph[nxt[0]][nxt[1]]) == 0:
                        cnt_room += dfs(nxt, now, graph, cnt_room, depth + 1)
                        spread_path -= 1
                    else:
                        graph[nxt[0]][nxt[1]].append(now)
                        graph[now[0]][now[1]].append(nxt)
                    if len(graph[nxt[0]][nxt[1]]) == 1 and not (nxt in end_rooms):
                        end_rooms.append(nxt)
                return cnt_room
        # If the room number is less then 20.
        if dfs(self.__entry_room_pos, self.__entry_room_pos, self.__graph, 0, 1) < 20:
            return False
        for i in range(MAP_SIZE[0]):
            for j in range(MAP_SIZE[1]):
                # Create the room
                if len(self.__graph[i][j]) != 0:
                    # Entry room
                    if (i, j) == self.__entry_room_pos:
                        self.__map[i][j] = RoomEmpty()
                    # End room
                    elif (i, j) in end_rooms:
                        self.__map[i][j] = RoomChest()
                    # Other room
                    else:
                        self.__map[i][j] = Map.__ROOM_KIND[random.randint(2, 11)]()
                # Add the door
                for item in self.__graph[i][j]:
                    if (item[0] - i, item[1] - j) == (0, -1):
                        to = 'up'
                    elif (item[0] - i, item[1] - j) == (0, 1):
                        to = 'down'
                    elif (item[0] - i, item[1] - j) == (-1, 0):
                        to = 'left'
                    elif (item[0] - i, item[1] - j) == (1, 0):
                        to = 'right'
                    else:
                        raise AttributeError("Illegal value of Map.__init_map.item in graph[i][j].")
                    self.__map[i][j].add_door(to)
        # Choose the real end room and put a treasure init.
        for end_room in end_rooms:
            if end_room[1] >= MAP_SIZE[1] // 2:
                self.__end_room_pos = end_room
        if self.__end_room_pos is None:
            end_room = end_rooms[random.randint(0, len(end_rooms) - 1)]
            self.__end_room_pos = end_room
        self.end_room.buildings[ROOM_SIZE[0] // 2][ROOM_SIZE[1] // 2].collectibles.append(Treasure())
        # Add a destination into the entry.
        self.entry_room.buildings[DOOR_POS['up'][0]][DOOR_POS['up'][1]] = Destination(DOOR_POS['up'])
        return True

    def walk(self, to):
        """
        Switch the display room for player.
        :param to: str. left, right, up, down.
        :return:
        """
        self.active_room.entities.remove(var.player)
        self.__active_room_pos = (self.__active_room_pos[0] + PORTAL_POS[to][0],
                                  self.__active_room_pos[1] + PORTAL_POS[to][1])
        self.__discover_set.add(self.__active_room_pos)
        for i in range(4):
            x, y = tuple(DOOR_POS.values())[i]
            dx, dy = tuple(PORTAL_POS.values())[i]
            if isinstance(self.active_room.buildings[x][y], Door) and \
               (self.__active_room_pos[0] + dx, self.__active_room_pos[1] + dy) in self.__discover_set:
                self.active_room.buildings[x][y].can_access = True
                self.active_room.buildings[x][y].on_trigger(var.player)
        self.active_room.entities.append(var.player)
        # If player move down, it will appear in the up door.
        if to == 'left':
            to = 'right'
        elif to == 'right':
            to = 'left'
        elif to == 'up':
            to = 'down'
        elif to == 'down':
            to = 'up'
        var.player.rect.center = self.active_room.buildings[DOOR_POS[to][0]][DOOR_POS[to][1]].rect.center

    def update(self):
        self.active_room.update()

    def to_surface(self, full_map=False):
        """
        Display as a little map.
        :param full_map: Choose whether to display the whole map.
        :return: Surface
        """
        surface_size = 200, 200
        x, y = surface_size[0] / (MAP_SIZE[0] + 1), surface_size[1] / (MAP_SIZE[1] + 1)
        if full_map:
            pos_list = [(i, j) for i in range(MAP_SIZE[0]) for j in range(MAP_SIZE[1]) if len(self.__graph[i][j]) != 0]
        else:
            pos_list = self.__discover_set
        for pos in pos_list:
            left, top = (pos[0] + 2/3)*x, (pos[1] + 2/3)*y
            width, height = 2/3*x, 2/3*y
            pygame.draw.rect(self.__surface, (255, 255, 255), (round(left), round(top), round(width), round(height)))
            dire = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in dire:
                nxt = pos[0] + d[0], pos[1] + d[1]
                if nxt in self.__graph[pos[0]][pos[1]]:
                    le, to = round(left + (1/6 + 1/2*d[0])*x), round(top + (1/6 + 1/2*d[1])*y)
                    wi, he = round(1/3*x), round(1/3*y)
                    if pos in self.__discover_set and nxt in self.__discover_set:
                        pygame.draw.rect(self.__surface, (100, 255, 255), (le, to, wi, he))
                    else:
                        pygame.draw.rect(self.__surface, (255, 255, 0), (le, to, wi, he))
        left, top = round((self.__active_room_pos[0] + 2/3) * x), round((self.__active_room_pos[1] + 2/3) * y)
        width, height = round(2/3*x), round(2/3*y)
        pygame.draw.rect(self.__surface, (255, 0, 0), (left, top, width, height))
        return self.__surface
