import re

TXTFILE = "day7.txt"
total_size = 0

def read_dir (f, path):
    global total_size

    size = 0
    while True:
        line = f.readline().strip()
        if not line:
            line = "$ cd .."
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    print (f"{path}: {size}")
                    if size <= 100000:
                        total_size += size
                    return size
                else:
                    size += read_dir (f, path + line[2] + "/")

        elif re.search ("^[0-9]*$", line[0]):
            size += int (line[0])

with open(TXTFILE, "r") as f:
    read_dir (f,"")

print (total_size)
