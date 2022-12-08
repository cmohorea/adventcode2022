import re

TXTFILE = "day7.txt"

total_size = 0

def read_dir (f, path):

    global total_size

    size = 0
    while True:
        line = f.readline().strip()
        if not line:
                print (f"{path}: {size}")
                if size <= 100000:
                    total_size += size
                return size
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    print (f"{path}: {size}")
                    if size <= 100000:
                        total_size += size
                    return size
                else:
                    # print (f"command: cd {path + line[2]}")
                    size += read_dir (f, path + line[2] + "/")
            elif line[1] == "ls":
                pass
            else:
                raise Exception(f"Unexpected command {line[1]}!")

        elif line[0] == "dir":
            pass
        elif re.search ("^[0-9]*$", line[0]):
            # print (f"file {line[1]} size is {line[0]}")
            size += int (line[0])
        else:
            raise Exception("Unexpected line!")


with open(TXTFILE, "r") as f:
    read_dir (f,"")

print (total_size)
