pos = 0
regX = 1

def tick ():
    global pos

    print ("#" if pos in range(regX-1,regX+2) else " ", end="")
    pos = (pos + 1) % 40
    if pos == 0:
        print()

with open("day10.txt", "r") as f:
    for line in f:
        cmd = line.strip().split()
        if cmd[0] == "noop":
            tick()
        elif cmd[0] == "addx":
            tick ()
            tick ()
            regX += int (cmd[1])

