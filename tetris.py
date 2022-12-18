import map

TETRIS = "@"
DROPPED = "#"

class Tetris ():

    def __init__ (self, global_map, x, y, elements):
        self.map = global_map
        self.move_to (x, y)
        self.sizex = len (elements[0])
        self.sizey = len (elements)

        self.elements = []
        for yy, line in enumerate (reversed(elements)):
            for xx, char in enumerate (line):
                if char != map.EMPTY:
                    self.elements.append([xx, yy - self.sizey + 1])
        self.element = elements

    def __del__ (self):
        self.show_on_map(DROPPED)

    def show_on_map (self, char = TETRIS):
        for coord in self.elements:
            self.map.set_item (self.x + coord [0], self.y + coord [1], char)

    def hide_on_map (self):
        self.show_on_map(map.EMPTY)

    def can_move_to (self, x, y):
        can_move = True
        for coord in self.elements:
            cont = self.map.get_item (x + coord [0], y+coord [1])
            if cont not in [TETRIS, map.EMPTY, map.UNDEFINED]:
                can_move = False
                break

        return can_move

    def can_move_down (self):
        return self.can_move_to (self.x, self.y - 1)

    def can_move_left (self):
        return self.can_move_to (self.x - 1, self.y)

    def can_move_right (self):
        return self.can_move_to (self.x + 1, self.y)

    def move_to (self, x, y):
        self.x = x
        self.y = y

    def move_by (self, x, y):
        self.hide_on_map()
        self.x += x
        self.y += y
        self.show_on_map()

    def move_down (self):
        self.move_by (0, -1)

    def move_left (self):
        self.move_by (-1, 0)

    def move_right (self):
        self.move_by (1, 0)



if __name__ == '__main__':
    
    m = map.AdventMap ()
    m.draw_line (0, 0, 10, 0)
    m.draw_line (0, 0, 0, 15)
    m.draw_line (10, 0, 10, 15)

    a = Tetris (m, 1, 10, [" # ","###"," # "])
    a.show_on_map ()
    m.print_map ()
    while a.can_move_right():
        a.move_right()
        m.print_map ()

    a.move_down()
    while a.can_move_left():
        a.move_left()
        m.print_map ()

    while a.can_move_down():
        a.move_down()
        m.print_map ()


    exit(0)