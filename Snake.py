import pygame
from pygame.locals import *
import pygame.gfxdraw

# Hàm vẽ hộp chạy trên bề mặt
def draw_box() :
    surface.fill((91, 162, 179))
    pygame.gfxdraw.box(surface, [rect_x, rect_y, 20, 20], [163, 67, 33])
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((91, 162, 179))
    rect_y = 100
    rect_x = 100
    pygame.gfxdraw.box(surface, [rect_x,rect_y,20,20], [163, 67, 33])

    pygame.display.flip()


    pygame.display.set_caption("Game Snake")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    rect_y -= 10
                    draw_box()
                if event.key == K_DOWN:
                    rect_y += 10
                    draw_box()
                if event.key == K_LEFT:
                    rect_x -= 10
                    draw_box()
                if event.key == K_RIGHT:
                    rect_x += 10
                    draw_box()
            elif event.type == QUIT:
                running = False

