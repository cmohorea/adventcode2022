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

ddx = [1,0,-1,0]
ddy = [0,1,0,-1]

def turn_right (dir):
    return (dir+1)%4

def turn_left (dir):
    return (dir-1)%4

def show_on_map (x,y,dir):
    map.set_item (x,y,DIRS[dir])

def find_wrap_coord (x,y,dx,dy):

    while True:
        w = map.get_item (x+dx, y+dy)
        if w in EMPTY:
            return [x, y]
        x += dx
        y += dy

def get_next_coord (x,y,dx,dy):
    
    next = map.get_item (x+dx, y+dy)
    if next == WALL:
        pass
    elif next in OPEN:
        x += dx
        y += dy
    elif next in EMPTY:
        nx, ny = find_wrap_coord (x, y, -dx, -dy)
        next = map.get_item (nx, ny)
        if next == WALL:
            pass
        elif next in OPEN:
            x = nx
            y = ny
        else:
            0/0
    else:
        0/0

    return [x, y]

def make_move (x, y, dir, steps):

    dx = ddx [dir]
    dy = ddy [dir]
    
    for _ in range(steps):
        x, y = get_next_coord (x,y,dx,dy)
        show_on_map (x, y, dir)
    
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

    my_x, my_y = make_move (my_x, my_y, my_dir, steps)
    print (f"Moved to {my_x}:{my_y} after {turn}{steps}")
    # map.set_item (my_x, my_y, "*")
    # map.print_map()

map.set_item (my_x, my_y, "$")
map.print_map()


print (my_x, my_y , my_dir)
passw = my_y * 1000 + my_x * 4 + my_dir
print (passw)

