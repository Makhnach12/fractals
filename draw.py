from pygame import gfxdraw

from mandelbrot_counter import mandelbrot_count


def draw_pixel(screen, x, y, color):
    gfxdraw.pixel(screen, x, y, color)


def draw_mandelbrot_in_area(screen, user_view, scale, size, coordinates):
    now_mandelbrot = mandelbrot_count(user_view, scale, size, coordinates)
    for iterator in now_mandelbrot:
        draw_pixel(screen, iterator[0], iterator[1], iterator[2])
