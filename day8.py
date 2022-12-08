import re

TXTFILE = "day8.txt"

rows = []
total_size = 0

def isVisible (x,y):
    
    me = rows[y][x]
    visible = 4

    for i in range (x-1,-1,-1):
        if me <= rows[y][i]:
            visible -= 1
            break

    for i in range (x+1,xx):
        if me <= rows[y][i]:
            visible -= 1
            break

    for i in range (y-1,-1,-1):
        if me <= rows[i][x]:
            visible -= 1
            break

    for i in range (y+1,yy):
        if me <= rows[i][x]:
            visible -= 1
            break

    print (f"[{x}:{y}]={me}:{visible>0}")
    return visible > 0

def ScenicScore (x,y):
    
    x-=1
    y-=1
    me = rows[y][x]
    score = 1

    idx=x
    for i in range (x-1,-1,-1):
        if me <= rows[y][i]:
            idx=x-i
            break
    # print (idx)
    score *= idx

    idx=xx-x-1
    for i in range (x+1,xx):
        if me <= rows[y][i]:
            idx=i-x
            break
    # print (idx)
    score *= idx

    idx=y
    for i in range (y-1,-1,-1):
        if me <= rows[i][x]:
            idx=y-i
            break
    # print (idx)
    score *= idx

    idx = yy - y - 1
    for i in range (y+1,yy):
        if me <= rows[i][x]:
            idx=i-y
            break
    # print (idx)
    score *= idx

    # print (f"[{x}:{y}]={me}:{score}")
    # print ("-------")
    return score



with open(TXTFILE, "r") as f:
    for line in f:
        rows.append (list(line.strip()))

xx = len (rows[0])
yy = len (rows)

# cnt = 0
# for y in range(len(rows)):
#     print ()
#     for x in range (len(rows[y])):
#         if isVisible (x, y):
#             cnt += 1

# print (cnt)

best = 0
for y in range(len(rows)):
    print ()
    for x in range (1,len(rows[y])+1):
        s = ScenicScore(x,y)
        if s > best:
            best = s
        # print (ScenicScore(x,y))

print (best)
