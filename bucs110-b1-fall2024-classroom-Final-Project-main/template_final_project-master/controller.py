import pygame
import math
import random
from glock import Glock
from background import Background
from bullet import Bullet
from bird import Bird
from scoreboard import Scoreboard

class Controller:
    def __init__(self):
        """creates controller object
        """
        pass
    def mainloop(self):
        """main gameplay loop
        """
        
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        
        forest = Background()
        forest_screen = forest.create_background()
        
        gun = Glock()
        bullet = Bullet()
        birds = Bird()
        scoreboard = Scoreboard()
        
        health = 5
        score = 0
        max_speed = 1
        max_opportunity = 50
        max_spawn = 5
        
        scores_list = [[5, 0.5, -5, 1], 
                    [10, 0.5, -5, 1], 
                    [20, 0.5, -10, 1], 
                    [30, 1, -5, 2], 
                    [40, 0.5, -5, 0], 
                    [50, 0.5, -5, 0]]
        
        running = True
        while running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            rotating_glock, rotating_rect, angle = gun.rotate()
            
            bullet_list = bullet.shoot(750, rotating_rect.centerx, rotating_rect.centery, 40, 1, 2, current_time, angle, (800,600))
            
            birds_list, health = birds.rain(health, max_speed, max_opportunity, max_spawn)
            
            for bullet_item in bullet_list[:]:
                for bird_item in birds_list[:]:
                    if bullet_item[0].colliderect(bird_item[2]):
                        bullet_list.remove(bullet_item)
                        birds_list.remove(bird_item)
                        birds.spawn -= 1
                        score += 1
                        print("You hit a bird! Current score: ", score)
                        

            for score_items in scores_list:
                if score == score_items[0]:
                    max_speed += score_items[1]
                    max_opportunity += score_items[2]
                    max_spawn += score_items[3]
                    score_items[0]= -100
                    print("speed: ", max_speed, "opportunity: ", max_opportunity, "spawn: ", max_spawn)
            
            score_text, health_text = scoreboard.write(score, health)
            
            screen.blit(forest_screen, (0,0))
            
            for bird_item in birds_list[:]:
                screen.blit(bird_item[1], bird_item[2])
            
            for bullet_item in bullet_list[:]:
                screen.blit(bullet_item[3], bullet_item[0])
                
            screen.blit(rotating_glock, rotating_rect)
            
            screen.blit(score_text, (50,50))
            screen.blit(health_text, (50, 100))
            
            if health <= 0:
                screen.fill("black")
                end_text = scoreboard.font.render(f"Game over! Your score is {score}", True, "white")
                screen.blit(end_text, ((800-end_text.get_width())/2, 300))
            
            pygame.display.flip()
        pygame.quit()
        
