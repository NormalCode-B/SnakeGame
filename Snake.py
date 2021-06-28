import pygame
from  pygame.locals import *
if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))
    surface.fill((91, 162, 179))
    pygame.display.flip()
    pygame.display.set_caption("Game Snake")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

