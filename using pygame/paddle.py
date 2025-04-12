import pygame

class Paddle(pygame.Rect):
    def __init__(self, width, height, screen_width):
        super().__init__((screen_width - width) // 2, 580, width, height)
        self.speed = 8

    def move(self, direction):
        if direction == "left" and self.left > 0:
            self.x -= self.speed
        elif direction == "right" and self.right < 800:
            self.x += self.speed