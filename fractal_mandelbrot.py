import pygame

import controller
import draw
import mandelbrot_set
from rectangle import Rectangle


def main():
    mandelbrot = mandelbrot_set.mandelbrot_set()
    pygame.init()
    screen = pygame.display.set_mode((mandelbrot.SIZE, mandelbrot.SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    draw.draw_mandelbrot_in_area(screen, (0, 0), mandelbrot.SCALE, mandelbrot.SIZE, (0, 0),
                                 mandelbrot.num_iterations, mandelbrot.radius, mandelbrot.z_0, mandelbrot.parameter)
    red_square = Rectangle(screen)
    red_square.output()

    while True:
        controller.control(red_square, screen, mandelbrot)
        if red_square.check_move():
            red_square.delete_rectangle(screen, mandelbrot)
        red_square.moving()
        red_square.output()
        pygame.display.update()


if __name__ == "__main__":
    main()
