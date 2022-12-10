TXTFILE = "day10.txt"

strength = 0
qtime = 20

time = 0
regX = 1

def tick ():
    global time, qtime, strength

    time += 1
    if time == qtime:
        strength += time * regX
        print (f"Time: {time:}, X = {regX}, strength = {strength}")
        qtime += 40


with open(TXTFILE, "r") as f:
    for line in f:
        cmd = line.strip().split()
        if cmd[0] == "noop":
            tick()
        elif cmd[0] == "addx":
            tick ()
            tick ()
            regX += int (cmd[1])

print (strength)
