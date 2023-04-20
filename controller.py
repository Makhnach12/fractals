import pygame

import rectangle
from draw import draw_mandelbrot, new_mandelbrot
from fractal_mandelbrot import SIZE, SCALE


def control(red_square: rectangle.Rectangle, screen, scale, coordinates):
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
                new_mandelbrot(screen, (red_square.rect.centerx / SCALE, red_square.rect.centery / SCALE), scale * 4.5, SIZE)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                red_square.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                red_square.is_moving_left = False
            elif event.key == pygame.K_DOWN:
                red_square.is_moving_down = False
            elif event.key == pygame.K_UP:
                red_square.is_moving_up = False
