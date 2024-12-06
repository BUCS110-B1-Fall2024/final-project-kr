import pygame
import math
import random

class Glock:
    def __init__(self, angle=0, img=r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\glock_img.png", scale=(100,100), position=(400,500)):
        """Creates glock obrect

        Args:
            angle (int, optional): Angle of glock's rotation. Defaults to 0.
            img (regexp, optional): Image of glock object. Defaults to r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\glock_img.png".
            scale (tuple, optional): Size of glock object. Defaults to (100,100).
            position (tuple, optional): Position of glock object. Defaults to (400,500).
        """
        self.img = img
        self.scale = scale
        self.position = position
        self.angle = angle
        
        self.glock = pygame.image.load(img)
        self.scaled_glock = pygame.transform.scale(self.glock, scale)
        self.glock_rect = self.scaled_glock.get_rect(center=position)
    def rotate(self, value=0.1):
        """_summary_

        Args:
            value (float, optional): the value by which the glock's angle increases or decreases when arrow keys are pressed. Defaults to 0.1.

        Returns:
            tuple: tuple containting the rotated glock surface, the rectangle for that surface, and the glock object's current angle
        """
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.angle -= value
        if key[pygame.K_LEFT]:
            self.angle += value
        
        if self.angle > 180:
            self.angle = 180
        elif self.angle < 0:
            self.angle = 0
        
        rotating_glock = pygame.transform.rotate(self.scaled_glock, self.angle)
        rotated_rect = rotating_glock.get_rect(center=(self.glock_rect.center))
        
        return (rotating_glock, rotated_rect, self.angle)