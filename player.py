class Player:

    def __init__(self):
        self.pos_x = 1
        self.pos_y = 10
        self.velocity_x = 1
        self.velocity_y = 0

    def update_position(self):
        self.pos_x += self.velocity_x
        self.pos_y += self.velocity_y
        self.wrap()

    def move_up(self):
        if self.velocity_y == 0:
            self.velocity_y = -1
            self.velocity_x = 0

    def move_down(self):
        if self.velocity_y == 0:
            self.velocity_y = 1
            self.velocity_x = 0

    def move_left(self):
        if self.velocity_x == 0:
            self.velocity_y = 0
            self.velocity_x = -1

    def move_right(self):
        if self.velocity_x == 0:
            self.velocity_y = 0
            self.velocity_x = 1

    def wrap(self):
        if self.pos_x == -1:
            self.pos_x = 19
        if self.pos_x == 20:
            self.pos_x = 0
        if self.pos_y == -1:
            self.pos_y = 19
        if self.pos_y == 20:
            self.pos_y = 0
