import re
from copy import deepcopy

max_tick = 24
TXTFILE = "day19.txt"

ORE = 0
CLAY = 1
OBSI = 2
GEODE = 3
MATS = [ORE, CLAY, OBSI, GEODE]

MINE_INIT = {
    ORE: {
        "rate": 1,
        "qty": 0,
    },
    CLAY: {
        "rate": 0,
        "qty": 0,
    },
    OBSI: {
        "rate": 0,
        "qty": 0,
    },
    GEODE: {
        "rate": 0,
        "qty": 0,
    },
}

RE = {
    ORE: {},
    CLAY: {},
    OBSI: {},
    GEODE: {},
}

def mine(M, mins):
    for _ in range (mins):
        for mat in M:
            M[mat]["qty"] += M[mat]["rate"]
    return M

def build_robot (M, mat, ticks):
    # print (f"Built {mat} robot at {ticks}")
    M[mat]["rate"] += 1
    for i in RE[mat]["cost"]:
        M[i[0]]["qty"] -= i[1]
    
    return M


def round_up_div (numerator, denominator): 
    return -(-numerator // denominator)

def can_build (M, mat):
    ticks = 1
    for i in RE[mat]["cost"]:
        if (M[i[0]]["qty"] < i[1]):
            if(M[i[0]]["rate"] == 0):
                return 0
            else:
                t = round_up_div (i[1] - M[i[0]]["qty"], M[i[0]]["rate"])
                if t > ticks:
                    ticks = t
    return ticks

def gener (MM, list, ticks):
    global maximum
    if ticks == max_tick:
        if MM[GEODE]['qty'] > maximum:
            maximum = MM[GEODE]['qty']
            print (f"Got: {list} {MM[GEODE]['qty']} {maximum}")
        # res = simulate (list)
        # if res:
        #     print res
    else:
        for m in MATS:
            MMM = deepcopy(MM)
            t = can_build (MMM, m)
            if t == 0:
                return
            elif t > max_tick - ticks:    # no time to build it
                mine (MMM, max_tick - ticks)
                gener (MMM, list, max_tick)
            else:
                MMM = mine (MMM, t)
                MMM = build_robot (MMM, m, ticks + t)
                gener (MMM, list + [m], ticks + t)



# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()

for line in lines:
    x = re.findall ( "(\d+)", line)
    print (f"Blueprint {x[0]}")
    MiM = deepcopy (MINE_INIT)
    maximum = 0
    
    RE[ORE]["cost"] = [ [ORE, int(x[1])] ]
    RE[CLAY]["cost"] = [ [ORE, int(x[2])] ]
    RE[OBSI]["cost"] = [ [ORE, int(x[3])], [CLAY, int(x[4])] ]
    RE[GEODE]["cost"] = [ [ORE, int(x[5])], [OBSI, int(x[6])] ]
    gener (MiM, [], 0)
