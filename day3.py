TXTFILE = "day3.txt"

def cost (l):
    if l.islower():
        return ord(l)-96
    else:
        return ord(l)-38


tcost = 0
with open(TXTFILE, "r") as f:
    while True:
        l1 = f.readline().strip()
        l2 = f.readline().strip()
        l3 = f.readline().strip()
        if not l1:
            break
        v = None
        for l in l1:
            if (l in l2) and (l in l3):
                v = l

        tcost += cost (v)
        print (f"{l1} / {l2} / {l3} / {tcost}")

    # for line in f:
    #     line = line.strip()
    #     p1=line[:len(line)//2]
    #     p2=line[len(line)//2:]
    #     v = None
    #     for l in p1:
    #         if l in p2:
    #             v = l
    #     tcost += cost (v)
    #     print (f"{line}:\t{p1}\t{p2}\t{v}\t{tcost}")
