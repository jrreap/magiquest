from random import randint
from random import choice
import arcade

'''
Based off the roguelike game example on arcade.academy

Modified by Jaydon Reap
'''

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 35
MAX_ITEMS_PER_ROOM = 2


class Rect:
    # a rectangle on the map. used to characterize a room.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        return center_x, center_y

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


class GameMap:
    def __init__(self, width: int, height: int, dungeon_level: int = 1):
        self.map_width = width
        self.map_height = height
        self.dungeon_level = dungeon_level
        self.tiles = [
            [1 for _ in range(self.map_height)] for _ in range(self.map_width)
        ]

    def make_map(
        self, level: int
    ):
        rooms = []
        num_rooms = 0
        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(MAX_ROOMS):
            # random width and height
            w = randint(ROOM_MIN_SIZE, ROOM_MIN_SIZE)
            h = randint(ROOM_MIN_SIZE, ROOM_MIN_SIZE)

            # random position without going out of the boundaries of the map
            x = randint(0, self.map_width - w - 1)
            y = randint(0, self.map_height - h - 1)

            # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)

            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid

                # "paint" it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    self.tiles[new_x][new_y] = 22
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel

                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    center_of_last_room_x = new_x
                    center_of_last_room_y = new_y

                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1

        #self.tiles[center_of_last_room_x][center_of_last_room_y] = TILE.STAIRS_DOWN

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                if self.tiles[x][y] != 22:
                    self.tiles[x][y] = 0

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if self.tiles[x][y] != 22:
                self.tiles[x][y] = 0

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if self.tiles[x][y] != 22:
                self.tiles[x][y] = 0
