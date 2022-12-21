import functools

TXTFILE = "day13.txt"

OK = -1
FAIL = 1
CONT = 0

def compare_lists (l1, l2):

    for i in range(len(l1)):
        v1 = l1[i]
        if i > len (l2) - 1:    # print ("-- Right side ran out of items")
            return FAIL
        v2 = l2[i]

        if isinstance(v1,int) and isinstance(v2, int):
            if v1 > v2:     # print ("-- Right side is smaller")
                return FAIL
            elif v1 < v2:   # print ("++ Left side is smaller")
                return OK
            else:
                continue

        if isinstance(v1, int):
            v1 = [v1]
        if isinstance(v2, int):
            v2 = [v2]

        res = compare_lists (v1, v2)
        if res == CONT:
            continue
        return res
    
    if len (l1) < len (l2): # print ("++ Left side ran out of items")
        return OK
    else:
        return CONT

targets = [ [[2]], [[6]] ]
packets = targets.copy()

with open(TXTFILE, "r") as f:
    for line in f:
        if line == "\n":
            continue
        packets.append(eval(line))

spackets = sorted (packets, key=functools.cmp_to_key(compare_lists))

mult = 1
for i in range(len(spackets)):
    if spackets[i] in targets:
        mult *= i+1

print (mult)
