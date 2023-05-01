import pygame

import controller
import draw
import mandelbrot_set
from rectangle import Rectangle


def enter_characteristics():
    characters = [0 for i in range(5)]
    characters[0] = int(input('Введите N\n'))
    characters[1] = int(input('Введите радиус\n'))
    print('Введите действительную и мнимую части для z0')
    characters[2] = int(input('Re(z) = '))
    characters[3] = int(input('Im(z) = '))
    characters[4] = int(input('Введите а\n'))
    return characters


def main():
    characters = enter_characteristics()
    mandelbrot = mandelbrot_set.mandelbrot_set(characters[0], characters[1],
                                               characters[2], characters[3],
                                               characters[4])
    pygame.init()
    screen = pygame.display.set_mode((mandelbrot.SIZE, mandelbrot.SIZE))
    pygame.display.set_caption("Множество Мандельброта")
    screen.fill((0, 0, 0))
    draw.draw_mandelbrot_in_area(screen, (0, 0), mandelbrot.SCALE, mandelbrot.SIZE,
                                 mandelbrot.SIZE, (0, 0),
                                 mandelbrot.num_iterations, mandelbrot.radius,
                                 mandelbrot.z_0, mandelbrot.parameter)
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
