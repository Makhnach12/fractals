import pygame

import draw
import mandelbrot_set


class Rectangle:
    def __init__(self, screen):
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

    def delete_rectangle(self, screen, mandelbrot: mandelbrot_set.mandelbrot_set):
        draw.draw_mandelbrot_in_area(screen, (mandelbrot.x_0 + self.rect.centerx / mandelbrot.SCALE,
                                              mandelbrot.y_0 + self.rect.centery / mandelbrot.SCALE),
                                     mandelbrot.SCALE, 100, 1,
                                     (self.rect.centerx, self.rect.centery), mandelbrot.num_iterations,
                                     mandelbrot.radius, mandelbrot.z_0, mandelbrot.parameter)
        draw.draw_mandelbrot_in_area(screen, (mandelbrot.x_0 + self.rect.centerx / mandelbrot.SCALE,
                                              mandelbrot.y_0 + (self.rect.centery + 99) / mandelbrot.SCALE),
                                     mandelbrot.SCALE, 100, 1,
                                     (self.rect.centerx, self.rect.centery + 99), mandelbrot.num_iterations,
                                     mandelbrot.radius, mandelbrot.z_0, mandelbrot.parameter)
        draw.draw_mandelbrot_in_area(screen, (mandelbrot.x_0 + self.rect.centerx / mandelbrot.SCALE,
                                              mandelbrot.y_0 + self.rect.centery / mandelbrot.SCALE),
                                     mandelbrot.SCALE, 1, 100,
                                     (self.rect.centerx, self.rect.centery), mandelbrot.num_iterations,
                                     mandelbrot.radius, mandelbrot.z_0, mandelbrot.parameter)
        draw.draw_mandelbrot_in_area(screen, (mandelbrot.x_0 + (self.rect.centerx + 99) / mandelbrot.SCALE,
                                              mandelbrot.y_0 + self.rect.centery / mandelbrot.SCALE),
                                     mandelbrot.SCALE, 1, 100,
                                     (self.rect.centerx + 99, self.rect.centery), mandelbrot.num_iterations,
                                     mandelbrot.radius, mandelbrot.z_0, mandelbrot.parameter)

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
