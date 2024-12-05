# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *
from player import *
from asteroidfield import *

def main():
    
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!") 
                event.type == pygame.QUIT
                return
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()


        # limit the FPS to 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()