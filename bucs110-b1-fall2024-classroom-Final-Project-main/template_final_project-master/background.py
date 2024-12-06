import pygame
import math
import random

class Background:
    def __init__(self, scale=(800, 600), img=r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\forest2_img.jpg"):
        """The background image object for the screen

        Args:
            scale (tuple, optional): The scale of the screen. Defaults to (800, 600).
            img (regexp, optional): The image the background is set to. Defaults to r"c:\Users\K\Desktop\gstuff\final-project-kr\bucs110-b1-fall2024-classroom-Final-Project-main\template_final_project-master\forest2_img.jpg".
        """
        self.scale = scale
        self.img = img
        
    def create_background(self):
        """Creates the background

        Returns:
            scaled_background (surface): the surface object of the scaled background image
        """
        background = pygame.image.load(self.img)
        scaled_background = pygame.transform.scale(background, self.scale)
        
        return scaled_background
        