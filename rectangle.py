import pygame
from pygame import Surface, gfxdraw


class Rectangle:
    def __init__(self, screen, x_0, y_0):
        self.screen = screen
        self.image = pygame.image.load('pixilart-drawing-2.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 0
        self.is_moving = False

    def output(self):
        self.screen.blit(self.image, (self.rect.centerx, self.rect.centery))

    def moving(self):
        if self.is_moving:
            self.rect.centerx += 1

