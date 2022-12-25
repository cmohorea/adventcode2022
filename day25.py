TXTFILE = "day25.txt"

def decode (str):
    s2d = {"2":2, "1":1, "0":0, "-":-1, "=":-2 }

    res = 0
    for c in str:
        res = res * 5 + s2d[c]

    return res

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def encode (num):
    d2s = {2:"2", 1:"1", 0:"0", -1:"-", -2:"=" }

    res = ""
    base5 = [0] + numberToBase(num, 5)
    for idx in range (len (base5)-1, 0, -1):
        nd = base5[idx]
        if 0 <= nd <= 2:
            res = res + d2s[nd]
        elif 3 <= nd <= 5:
            res = res + d2s [nd - 5]
            base5[idx-1] += 1
        else:
            0/0

    return res[::-1]

# ------------------------------------------------------
total = 0

with open(TXTFILE, "r") as f:
    for line in f:
        dec = decode(line.strip())
        total += dec
        # print (f"{line.strip()} == {dec}")


print (f"Total is {total}, or {encode(total)}")
