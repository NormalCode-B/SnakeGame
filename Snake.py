import pygame
from pygame.locals import *
import pygame.gfxdraw
import time

# Cấu hình cho con rắn
class Snake:
    def __init__(self, parent_screen ):
        self.parent_screen = parent_screen
        self.y = 100
        self.x = 100
        self.direction = 'down'
    # Hàm vẽ con rắn trong màn hình
    def draw(self):
        # Màu của màn hình
        self.parent_screen.fill((91, 162, 179))
        # Hình dạng hộp con rắn
        pygame.gfxdraw.box(self.parent_screen, [self.x, self.y, 20, 20], [163, 67, 33])
        # Cập nhật hay hiển thị lên màn hình
        pygame.display.flip()

    # Các hàm dưới này để định nghĩa đường đi cho con rắn
    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"

    # Hàm này dùng để setup vị trí di chuyển của nó so với vị trí trước
    def walk(self):
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
            self.y += 10
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game Snake")
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((91, 162, 179))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.1)

if __name__ == "__main__":
    a = Game()
    a.run()