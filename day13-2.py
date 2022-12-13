import pprint

TXTFILE = "day13.txt"

OK = 0
FAIL = 1
CONT = 2

idx = 1
idxs = 0

def get_first (x):
    return [x[0]] if len (x) > 0 else []

def compare_lists (l1, l2):

    for i in range(len(l1)):
        v1 = l1[i]
        if i > len (l2) - 1:
            # print ("-- Right side ran out of items")
            return FAIL
        v2 = l2[i]

        if (type(v1) == int) and type(v2) == int:
            if v1 > v2:
                # print ("-- Right side is smaller")
                return FAIL
            elif v1 < v2:
                # print ("++ Left side is smaller")
                return OK
            else:
                continue

        if type(v1) == int:
            v1 = [v1]

        if type(v2) == int:
            v2 = [v2]

        res = compare_lists (v1, v2)
        if res == CONT:
            continue

        return res

    
    if len (l1) < len (l2):
        # print ("++ Left side ran out of items")
        return OK
    else:
        return CONT


el1 = [[2]]
el2 = [[6]]
packets = [el1, el2]

with open(TXTFILE, "r") as f:
    for line in f:
        if line == "\n":
            continue
        packets.append(eval(line))


for i in range(len(packets)):
    for j in range(len(packets)-1):
        if compare_lists (packets[j],packets[j+1]) == FAIL:
            packets [j], packets [j+1] = packets [j+1], packets [j]

mult = 1
for i in range(len(packets)):
    if packets[i] in [el1, el2]:
        mult *= i+1
    # print (packets[i])

print (mult)
