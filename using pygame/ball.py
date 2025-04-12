import pygame
import random

class Ball(pygame.Rect):
    def __init__(self, radius):
        super().__init__(400 - radius, 300 - radius, radius * 2, radius * 2)
        self.dx = 5 * random.choice((1, -1))
        self.dy = -5

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def reset(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.dx = 5 * random.choice((1, -1))
        self.dy = -5