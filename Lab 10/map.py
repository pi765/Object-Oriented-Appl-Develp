# Lab 10
# Kamal Ali & William Nguyen
# 10/30/2024
# Map singleton, reads from map.txt and can show the map tiles

class Map:  # singleton
    _instance = None
    _initialized = False

    def __new__(cls, *args):        # overridden __new__
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Map._initialized:
            self._map = []      # 2d list
            with open("map.txt", "r") as file:          # read from file
                for row in file:
                    items = list(row.strip())        # change each line into a list of characters
                    self._map.append(items)          # add each line of the file as an item in a 2d list

            self._revealed = []                 # 2d list with all false
            for r in range(len(self._map)):     # loop throughout all locations on the map
                listTemp = []   # inner lists
                for c in range(len(self._map[r])):
                    listTemp.append(False)
                self._revealed.append(listTemp) # [[False, False,...], [False, False,...],...]

            Map._initialized = True

    def __getitem__(self, row):
        return self._map[row]   # return sepecified row

    def __len__(self):
        return len(self._map)   # returns number of rows

    def show_map(self, loc):
        full_map = ""
        for r in range(len(self._map)):
            for c in range(len(self._map[r])):
                if (r, c) == (loc[0], loc[1]):      # check for user's location
                    full_map += "*"
                elif self._revealed[r][c] == True:  # show map locations if matching position in self._revealed is True
                    full_map += self._map[r][c]
                else:
                    full_map += "x"                 # X if not revealed
            full_map += "\n"                        # new row
        return full_map     # return a string (5x5 Matrix of characters)

    def reveal(self, loc):
        r = loc[0]
        c = loc[1]
        self._revealed[r][c] = True     # mark user's location as revealed

    def remove_at_loc(self, loc):
        r = loc[0]
        c = loc[1]
        self._map[r][c] = 'n'       # replace the location with a 'n'