from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 51)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        asteroid_child_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_child_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_child_1.velocity = new_velocity_1 * 1.2
        asteroid_child_2.velocity = new_velocity_2 * 1.2
