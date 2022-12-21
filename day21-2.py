import re
from copy import deepcopy

TXTFILE = "day21.txt"

ops = {}
values = {}

def optimize (name):
    global ops

    try:
        if name == "humn":
            return ( [values[name], False] )
        else:
            return ( [values[name], True] )
    except:
        x,op,y = ops[name]
        xx, ca1 = optimize (x)
        yy, ca2 = optimize (y)
        result = int (eval (f"{xx}{op}{yy}"))
        cacheable = ca1 and ca2
        if cacheable:
            values.pop (x)
            values.pop (y)
            ops.pop (name)
            values[name] = result
            return [result, True]
        else:
            return [result, False]

def get_value (name):
    result = values.get(name)
    if result!=None:
        return result
    else:
        x,op,y = ops[name]
        xx = get_value (x)
        yy = get_value (y)
        res = int (eval (f"{xx}{op}{yy}"))
        print (f"{name} evaluated to {res} from {x}[{xx}] {op} {y}[{yy}]")
        return res

def parse_child (name):
    x,op,y = ops[name]
    if values.get(x) == None:
        num = values.get(y)
        name = x
        norm = True
    else:
        num = values.get(x)
        name = y
        norm = False
    return [name, op, num, norm]

def eval_back (name, value):
    reverse_op = {"+":"-", "-":"+", "*":"//", "//":"*"}

    print (f"{name} value: {value}")
    mych1, myop, mych2 = ops.get(name)
    if (mych1 == "humn") or (mych2 == "humn"):
        op = reverse_op [myop]
        if (mych1 == "humn"):
            val = int(eval (f"{value} {op} {values[mych2]}"))
        else:
            val = int(eval (f"{value} {op} {values[mych1]}"))
        print (f"Human is: {val}")
        return
    
    child1, my_op, child2_val, dir = parse_child (name)
    if dir or my_op in ["+","*"]: # "Left place"
        rop = reverse_op [my_op]
        child1val = int(eval (f"{value} {rop} {child2_val}"))
    elif my_op in ["//","-"]:
        child1val = int(eval (f"{child2_val} {my_op} {value}"))

    eval_back (child1,child1val)
    
# ------------------------------------------------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()

for line in lines:
    li = line.strip().split(":")
    name = li[0].strip()
    value = li[1].strip()

    try:
        values[name] = int(value)
    except:
        ops[name] = value.split()
        if ops[name][1] == "/":
            ops[name][1] = "//"
         

optimize("root")
x = parse_child("root")
eval_back (x[0], x[2])
