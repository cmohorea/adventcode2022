import re
from map import AdventMap, UNDEFINED, INFINITY

TXTFILE = "day15.txt"
DIMENSION = 4000000
# TXTFILE = "day15.txt1"
# DIMENSION = 20

EMPTY = " "
SENSOR = "S"
BEAKON = "B"
RANGE = "#"

map = AdventMap ()
tpl = re.compile ("[\-\d]+")

def boundaries (sx, sy, bx, by):

    changed = False
    dist = abs (bx-sx) + abs (by-sy)
    for y in range (- dist, dist + 1):
        ry = sy + y
        if ( ry>= 0) and (ry <= DIMENSION): # only interesting line

            xw = dist - abs(y)
            mi = sx - xw 
            ma = sx + xw + 1

            if (minlist[ry] < ma) and (minlist[ry] >= mi):
                minlist[ry] = ma
                changed = True
            if (maxlist[ry] > mi) and (maxlist[ry] <= ma):
                maxlist[ry] = mi
                changed = True

    return changed

minlist = {i:0  for i in range (DIMENSION+1)}
maxlist = {i:DIMENSION  for i in range (DIMENSION+1)}

with open(TXTFILE, "r") as f:
    lines = f.readlines()

iter = 1
while True:
    print (f"Iteration {iter}", end="\r")
    iter += 1
    changed = False 
    for line in lines:
        sx, sy, bx, by = tpl.findall(line)
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        if boundaries (sx,sy, bx, by):
            changed = True
        # for i, val in minlist.items():
        #     print (f"{i}: {val} {maxlist[i]}")
        # print ("-"*40)
    if not changed:
        break
        

for i, val in minlist.items():
    if maxlist[i] > i:
        print (f"{i}: {val} {maxlist[i]} = {val*4000000+i}")


