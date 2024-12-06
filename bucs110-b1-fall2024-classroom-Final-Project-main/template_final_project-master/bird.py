import pygame
import math
import random

class Bird:
    def __init__(self, bird_image_list=[r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\duck_img.png", 
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\eagle_img.png",
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\owl_img.png", 
                       r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\brown_bird_img.png"], scale=(100,100)):
        """bird object

        Args:
            bird_image_list (list, optional): list of images for the birds to spawn as. Defaults to [r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\duck_img.png", r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\eagle_img.png", r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\owl_img.png", r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\brown_bird_img.png"].
            scale (tuple, optional): bird object scale. Defaults to (100,100).
        """
        self.bird_image_list = bird_image_list
        self.scale = scale
        
        self.spawn = 0
        self.bird_list = []
    def rain(self, health, max_speed, max_opportunity, max_spawn, screen_scale=(800,600)):
        """Causes birds to rain (spawn at top of screen and move downwards)

        Args:
            health (int): player's health
            max_speed (float): the maximum speed at which the bird moves down that the bird can spawn withh
            max_opportunity (int): the end value for the range in which a random number is generated. if that random number is 1 the bird can move
            max_spawn (int): the maximum number of bird which can be onscreen at a time
            screen_scale (tuple, optional): the screen's scale. Defaults to (800,600).

        Returns:
            (tuple): tuple containing a list of the bird objects onscreen and the player's health
        """
        if (random.randint(1, 2500) == 1) and self.spawn < max_spawn:
                bird = pygame.image.load(self.bird_image_list[random.randint(0, len(self.bird_image_list)-1)])
                scaled_bird = pygame.transform.scale(bird, self.scale)
                bird_rect = scaled_bird.get_rect(center=(random.randint(100,screen_scale[0]-100), 50))
                bird_speed = random.uniform(0.5, max_speed)
                self.bird_list.append([bird, scaled_bird, bird_rect, bird_speed])
                self.spawn += 1
        for bird_item in self.bird_list[:]:
            if (random.randint(1, max_opportunity) == 1):
                bird_item[2].y += bird_item[3]
            if bird_item[2].y > screen_scale[1]:
                self.bird_list.remove(bird_item)
                self.spawn -=1
                health -= 1
                print(health)
        
        return self.bird_list, health