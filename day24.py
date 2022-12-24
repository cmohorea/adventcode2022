# import map22, re
from map22 import INFINITY
from map22 import AdventMap
from collections import deque
import math

TXTFILE = "day24.txt"

EMPTY = " "
OPEN = "."
BLIZZARD = ["<",">","^","v"]

DIRS = { 
    "^": [0, -1], 
    "v": [0, 1], 
    "<": [-1, 0], 
    ">": [1, 0] 
}

# ------------------------------------------------------
def bliz_map (time):

    # global map

    for y in range (map.miny+1, map.maxy):
        for x in range (map.minx+1, map.maxx):
            map.set_item (x,y,OPEN)

    for id in range (len (blizz_start) ):
        dx, dy = DIRS[ blizz_type[id] ]
        x = (blizz_start[id][0] - 1 + dx * time) % mod_x + 1 
        y = (blizz_start[id][1] - 1 + dy * time) % mod_y + 1 

        # p = map.get_item (x,y)
        # if p ==OPEN:
        #     v = blizz_type [id]
        # elif p in BLIZZARD:
        #     v = "2"
        # else:
        #     v = str (int (p) + 1)
        
        map.set_item (x, y, "*")

def move_options (elfx, elfy):

    OPTS = [ [1, 0], [0, 1], [0, -1], [-1, 0], [0, 0]]
    res = []
    
    for dx, dy in OPTS:
        if map.get_item (elfx + dx, elfy + dy) == OPEN:
            res.append ([elfx + dx, elfy + dy])
    
    return res


def find_path (starttime, start, exit_point):

    queue = deque([(starttime, start[0], start [1])])

    while True:
        time, ex, ey = queue.popleft ()
        time += 1
        qc = len (queue)
        print (f"Current time is {time}, queue is {qc}   ", end = "\r")
        
        bliz_map (time)
        next_steps = move_options (ex, ey)
        for nx, ny in next_steps:

            if [nx, ny] == exit_point:
                print (f"Reached exit in {time - starttime} minutes {' '*30}")
                return time - starttime

            key = (time, nx, ny)
            if key in seen:
                continue
           
            seen.add (key)
            queue.append (key)

# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()
    # lines = f.read()


map = AdventMap ()

blizz_start = []
blizz_type = []
seen = set ()
id = 0

for y, line in enumerate (lines):
    for x, item in enumerate (line.strip()):
        if item in BLIZZARD:
            blizz_start.append ( [x, y] )
            blizz_type.append ( item )
            id += 1
        else:
            map.set_item (x, y, item)

mod_x = map.maxx - map.minx - 1
mod_y = map.maxy - map.miny - 1
loop_idx = (map.maxx - map.minx - 1) * (map.maxy - map.miny - 1) // math.gcd(map.maxx - map.minx - 1, map.maxy - map.miny - 1)

start_point = [1, 0]
exit_point = [map.maxx-1, map.maxy]

t1 = find_path (0, start_point, exit_point)
print (t1)
t2 = find_path (t1, exit_point, start_point)
print (t2)
t3 = find_path (t2 + t1, start_point, exit_point)
print (t3)

print (f"Total run: {t1+t2+t3}")

# print (f"\nreached {exit_point} at {time}")