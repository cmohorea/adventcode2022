import re, pprint
import rustworkx as rx


TXTFILE = "day16.txt"

with open(TXTFILE, "r") as f:
    lines = f.readlines()

all_valves = {}
in_scope = []
global_max = 0

def dummy (param):
    return 1

def valve_id_by_name (name):
    for i in all_valves:
        if all_valves[i]["name"] == name:
            return i
    return -1

def path_len (a, b):
    return 0 if a == b else len(all_paths[a][b])-1

def steam_per_tick (valves, ticks):
    steam = 0
    for id in valves:
        steam += all_valves[id]["fps"]
    return steam * ticks

def iterate_paths (current, visited, to_go, timer = 0, steam = 0):
    
    global global_max

    if timer > 30:
        print (f"----------- Over 30! ------------------- {steam}")
        return False

    # if current not in visited:
    #     visited.append (current)

    if (len (to_go) == 0) or (timer == 30):
        rest_steam = steam_per_tick (visited, 30 - timer)
        steam += rest_steam
        print (f"Reached {current} via {visited} in {timer}, steam = {steam}")
        if steam > global_max:
            global_max = steam
        # exit(0)
        return True

    for p in to_go:
        rest = to_go.copy()
        rest.remove (p)
        visi = visited.copy()
        
        ticks = path_len(current, p) + 1
        if timer + ticks > 30:
            st = steam_per_tick (visi, 30 - timer)
            print (f"At {current}. Visited: {visi}, to visit: {rest} [{ticks-1}/{timer}]. Steam: {st}")
            iterate_paths (p, visi, rest, 30, steam + st)
        else:
            visi.append (current)
            st = steam_per_tick (visi, ticks)
            print (f"At {current}. Visited: {visi}, to visit: {rest} [{ticks}/{timer}]. Steam: {st}/{steam + st}")
            iterate_paths (p, visi, rest, timer + ticks, steam + st)

G = rx.PyDiGraph()
for line in lines:
    line = re.sub("Valve ","", line)
    line = re.sub("has flow rate=","", line)
    line = re.sub("; tunnel(s)? lead(s)? to valve(s)?|,","", line)
    v = line.split()
    
    id = G.add_node(v[0])
    all_valves[id] = {}
    all_valves[id]["name"] = v[0]
    all_valves[id]["fps"] = int(v[1])
    all_valves[id]["open"] = v[1] == "0"
    all_valves[id]["peer_names"] = v[2:]
    if not all_valves[id]["open"]:
        in_scope.append(id)

for v in all_valves:
    all_valves[v]["peers"] = [ valve_id_by_name (name) for name in all_valves[v]["peer_names"] ]
    for p in all_valves[v]["peers"]:
        G.add_edge(v, p, 1)

# pprint.pprint (valve, indent = 4)

# iterate_paths ([], in_scope)
# print (count)

node_indices = G.node_indices()
edge_indices = G.edge_indices()
# print(node_indices)
# print(edge_indices)
# all_paths = rx.dijkstra_shortest_path_lengths (G, 0, dummy)
all_paths = dict(rx.all_pairs_dijkstra_shortest_paths (G, dummy))
full_steam = steam_per_tick (in_scope, 1)
# for node, path  in all_paths.items():
#     print (node, path)
#     print ("-"*40)

# for node, path  in all_paths.items():
#      print (path_len(0, node))

# print (in_scope)
# [3, 4, 6, 9, 12, 15, 18, 29, 31, 35, 44, 45, 46, 57, 61]
# in_scope = [3,1,9,7,4,2]
in_scope = [57, 6, 15, 3, 12, 18, 9, 35, 45]
iterate_paths (0, [], in_scope)
print (f"Max steam = {global_max}")