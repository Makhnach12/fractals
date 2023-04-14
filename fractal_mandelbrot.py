import pygame

import controller
import draw
from rectangle import Rectangle

SIZE = 600


def main():
    x, y = 0, 0
    scale = 150
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    draw.draw_mandelbrot(screen, (x, y), scale, 100, (-SIZE // 2, SIZE // 2), (-SIZE // 2, SIZE // 2))
    red_square = Rectangle(screen, 1, 1)
    red_square.output()

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         return
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #         x0, y0 = pygame.mouse.get_pos()
        #
        #         x = x0
        #         y = y0
        #         scale *= 2
        #
        #         now_mandelbrot = mandelbrot((x, y), scale, 100, (-SIZE // 2, SIZE // 2), (-SIZE // 2, SIZE // 2))
        #         for iterator in now_mandelbrot:
        #             draw_pixel(screen, iterator[0], iterator[1], iterator[2])
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:
        #             now_mandelbrot = mandelbrot((x, y), scale, 100,
        #                                         (red_square.rect.centery - SIZE // 2,
        #                                          red_square.rect.centery + 101 - SIZE // 2),
        #                                         (red_square.rect.centerx - SIZE // 2,
        #                                          red_square.rect.centerx + 101 - SIZE // 2))
        #             for iterator in now_mandelbrot:
        #                 draw_pixel(screen, iterator[0], iterator[1], iterator[2])
        #             red_square.rect.centerx += 1
        controller.control(red_square, screen, scale, [x, y])
        if red_square.is_moving:
            draw.draw_mandelbrot(screen, (x, y), scale, 100,
                                 (red_square.rect.centery - SIZE // 2,
                                  red_square.rect.centery + 101 - SIZE // 2),
                                 (red_square.rect.centerx - SIZE // 2,
                                  red_square.rect.centerx + 101 - SIZE // 2))
        red_square.moving()
        red_square.output()
        pygame.display.update()


if __name__ == "__main__":
    main()
