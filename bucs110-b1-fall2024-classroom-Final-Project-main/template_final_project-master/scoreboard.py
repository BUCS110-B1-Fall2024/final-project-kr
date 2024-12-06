import pygame
import math
import random

class Scoreboard:
    def __init__(self, font_type='Arial', font_size=30, bold=True, color_one="black", color_two="red"):
        """Scoreboard for the player's health and score

        Args:
            font_type (str, optional): The font the scoreboard should write in. Defaults to 'Arial'.
            font_size (int, optional): The size of the scoreboard's font. Defaults to 30.
            bold (bool, optional): if the scoreboard text should be bold or not. Defaults to True.
            color_one (str, optional):the color of the text displaying the score. Defaults to "black".
            color_two (str, optional): the color of the text displaying the health. Defaults to "red".
        """
        self.font_type = font_type
        self.font_size = font_size
        self.bold = bold
        self.color_one = color_one
        self.color_two = color_two
        
        self.font = pygame.font.SysFont(font_type, font_size, bold=bold)

    def write(self, score, health):
        """Creates text displaying score and health

        Args:
            score (int): player's score
            health (int): player's health

        Returns:
            (tuple): returns a tuple containt the text for the player's score and the text for the player's health
        """
        score_text = self.font.render(f"Score: {score}", True, self.color_one)
        health_text = self.font.render(f"Health: {health}", True, self.color_two)
        
        return score_text, health_text