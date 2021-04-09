from tkinter import *

import fruit
import player
import time


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Snake")
        self.game = Game()
        self.mainloop()


class Game(Canvas):

    def __init__(self):
        super().__init__(width=500, height=500, bg="black")
        self.snake = [player.Player()]
        self.time_step = 0.1
        self.fruit = fruit.Fruit()
        self.has_key_been_pressed = False
        self.draw_player()
        self.draw_fruit()
        self.is_playing = False
        self.bind_all("<Key>", self.key_pressed)
        self.pack()

    def game_loop(self):
        while self.is_playing:
            self.has_key_been_pressed = False
            self.clear_screen()
            for segment in self.snake:
                segment.update_position()
            if self.snake[0].pos_x == self.fruit.pos_x and self.snake[0].pos_y == self.fruit.pos_y:
                self.fruit.eat()
                new_segment = player.Player()
                new_segment.pos_x = self.snake[-1].pos_x - self.snake[-1].velocity_x
                new_segment.pos_y = self.snake[-1].pos_y - self.snake[-1].velocity_y
                new_segment.velocity_x = self.snake[-1].velocity_x
                new_segment.velocity_y = self.snake[-1].velocity_y
                self.snake.append(new_segment)
                if len(self.snake) % 5 == 0:
                    self.time_step = self.time_step / 1.1
            self.draw_player()
            self.update_velocity()
            self.draw_fruit()
            self.loss_check()
            time.sleep(self.time_step)
            self.update()

    def loss_check(self):
        for i, segment in enumerate(self.snake):
            if not i == 0:
                if self.snake[0].pos_x == segment.pos_x and self.snake[0].pos_y == segment.pos_y:
                    new_segment = self.snake[0]
                    self.snake.clear()
                    self.snake.append(new_segment)
                    self.time_step = 0.1

    def draw_player(self):
        for segment in self.snake:
            self.create_rectangle(segment.pos_x * 25, segment.pos_y * 25,
                                  segment.pos_x * 25 + 25, segment.pos_y * 25 + 25,
                                  fill="white", outline="green")

    def draw_fruit(self):
        self.create_rectangle(self.fruit.pos_x * 25, self.fruit.pos_y * 25,
                              self.fruit.pos_x * 25 + 25, self.fruit.pos_y * 25 + 25,
                              fill="red")

    def key_pressed(self, event):
        if not self.has_key_been_pressed:
            if event.keysym == "w" or event.keysym == "Up":
                self.move_snake_up()
            if event.keysym == "a" or event.keysym == "Left":
                self.move_snake_left()
            if event.keysym == "s" or event.keysym == "Down":
                self.move_snake_down()
            if event.keysym == "d" or event.keysym == "Right":
                self.move_snake_right()
            self.has_key_been_pressed = True
        if event.keysym == "space":
            self.is_playing = True
            self.game_loop()

    def update_velocity(self):
        for i, segment in reversed(list(enumerate(self.snake))):
            if not i == 0:
                segment.velocity_x = self.snake[i - 1].velocity_x
                segment.velocity_y = self.snake[i - 1].velocity_y

    def move_snake_up(self):
        self.snake[0].move_up()

    def move_snake_down(self):
        self.snake[0].move_down()

    def move_snake_left(self):
        self.snake[0].move_left()

    def move_snake_right(self):
        self.snake[0].move_right()

    def clear_screen(self):
        self.delete("all")

