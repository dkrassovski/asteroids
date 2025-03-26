import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius

        def draw(self, surface): 
            pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 2)

        def update(self, dt):
            self.x += self.velocity.x * dt
            self.y += self.velocity.y * dt