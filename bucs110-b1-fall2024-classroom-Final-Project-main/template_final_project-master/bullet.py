import pygame
import random
import math
from glock import Glock

class Bullet:
    def __init__(self, img=r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\bullet_img.png", scale=(25,25)):
        """Bullet object

        Args:
            img (regexp, optional): The bullet image. Defaults to r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\bullet_img.png".
            scale (tuple, optional): The bullet's size. Defaults to (25,25).
        """
        self.img = img
        self.scale = scale
        
        self.bullet = pygame.image.load(self.img)
        self.scaled_bullet = pygame.transform.scale(self.bullet, self.scale)
        self.bullet_list = []
        self.last_bullet_time = 0
    def shoot(self, delay, glock_center_x, glock_center_y, distance, sign_multiplyer, speed, current_time, angle, scale):
        """Shoots the bullet when player presses space

        Args:
            delay (int): The time delay between bullets firing
            glock_center_x (int): The center x value for the glock
            glock_center_y (int): The center y value for the glock
            distance (int): The distance between the bullet spawn position and the center of the glock 
            sign_multiplyer (float): The multiplies a value by which the glock center value should be offset based on the glock's rotation so the bullet angle is correct
            speed (int): bullet movement speed
            current_time (float): time on the pygame's clock
            angle (float): glock's angle
            scale (int): screen scale

        Returns:
            bullet_list(list): list of currently spawned bullet objects onscreen
        """
        if angle > 120:
            sign_multiplyer = -sign_multiplyer-0.2
        elif sign_multiplyer < 120:
            sign_multiplyer= sign_multiplyer
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and (current_time - self.last_bullet_time >= delay):
            bullet_x_trig = math.cos(math.radians(angle)) * speed
            bullet_y_trig = math.sin(math.radians(angle)) * speed
            
            bullet_x = (glock_center_x-5*sign_multiplyer) + math.cos(math.radians(angle)) * distance * sign_multiplyer
            bullet_y = (glock_center_y-25*sign_multiplyer) - math.sin(math.radians(angle)) * distance * sign_multiplyer
           
            
            bullet_rect = self.scaled_bullet.get_rect(center=(bullet_x, bullet_y))
            rotated_bullet = pygame.transform.rotate(self.scaled_bullet, angle)
            rotated_bullet_rect = rotated_bullet.get_rect(center=(bullet_rect.center))
            
            self.bullet_list.append([rotated_bullet_rect, bullet_x_trig, bullet_y_trig, rotated_bullet])
            
            self.last_bullet_time = current_time
            
        for bullet_item in self.bullet_list[:]:
                bullet_item[0].x += bullet_item[1]
                bullet_item[0].y -= bullet_item[2]
                if bullet_item[0].x < 0 or bullet_item[0].x > scale[0] or bullet_item[0].y < 0 or bullet_item[0].y > scale[1]:
                        self.bullet_list.remove(bullet_item)
                        
        return self.bullet_list