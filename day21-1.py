import re
from copy import deepcopy

TXTFILE = "day21.txt"

data = {}

def get_value (name):

    item = data[name]
    try:
        return (int(item))
    except:
        x,op,y = item.split()
        xx = get_value (x)
        yy = get_value (y)
        return int (eval (f"{xx}{op}{yy}"))

# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()

for line in lines:
    li = line.strip().split(":")
    data[li[0].strip()] = li[1].strip()

# data["humn"]="9879574614298"
print (get_value("root"))
