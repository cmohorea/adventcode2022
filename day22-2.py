import map22, re

TXTFILE = "day22.txt"

EMPTY = " "
OPEN = ".<>v^*"
WALL = "#"


DIRS = {
    0: ">", 
    1: "v", 
    2: "<", 
    3: "^",
}

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

ddx = [1,0,-1,0]
ddy = [0,1,0,-1]

def turn_right (dir):
    return (dir+1)%4

def turn_left (dir):
    return (dir-1)%4

def show_on_map (x,y):
    map.set_item (x,y,DIRS[my_dir])

def find_wrap_coord (x,y,dx,dy):

    ndir = dir

    if x == 1 and dx == -1:
        if 100 < y <=150:   # 5l
            x = 51
            y = 150 - y + 1
            ndir = RIGHT
        elif 150 < y <=200: # 6l
            x = y - 100
            y = 1
            ndir = DOWN
        else:
            0/0
    elif x == 51 and dx == -1:
        if 0 < y <=50:      # 1l
            x = 1
            y = 150 - y + 1
            ndir = RIGHT
        elif 50 < y <=100: # 3l
            x = y - 50
            y = 101
            ndir = DOWN
        else:
            0/0
    elif x == 50 and dx == 1:
        if 150 < y <=200:   # 6r
            x = y - 100
            y = 150
            ndir = UP
        else:
            0/0
    elif x == 100 and dx == 1:
        if 50 < y <=100:      # 3r
            x = y + 50
            y = 50
            ndir = UP
        elif 100 < y <=150: # 4r
            x = 150
            y = 150-y+1
            ndir = LEFT
        else:
            0/0
    elif x == 150 and dx == 1:
        if 0 < y <=50:      # 2r
            x = 100
            y = 150-y+1
            ndir = LEFT
        else:
            0/0
# U/D
    elif y == 1 and dy == -1:
        if 50 < x <=100:      # 1u
            y = x + 100
            x = 1
            ndir = RIGHT
        elif 100 < x <=150:     # 2u
            x = x - 100
            y = 200
            ndir = UP
        else:
            0/0
    elif y == 101 and dy == -1:
        if 0 < x <=50:      # 5u
            y = x + 50
            x = 51
            ndir = RIGHT
        else:
            0/0
    elif y == 50 and dy == 1:
        if 100 < x <=150:      # 2d
            y = x - 50
            x = 100
            ndir = LEFT
        else:
            0/0
    elif y == 150 and dy == 1:
        if 50 < x <=100:      # 4d
            y = x + 100
            x = 50
            ndir = LEFT
        else:
            0/0
    elif y == 200 and dy == 1:
        if 0 < x <=50:      # 6d
            x = x + 100
            y = 1
            ndir = DOWN
        else:
            0/0
    else:
        0/0

    return [x, y, ndir]

def get_next_coord (x,y,dx,dy):
    
    global my_dir

    next = map.get_item (x+dx, y+dy)
    if next == WALL:
        pass
    elif next in OPEN:
        x += dx
        y += dy
    elif next in EMPTY:
        nx, ny, ndir = find_wrap_coord (x, y, dx, dy)
        next = map.get_item (nx, ny)
        if next == WALL:
            pass
        elif next in OPEN:
            x = nx
            y = ny
            my_dir = ndir
        else:
            0/0
    else:
        0/0

    return [x, y]

def make_move (x, y, steps):

    global my_dir
    
    for _ in range(steps):
        dx = ddx [my_dir]
        dy = ddy [my_dir]
        x, y = get_next_coord (x,y,dx,dy)
        show_on_map (x, y)
    
    return [x, y]

# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    # lines = f.readlines()
    lines = f.read()


mymap, prog = lines.split("\n\n")
mymap = mymap.split ("\n")
prog = "R"+prog.strip()

map = map22.AdventMap ()

for y, line in enumerate (mymap):
    for x, item in enumerate (line):
        map.set_item (x+1,y+1,item)

for i in range(len(mymap[0])):
    if mymap[0][i] not in EMPTY:
        start_pos = i+1
        break
 
my_dir = 3 #up
my_x = start_pos
my_y = 1

# prog = "R2R100R50L250"
while True:
    x = re.findall("([R,L])(\d*)(.*)", prog)
    if not x:
        break
    turn = x[0][0]
    steps = int(x[0][1])
    prog = x[0][2]
    
    if turn == "R":
        my_dir = turn_right (my_dir)
    elif turn == "L":
        my_dir = turn_left (my_dir)
    else:
        0/0

    my_x, my_y = make_move (my_x, my_y, steps)
    print (f"Moved to {my_x}:{my_y} after {turn}{steps}")
    # map.set_item (my_x, my_y, "*")
    # map.print_map()

map.set_item (my_x, my_y, "$")
map.print_map()


print (my_x, my_y , my_dir)
passw = my_y * 1000 + my_x * 4 + my_dir
print (passw)
