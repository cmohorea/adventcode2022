TXTFILE = "day5.txt"

crates = [
    list ("RPCDBG"),
    list ("HVG"),
    list ("NSQDJPM"),
    list ("PSLGDCNM"),
    list ("JBNCPFLS"),
    list ("QBDZVGTS"),
    list ("BZMHFTQ"),
    list ("CMDBF"),
    list ("FCQG")
]

def move (i1,i2):
    q = crates[i1].pop()
    crates[i2].append(q)

def moveall (i1,i2,qty):
    crates[i2].extend(crates[i1][-qty:])
    crates[i1] = crates[i1][:-qty]


total = 0
with open(TXTFILE, "r") as f:
    for line in f:
        e = line.strip().split()
        cnt = int(e[1])
        fr = int(e[3])-1
        to = int(e[5])-1
        # for i in range(cnt):
        #     move (fr,to)

        moveall (fr,to, cnt)

        # print (f"{cnt}/{fr}/{to}")

# moveall (1,2,3)
# print (crates)

# moveall (2,3,3)
# print (crates)

# moveall (3,4,3)
# print (crates)

s=""
for i in crates:
    s+=i[-1]

print (s)

