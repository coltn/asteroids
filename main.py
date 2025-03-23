import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from player import Player


def main():
    print("Starting Asteroids!")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while (True):
        # Watch for OS quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)

        # Flip the screen to another frame
        pygame.display.flip()
        # Calculate the "delta time" (used to compensate for slow frames)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
