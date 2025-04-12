import pygame

class Block(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)