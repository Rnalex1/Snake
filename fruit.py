import random


class Fruit:

    def __init__(self):
        self.pos_x = random.randint(0, 19)
        self.pos_y = random.randint(0, 19)

    def eat(self):
        self.pos_x = random.randint(0, 19)
        self.pos_y = random.randint(0, 19)