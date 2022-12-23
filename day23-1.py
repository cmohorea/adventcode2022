import map22, re
from map22 import INFINITY

TXTFILE = "day23.txt"

EMPTY = " "
OPEN = "."
ELF = "#"
DOUBLEMOVE = "X"

DIRS = [ [0, -1], [0, 1], [-1, 0], [1, 0] ]     #NSWE
CHECK = [ 
    [ [-1, -1], [0, -1], [1, -1] ], 
    [ [-1,  1], [0,  1], [1,  1] ], 
    [ [-1, -1], [-1, 0], [-1, 1] ],
    [ [ 1, -1], [ 1, 0], [ 1, 1] ],
]

DIRS += DIRS
CHECK += CHECK

dir = 0
elves = {}

def move_to (map, id, newx, newy):
    global elves

    x = elves[id][0]
    y = elves[id][1]  
    c = map.get_item (x, y)
    if c != EMPTY:
        map.set_item (x,y,OPEN)
    elves [id] = [newx, newy]
    map.set_item (newx,newy,ELF)

def need_to_move (map, id):
    cnt = 0
    ex = elves[id][0]
    ey = elves[id][1]
    for x in range (ex-1, ex+2):
        for y in range (ey-1, ey+2):
            if map.get_item (x, y) == ELF:
                cnt += 1

    return cnt > 1

def next_step (id):
    ex = elves[id][0]
    ey = elves[id][1]
    
    for d in range (4):
        i1 = map.get_item(ex + CHECK[dir + d][0][0], ey + CHECK[dir + d][0][1])
        i2 = map.get_item(ex + CHECK[dir + d][1][0], ey + CHECK[dir + d][1][1])
        i3 = map.get_item(ex + CHECK[dir + d][2][0], ey + CHECK[dir + d][2][1])
        if i1 != ELF and i2 != ELF and i3 != ELF:
            ex += DIRS[dir + d][0]
            ey += DIRS[dir + d][1]
            break

    return [ ex, ey ]

def find_square (map):
    minx = INFINITY
    maxx = -INFINITY
    miny = INFINITY
    maxy = -INFINITY

    for y in range (map.miny, map.maxy + 1):
        for x in range (map.minx, map.maxx + 1):
            if map.get_item (x, y) == ELF:
                if x < minx:
                    minx = x
                if x > maxx:
                    maxx = x
                if y < miny:
                    miny = y
                if y > maxy:
                    maxy = y

    # map.set_item (minx, miny, "$")
    # map.set_item (minx, maxy, "$")
    # map.set_item (maxx, miny, "$")
    # map.set_item (maxx, maxy, "$")

    count = 0
    for y in range (miny, maxy + 1):
        for x in range (minx, maxx + 1):
            if map.get_item (x, y) in [OPEN, EMPTY]:
                count += 1

    print (count)



# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()
    # lines = f.read()


map = map22.AdventMap ()

id = 0
for y, line in enumerate (lines):
    for x, item in enumerate (line.strip()):
        if item == ELF:
            elves[id] = [x, y]
            id += 1
        map.set_item (x, y, OPEN)
        
for id, [x, y] in elves.items():
    move_to (map, id, x, y)

for _ in range (10):

    next_map = map22.AdventMap ()
    
    # evaluating phase
    moving = []
    next_move = {}
    for elf_id in elves.keys():
        if need_to_move (map, elf_id):
            moving.append (elf_id)
            newx, newy = next_step (elf_id)
            next_move [elf_id] = [newx, newy]
            mm = next_map.get_item (newx, newy)
            if mm in [ELF, DOUBLEMOVE]:
                next_map.set_item (newx, newy, DOUBLEMOVE)
            else:
                next_map.set_item (newx, newy, ELF)


    # moving phase
    for elf_id in moving:
        newx, newy = next_move [elf_id]
        if next_map.get_item (newx, newy) == ELF:
            move_to (map, elf_id, newx, newy)
        # else:
        #     print (f"not moving elf {elf_id}")

    # next_map.print_map()
    del (next_map)
    dir = (dir + 1) % 4


map.print_map()
find_square (map)
