TXTFILE = "day6.txt"

def are_uni (s):
    for i in range (len (s)-1):
        if s.count(s[i]) > 1:
            return False
    
    return True

with open(TXTFILE, "r") as f:
    for line in f:
        e = line.strip()
        for r in range(len(e)-3):
            uni = are_uni (e[r:r+14])
            if uni:
                print(f"{r+14}:{e[r:r+4]}: {uni}")
                break
