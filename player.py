import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.__class__.containers)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED*dt)
    
    def update(self, dt):
        self.timer -= dt
        if self.timer <0:
            self.timer = 0
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot_position = pygame.Vector2(self.position)
        shot_velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED

        Shot(shot_position.x, shot_position.y, shot_velocity)

        
    