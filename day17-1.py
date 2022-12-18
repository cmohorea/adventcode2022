import map
from tetris import Tetris

TXTFILE = "day17.txt"

CAVE_WIDTH = 7
pattern_offset = 0
figure_offset = 0

figures = [
    ["@@@@"],
    [" @ ","@@@"," @ "],
    ["  @","  @","@@@"],
    ["@ ","@","@","@"],
    ["@@","@@"],
]

# -------------------

def next_pattern():
    global pattern_offset
    res = pattern[pattern_offset]
    pattern_offset = (pattern_offset + 1) % len (pattern)
    return res

def next_figure():
    global figure_offset
    res = figures[figure_offset]
    figure_offset = (figure_offset + 1) % len (figures)
    return res

def drop_next_piece (cave, height):
    # return cave height
    fig = Tetris (cave, 0, 0, next_figure())
    newh = height + fig.sizey + 3
    fig.move_to (3, newh)
    fig.show_on_map ()
    cave.draw_line (0,height, 0, newh,"|")
    cave.draw_line (8,height, 8, newh,"|")
    # cave.print_map()

    while True:
        dir = next_pattern()
        # print (dir)

        if dir == "<":
            if fig.can_move_left():
                fig.move_left()
        elif dir == ">":
            if fig.can_move_right():
                fig.move_right()
        else:
            0/0

        if fig.can_move_down():
            fig.move_down()
        else:
            # cave.print_map()
            break
        
        # cave.print_map()
    
    newh = fig.y if fig.y > height else height
    del fig
    return newh

# -------------
with open(TXTFILE, "r") as f:
    lines = f.readlines()

pattern = lines [0].strip()


cave = map.AdventMap ()
cave.draw_line (0,0, CAVE_WIDTH+1,0,"=")

height = 0
for _ in range (2022):
    # print (_)
    height = drop_next_piece (cave, height)

    # cave.print_map()
    # print("-"*40)
print (height)
# cave.print_map()
