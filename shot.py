import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape,pygame.sprite.Sprite):
    def __init__(self,x,y, velocity):
        super().__init__(x,y,SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self,self.__class__.containers)
        self.velocity = velocity
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(int(self.position.x),int(self.position.y)),self.radius)
