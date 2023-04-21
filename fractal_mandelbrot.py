import pygame

import controller
import draw
import mandelbrot_set
from rectangle import Rectangle


def main():
    mandelbrot = mandelbrot_set.mandelbrot_set()
    x, y = 0, 0
    pygame.init()
    screen = pygame.display.set_mode((mandelbrot.SIZE, mandelbrot.SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    draw.new_mandelbrot(screen, (x, y), mandelbrot.SCALE, mandelbrot.SIZE, (0, 0))
    red_square = Rectangle(screen, 1, 1)
    red_square.output()

    while True:
        controller.control(red_square, screen, mandelbrot, [x, y])
        if red_square.is_moving_right or red_square.is_moving_left \
                or red_square.is_moving_down or red_square.is_moving_up:
            draw.new_mandelbrot(screen, (mandelbrot.x_0 + red_square.rect.centerx / mandelbrot.SCALE
                                         , mandelbrot.y_0 + red_square.rect.centery / mandelbrot.SCALE),
                                mandelbrot.SCALE, 100, (red_square.rect.centerx, red_square.rect.centery))
        red_square.moving()
        red_square.output()
        pygame.display.update()


if __name__ == "__main__":
    main()
