import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots,updateable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = 0
    score_increment = 10
    font = pygame.font.Font(None, 36)
    
  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updateable.update(dt)
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                print(f"Score: {score}")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    score += score_increment
                    asteroid.split()
                    shot.kill()
                    
        

        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
            score_text = font.render(f'Score: {score}', True, (255,255,255))
            screen.blit(score_text, (10,10))
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

