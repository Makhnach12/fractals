import pygame

import mandelbrot_set
import rectangle
from draw import new_mandelbrot


def control(red_square: rectangle.Rectangle, screen, mandelbrot: mandelbrot_set.mandelbrot_set, coordinates):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                red_square.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                red_square.is_moving_left = True
            elif event.key == pygame.K_DOWN:
                red_square.is_moving_down = True
            elif event.key == pygame.K_UP:
                red_square.is_moving_up = True
            elif event.key == pygame.K_RETURN:
                mandelbrot.x_0 += red_square.rect.centerx / mandelbrot.SCALE
                mandelbrot.y_0 += red_square.rect.centery / mandelbrot.SCALE
                mandelbrot.SCALE *= 6
                new_mandelbrot(screen, (mandelbrot.x_0,
                                        mandelbrot.y_0),
                               mandelbrot.SCALE,
                               mandelbrot.SIZE, (0, 0))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                red_square.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                red_square.is_moving_left = False
            elif event.key == pygame.K_DOWN:
                red_square.is_moving_down = False
            elif event.key == pygame.K_UP:
                red_square.is_moving_up = False
