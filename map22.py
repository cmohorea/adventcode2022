INFINITY = 9999999
OUT_OF_RANGE = "-"
UNDEFINED = " "
EMPTY = "."
NONEMPTY = "#"

class AdventMap ():

    def __init__ (self):
        self.set_size (INFINITY, INFINITY, -INFINITY, -INFINITY)
        self.map = {}

    def set_size (self, x, y, xx, yy):
        self.minx = x
        self.maxx = xx
        self.miny = y
        self.maxy = yy


    def set_item (self, x, y, value):

        if x < self.minx:
            self.minx = x
        if x > self.maxx:
            self.maxx = x
        if y < self.miny:
            self.miny = y
        if y > self.maxy:
            self.maxy = y

        if not self.map.get (y):
            self.map[y] = {}
        self.map[y][x] = value

    def draw_line (self, px, py, x, y, item = NONEMPTY):

        if px == x:    #Y line
            step = (y - py) // abs (y - py)
            for yy in range (py, y + step, step):
                self.set_item (x, yy, item)
        elif py == y:    #X line
            step = (x - px) // abs (x - px)
            for xx in range (px, x + step, step):
                self.set_item (xx, y, item)
        else:
            # cannot draw diagonals
            return
    
    def set_item_safe (self, x, y, value):
        if x in range (self.minx, self.maxx + 1) and y in range (self.miny, self.maxy + 1):
            self.set_item (x, y, value)

    def get_item (self, x, y):
        return self.map.get(y,{}).get(x,UNDEFINED)

    def get_line (self, y):
        line = ""
        for x in range (self.minx, self.maxx+1):
            line += self.get_item(x,y)
        return line

    def print_map(self):
        self.print_map_abs (self.minx, self.miny, self.maxx, self.maxy)

    def print_top(self):
        self.print_map_abs (self.minx, self.maxy - 50, self.maxx, self.maxy)

    def print_map_abs (self, x1, y1, x2, y2):
        print(f"X: {x1:3}:{x2}")
        for y in range (y1, y2+1):
            print(f"{y:3}: ", end="")
            for x in range (x1, x2+1):
                print (self.get_item(x,y), end="")
            print()
        print()


if __name__ == '__main__':
    exit(0)
# mymap = AdventMap ()
# mymap.set_item(1,1,"*")
# mymap.set_item(10,10,"*")
# mymap.print_map()

