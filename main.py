# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *
from player import *

def main():
    
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        pygame.display.flip()
        Player.draw(screen)

        # limit the FPS to 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()