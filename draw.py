from pygame import gfxdraw

from mandelbrot_counter import mandelbrot, mandelbrot_scale


def draw_pixel(screen, x, y, color):
    gfxdraw.pixel(screen, x, y, color)


def draw_mandelbrot(screen, user_view, scale, num_of_iterations, y_bords, x_bords):
    now_mandelbrot = mandelbrot(user_view, scale, num_of_iterations, y_bords, x_bords)
    for iterator in now_mandelbrot:
        draw_pixel(screen, iterator[0], iterator[1], iterator[2])


def new_mandelbrot(screen, user_view, scale, size):
    now_mandelbrot = mandelbrot_scale(user_view, scale, size)
    for iterator in now_mandelbrot:
        draw_pixel(screen, iterator[0], iterator[1], iterator[2])