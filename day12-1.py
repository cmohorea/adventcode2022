TXTFILE = "day12.txt"
INF = 999999

map = []
path = {}

def get_item (x,y):
    if x < 0 or y < 0:
        return None
    try:
        return map[y][x]
    except:
        return None

def set_path_cost (x,y,v):
    path [f"{x}:{y}"] = v

def get_path_cost (x,y):
    return path.get(f"{x}:{y}", INF)

def get_cost_to (x1, y1, x2, y2):

    a = get_item (x1, y1)
    b = get_item (x2, y2)

    # if (a and b) and (abs (ord(a) - ord (b)) <= 1):
    if (a and b) and (ord(b) - ord(a) <= 1):
        return 1
    else:
        return INF

def calc_paths(x,y):  

    def calc_path_to_me (x,y, x1, y1):     #x1,y1 to me (x,y)

        my_cost = get_path_cost (x, y)
        his_cost = get_path_cost (x1, y1)
        step_cost = get_cost_to (x1, y1, x, y)

        if my_cost + step_cost < his_cost:
            set_path_cost (x1, y1, my_cost + step_cost)
            to_be_updated.append ([x1,y1])

    to_be_updated = []

    calc_path_to_me (x, y, x + 1, y)
    calc_path_to_me (x, y, x - 1, y)
    calc_path_to_me (x, y, x, y + 1)
    calc_path_to_me (x, y, x, y - 1)

    for i in to_be_updated:
        calc_paths (i[0],i[1])

mr = 0
with open(TXTFILE, "r") as f:
    for line in f:
        ml = list(line.strip())
        for mc in range(len(ml)):
            if ml[mc] == "S":
                start = [mc,mr]
                ml[mc] = "a"
            elif ml[mc] == "E":
                end = [mc,mr]
                ml[mc] = "z"
                set_path_cost (mc, mr, 0)
        map.append (ml)
        mr += 1

calc_paths (end[0],end[1])
print (get_path_cost(start[0],start[1]))
