import re
from map import AdventMap, UNDEFINED, INFINITY

TXTFILE = "day15.txt"
TARGETLINE = 2000000
TXTFILE = "day15.txt1"
TARGETLINE = 10

EMPTY = " "
SENSOR = "S"
BEAKON = "B"
RANGE = "#"


map = AdventMap ()
tpl = re.compile ("[\-\d]+")

def cover_it (sx, sy, bx, by):

    dist = abs (bx-sx) + abs (by-sy)
    for y in range (- dist, dist + 1):
        # if sy + y == TARGETLINE: # only interesting line
            for x in range (abs (y) - dist,  dist - abs (y) + 1):
                if map.get_item (sx + x, sy + y) == UNDEFINED:
                    map.set_item (sx + x, sy + y, RANGE)
        # print (x, y)
        # map.print_map()

minx = INFINITY
miny = INFINITY
maxx = -INFINITY
maxy = -INFINITY

cover = []
with open(TXTFILE, "r") as f:
    for line in f:
        sx, sy, bx, by = tpl.findall(line)
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        # print(f'Match found: Beacon {bx}:{by}, sensor {sx}:{sy}')
        map.set_item (sx, sy, "S")
        map.set_item (bx, by, "B")
        cover_it (sx,sy, bx, by)
        print (".", end="")

print ("coverage complete")

map.print_map()
line = map.get_line(TARGETLINE)
print (line.count(RANGE))
