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
            print ("-- Right side ran out of items")
            return FAIL
        v2 = l2[i]

        if (type(v1) == int) and type(v2) == int:
            if v1 > v2:
                print ("-- Right side is smaller")
                return FAIL
            elif v1 < v2:
                print ("++ Left side is smaller")
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
        print ("++ Left side ran out of items")
        return OK
    else:
        return CONT

with open(TXTFILE, "r") as f:
    while True:
        line1 = f.readline()
        if not line1:
            break
        if line1 == "\n":
            continue

        line1 = eval(line1)
        line2 = eval(f.readline())
        
        res = compare_lists(line1, line2)
        if res == OK:
            idxs += idx
            print (f"line {idx:} {line1} / {line2}: {res}")
        elif res == CONT:
            print (f"line {idx:} {line1} / {line2}: {res}")
            0/0
        idx += 1
        


print (f"the sum of the indices is {idxs}")

