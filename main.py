import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()


    while (True):
        # Watch for OS quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill((0, 0, 0))

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return

        for item in drawable:
            item.draw(screen)

        # Flip the screen to another frame
        pygame.display.flip()
        # Calculate the "delta time" (used to compensate for slow frames)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
