# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = float(2)
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    field = AsteroidField()
    Shot.containers = (bullets, updateable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        for obj in updateable:
            obj.update(dt)
        for obj in asteroids:
            if obj.collide(player):
                exit("Game over!")
        for obj in asteroids:
            for shot in bullets:
                if obj.collide(shot):
                    obj.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)

if __name__ == "__main__":
    main()