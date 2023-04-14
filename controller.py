import pygame

import rectangle
from draw import draw_mandelbrot
from fractal_mandelbrot import SIZE


def control(red_square: rectangle.Rectangle, screen, scale, coordinates):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = pygame.mouse.get_pos()

            coordinates[0] = x0
            coordinates[1] = y0
            scale *= 2

            draw_mandelbrot(screen, tuple(coordinates), scale, 100, (-SIZE // 2, SIZE // 2), (-SIZE // 2, SIZE // 2))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                draw_mandelbrot(screen, tuple(coordinates), scale, 100,
                                (red_square.rect.centery - SIZE // 2,
                                 red_square.rect.centery + 101 - SIZE // 2),
                                (red_square.rect.centerx - SIZE // 2,
                                 red_square.rect.centerx + 101 - SIZE // 2))
                red_square.is_moving = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                draw_mandelbrot(screen, tuple(coordinates), scale, 100,
                                (red_square.rect.centery - SIZE // 2,
                                 red_square.rect.centery + 101 - SIZE // 2),
                                (red_square.rect.centerx - SIZE // 2,
                                 red_square.rect.centerx + 101 - SIZE // 2))
                red_square.is_moving = False
