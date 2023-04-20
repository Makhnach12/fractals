import pygame

import controller
import draw
from rectangle import Rectangle

SIZE = 600
SCALE = 1


def main():
    x, y = 0, 0
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    draw.new_mandelbrot(screen, (x, y), SCALE, SIZE)
    red_square = Rectangle(screen, 1, 1)
    red_square.output()

    while True:
        controller.control(red_square, screen, SCALE, [x, y])
        if red_square.is_moving_right or red_square.is_moving_left \
                or red_square.is_moving_down or red_square.is_moving_up:
            draw.new_mandelbrot(screen, (red_square.rect.centerx, red_square.rect.centery), SCALE, 101)
        red_square.moving()
        red_square.output()
        pygame.display.update()


if __name__ == "__main__":
    main()
