TXTFILE = "day9.txt"

# head = {"x":0,"y":0}
# tail = {"x":0,"y":0}
visited = {}
qty = 10
knots = [{"x":0,"y":0} for _ in range(qty)]

def move_head (head, dx, dy):
    head["x"] += dx
    head["y"] += dy
    print (f'head moved to {head["x"]}:{head["y"]}')

def move_tail (head, tail):
    
    dx = head["x"] - tail["x"]
    dy = head["y"] - tail["y"]
    if (abs(dx) > 1) or (abs(dy) > 1):
        dx = dx // abs (dx) if dx != 0 else 0
        dy = dy // abs (dy) if dy != 0 else 0
    else:
        dx = 0
        dy = 0

    tail["x"] += dx
    tail["y"] += dy
    print (f'and tail moved to {tail["x"]}:{tail["y"]}')

def make_move (dir, num):
    MX = {"L":-1, "R":1}
    MY = {"U":-1, "D":1}

    dx = MX.get(dir,0)
    dy = MY.get(dir,0)

    for i in range (int(num)):
        move_head (knots[0], dx, dy)
        for j in range (qty-1):
            move_tail (knots[j], knots[j+1])
    
        visited [f'{knots[qty-1]["x"]}:{knots[qty-1]["y"]}'] = True

with open(TXTFILE, "r") as f:
    for line in f:
        [dir,num] = line.strip().split()
        print (f"{dir}:{num}")
        make_move (dir, num)

print (len(visited))
