import pygame
import math
import random

###Graders! Ignore this file. This is a test file I used to develop the game's functionality before I organized the code into classes.

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    
    font = pygame.font.SysFont('Arial', 30, bold=True)
    
    background = pygame.image.load(r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\forest2_img.jpg")
    background = pygame.transform.scale(background, (800,600))
    
    
    glock = pygame.image.load(r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\glock_img.png")
    glock_scale = pygame.transform.scale(glock, (100, 100))
    glock_rect = glock_scale.get_rect(center=(400, 500))
    
    bullet = pygame.image.load(r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\bullet_img.png")
    bullet_scale = pygame.transform.scale(bullet, (25,25))
    
    bird_image_list = [r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\duck_img.png", 
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\eagle_img.png",
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\owl_img.png", 
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\brown_bird_img.png"]
    
    bird_list = []
    
    angle = 0.1
    speed = 2
    bullet_list = []
    
    last_bullet_time = 0
    delay = 750
    
    score = 0
    scores_list = [[5, 1.5, 45, 6], [10, 2, 40, 7], [20, 2.5, 30, 8], [30, 3.5, 25, 10], [40, 4, 20, 10], [50, 4.5, 15, 10]]
    health = 5
    
    max_speed = 1
    max_opportunity = 50
    spawn = 0
    max_spawn = 5
    clock = pygame.time.Clock()
    running = True
    
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        if (random.randint(1, 2500) == 1) and spawn < max_spawn:
                bird = pygame.image.load(bird_image_list[random.randint(0, len(bird_image_list)-1)])
                bird_scale = pygame.transform.scale(bird, (100,100))
                bird_rect = bird_scale.get_rect(center=(random.randint(100,700), 50))
                bird_speed = random.uniform(0.5, max_speed)
                bird_list.append([bird, bird_scale, bird_rect, bird_speed])
                spawn += 1
        

        for bird_item in bird_list[:]:
            if (random.randint(1, max_opportunity) == 1):
                bird_item[2].y += bird_item[3]
            if bird_item[2].y > 600:
                bird_list.remove(bird_item)
                spawn -=1
                health -= 1
        
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            angle -= 0.1
        if key[pygame.K_LEFT]:
            angle += 0.1

        
        rotating_glock = pygame.transform.rotate(glock_scale, angle)
        rotated_rect = rotating_glock.get_rect(center=(glock_rect.center))
                    
        if angle > 180:
            angle = 180
        elif angle < 0:
            angle = 0
        
        sign_multiplyer = 1
        if angle > 120:
            sign_multiplyer = -1.2
        elif sign_multiplyer < 120:
            sign_multiplyer= 1

        if key[pygame.K_SPACE] and (current_time - last_bullet_time >= delay):
            bullet_x_trig = math.cos(math.radians(angle)) * speed
            bullet_y_trig = math.sin(math.radians(angle)) * speed
            
            bullet_x = (glock_rect.centerx-5*sign_multiplyer) + math.cos(math.radians(angle)) * 40 * sign_multiplyer
            bullet_y = (glock_rect.centery-25*sign_multiplyer) - math.sin(math.radians(angle)) * 40 * sign_multiplyer
           
            
            bullet_rect = bullet_scale.get_rect(center=(bullet_x, bullet_y))
            rotated_bullet = pygame.transform.rotate(bullet_scale, angle)
            rotated_bullet_rect = rotated_bullet.get_rect(center=(bullet_rect.center))
            
            bullet_list.append([rotated_bullet_rect, bullet_x_trig, bullet_y_trig, rotated_bullet])
            
            last_bullet_time = current_time
        
        for bullet_item in bullet_list[:]:
            for bird_item in bird_list[:]:
                if bullet_item[0].colliderect(bird_item[2]):
                    bullet_list.remove(bullet_item)
                    bird_list.remove(bird_item)
                    spawn -= 1
                    score += 1
                    print("You hit a bird! Current score: ", score)
                    
        for score_items in scores_list[:]:
            if score == score_items[0]:
                max_speed = score_items[1]
                max_opportunity = score_items[2]
                max_spawn = score_items[3]
            
        for bullet_item in bullet_list[:]:
            bullet_item[0].x += bullet_item[1]
            bullet_item[0].y -= bullet_item[2]
            if bullet_item[0].x < 0 or bullet_item[0].x > 800 or bullet_item[0].y < 0 or bullet_item[0].y > 600:
                    bullet_list.remove(bullet_item)
            
        screen.blit(background, (0,0))
        
        for bird_item in bird_list[:]:
            screen.blit(bird_item[1], bird_item[2])
        
        for bullet_item in bullet_list[:]:
            screen.blit(bullet_item[3], bullet_item[0])
        
        screen.blit(rotating_glock, rotated_rect)
        
        score_text = font.render(f"Score: {score}", True, "black")
        screen.blit(score_text, (50,50))
        
        health_text = font.render(f"Health: {health}", True, "red")
        screen.blit(health_text, (50, 100))
        
        if health <= 0:
            screen.fill("black")
            end_text = font.render(f"Game over! Your score is {score}", True, "white")
            screen.blit(end_text, ((800-end_text.get_width())/2, 300))

        pygame.display.flip()
    pygame.quit()
main()