import pygame
from pygame import Surface, gfxdraw

import draw


class Rectangle:
    def __init__(self, screen, x_0, y_0):
        self.screen = screen
        self.image = pygame.image.load('pixilart-drawing-2.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 0
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_down = False
        self.is_moving_up = False

    def output(self):
        self.screen.blit(self.image, (self.rect.centerx, self.rect.centery))

    def delete_rectangle(self, screen, mandelbrot, num_iters):
        draw.draw_mandelbrot_in_area(screen, (mandelbrot.x_0 + self.rect.centerx / mandelbrot.SCALE
                                              , mandelbrot.y_0 + self.rect.centery / mandelbrot.SCALE),
                                     mandelbrot.SCALE, num_iters, (self.rect.centerx, self.rect.centery))

    def moving(self):
        if self.is_moving_right and self.rect.centerx < 499:
            self.rect.centerx += 1
        elif self.is_moving_left and self.rect.centerx > 0:
            self.rect.centerx -= 1
        elif self.is_moving_down and self.rect.centery < 499:
            self.rect.centery += 1
        elif self.is_moving_up and self.rect.centery > 0:
            self.rect.centery -= 1

    def check_move(self):
        return self.is_moving_right or self.is_moving_left \
                or self.is_moving_down or self.is_moving_up


