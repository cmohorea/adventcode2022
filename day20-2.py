import re
from copy import deepcopy

TXTFILE = "day20.txt"

# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()

items = []
for i, line in enumerate (lines):
    items.append ([i, int(line) * 811589153])
    if line == "0\n":
        zitem = [i, int(line) * 811589153]

allitems = items.copy()

print (allitems)

# def item_by_seq (seq):
#     for i in items:
#         if i[0] == seq:
#             return i
#     return 0/0


total = len (items)

for i in range (10):
    for item in allitems:
        # item = item_by_seq (iter[0])
        # if item[1] == 0:
        #     print ("")

        idx = items.index (item)

        item = items.pop(idx)
        if idx + item[1] > 0:
            newidx = (idx + item[1] ) % (total - 1)
        else:
            newidx = (idx + item[1] - 1 ) % (total - 1) + 1
        items.insert (newidx, item)


    print (i, " ->", [i[1] for i in items])

idx = items.index(zitem)
a = items[ (idx + 1000) % total][1]
b = items[ (idx + 2000) % total][1]
c = items[ (idx + 3000) % total][1]

print (a+b+c)



