import re

TXTFILE = "day14.txt"

EMPTY = " "
STONE = "#"
SAND = "o"

# x: 489 - 562
# y: 17 - 161
minx = 400
maxx = 600
maxy = 200

# minx = 490
# maxx = 505
# maxy = 10


l = [EMPTY for _ in range(maxx)]
cave = [l.copy() for _ in range(maxy)]

def get_item (x,y):
    return cave[y][x]

def set_item (x,y,v):
    # print (f"{x}:{y} = {v}")
    cave [y][x] = v

def draw_line (px, py, x, y):

    if px == x:    #Y line
        step = (y - py) // abs (y - py)
        for yy in range (py, y + step, step):
            set_item (x, yy, STONE)
    elif py == y:    #X line
        step = (x - px) // abs (x - px)
        for xx in range (px, x + step, step):
            set_item (xx, y, STONE)
    else:
        0/0

def print_cave():
    for y in range (maxy):
        print(f"{y:3}", end="")
        for x in range (minx, maxx):
            print (get_item(x,y), end="")
        print()

def can_move(x, y):
    if y >= maxy:
        return True
    i = get_item (x, y)
    return True if i == EMPTY else False

def drop_sand():

    x = 500
    y = 0
    while True:
        if can_move (x, y+1):
            y += 1
            if y >= maxy:
                return False
            continue
        elif can_move (x-1, y+1):
            y += 1
            x -= 1
            continue
        elif can_move (x+1, y+1):
            y += 1
            x += 1
            continue
        else:
            set_item (x,y,SAND)
            return True



with open(TXTFILE, "r") as f:
    for line in f:
        coords = re.split (" -> ", line)
        px = py = None
        for c in coords:
            x = int(c.split(",")[0])
            y = int(c.split(",")[1])
            if not px:
                px = x
                py = y
                continue
            else:
                # set_item (x, y, STONE)
                # print (f"{px}-{py}:{x}-{y}",end=",")
                draw_line (px, py, x, y)
                px = x
                py = y
        print()

#print (f"{minx}-{maxx}:{miny}-{maxy}")
count = 0
while drop_sand():
    # print_cave()
    count += 1

print (count)

