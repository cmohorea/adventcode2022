monkeys = {}

class Monkey ():

    def __init__ (self, f, me):
        
        self.inspections = 0
        self.me = me

        # read items
        line = f.readline().strip().replace(",","").split()[2:]
        self.items = []
        for i in line:
            self.add_item (int(i))
        
        # read operation
        line = f.readline().strip().split()
        self.oper = line [-3] + line[-2] + line[-1]

        # read test
        line = f.readline().strip().split()
        self.test = int(line [3])

        # read "if true"
        line = f.readline().strip().split()
        self.give_true = line [5]

        # read "if false"
        line = f.readline().strip().split()
        self.give_false = line [5]

        #read empty line
        f.readline()

    def add_item (self, item):
        # print (f"Monkey {self.me} added {item}")
        self.items.append (item)

    def inspect_my_items (self):
        
        global monkeys
        for item in self.items:
            self.inspections += 1
            oper = self.oper.replace ("old",str(item))
            wl = eval (oper)
            # print (f"wl: old {item} new {wl}")

            wl //= 3
            if wl % self.test == 0:
                # divisible 
                monkeys [self.give_true].add_item(wl)
            else:
                monkeys [self.give_false].add_item(wl)

            self.items = []


with open("day11.txt1", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().split()
        if line and (line [0] == "Monkey"):
            me = line[1][:-1]
            monkeys[me] = Monkey (f, me)

for i in range (20):
    print (f"Turn {i}")
    for m in monkeys:
        # print (f"Monkey {m} turn:")
        monkeys[m].inspect_my_items()
    for m in monkeys:
    #     print (f"Monkey {m} has {monkeys[m].items}")
        print ([monkeys[m].inspections for m in monkeys])

# for m in monkeys:
#     print (f"Monkey {m} inspections: {monkeys[m].inspections}")

z = [monkeys[m].inspections for m in monkeys]
z.sort()
print (z[-1]*z[-2])