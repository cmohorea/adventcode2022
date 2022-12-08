TXTFILE = "day4.txt"

def con (e1,e2):
    a=int(e1[0])
    b=int(e1[1])
    x=int(e2[0])
    y=int(e2[1])

    if (a>=x) and (a<=y):
        return True
    if (b>=x) and (b<=y):
        return True
    if (x>=a) and (x<=b):
        return True
    if (y>=a) and (y<=b):
        return True
    else:
        return False


total = 0
with open(TXTFILE, "r") as f:
    for line in f:
        e = line.strip().split(",")
        e1 = e[0].split("-")
        e2 = e[1].split("-")
        if con(e1,e2):
            total += 1
        print (f"{e1}\t{e2}\t{total}")
