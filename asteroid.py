import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(150,75,0),(int(self.position.x), int(self.position.y)),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            asteroid1vec = self.velocity.rotate(random_angle)
            asteroid2vec = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
        
            # Create new asteroids
            Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
             # Set their velocities (step 6 and 7)
            Asteroid1.velocity = asteroid1vec * 1.2
            Asteroid2.velocity = asteroid2vec * 1.2
        
            # Add them to the same groups
            for group in self.groups():
                group.add(Asteroid1, Asteroid2)
