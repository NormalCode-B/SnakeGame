import pygame
from pygame.locals import *
import pygame.gfxdraw
import time

size = 20

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = size * 4
        self.y = size * 4
    def draw(self):
        pygame.gfxdraw.filled_circle(self.parent_screen, self.x, self.y, 7, [207, 4, 4])
        pygame.display.flip()

# Cấu hình cho con rắn
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.y = [size]*length
        self.x = [size]*length

        self.direction = 'down'
    # Hàm vẽ con rắn trong màn hình
    def draw(self):
        # Màu của màn hình
        self.parent_screen.fill((91, 162, 179))
        for i in range(self.length):
            # Hình dạng hộp con rắn
             pygame.gfxdraw.rectangle(self.parent_screen, [self.x[i], self.y[i], 18, 18], [115, 15, 111])
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
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= size
        if self.direction == "down":
            self.y[0] += size
        if self.direction == "left":
            self.x[0] -= size
        if self.direction == "right":
            self.x[0] += size

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game Snake")
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((91, 162, 179))
        self.snake = Snake(self.surface,7)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

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

            self.play()
            time.sleep(0.2)

if __name__ == "__main__":
    a = Game()
    a.run()