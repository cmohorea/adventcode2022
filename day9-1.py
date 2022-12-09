TXTFILE = "day9.txt"

head = {"x":0,"y":0}
tail = {"x":0,"y":0}
visited = {}

def move_head (dx, dy):
    head["x"] += dx
    head["y"] += dy
    print (f'head moved to {head["x"]}:{head["y"]}')

def move_tail (dx, dy):
    
    if abs (head["x"] - tail["x"]) < 2:
        dx = 0
    else:
        tail["y"] = head["y"]

    if abs (head["y"] - tail["y"]) < 2:
        dy = 0
    else:
        tail["x"] = head["x"]

    tail["x"] += dx
    tail["y"] += dy
    print (f'and tail moved to {tail["x"]}:{tail["y"]}')
    visited [f'{tail["x"]}:{tail["y"]}'] = True

def make_move (dir, num):
    MX = {"L":-1, "R":1}
    MY = {"U":-1, "D":1}

    dx = MX.get(dir,0)
    dy = MY.get(dir,0)

    for i in range (int(num)):
        move_head (dx, dy)
        move_tail (dx, dy)

with open(TXTFILE, "r") as f:
    for line in f:
        [dir,num] = line.strip().split()
        print (f"{dir}:{num}")
        make_move (dir, num)

print (visited)
print (len(visited))
