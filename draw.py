from pygame import gfxdraw

from mandelbrot_counter import mandelbrot_count


def draw_mandelbrot_in_area(screen, user_view, scale, size, coordinates, num_iterations, radius, z_0, parameter):
    now_mandelbrot = mandelbrot_count(user_view, scale, size, coordinates, num_iterations, radius, z_0, parameter)
    for iterator in now_mandelbrot:
        gfxdraw.pixel(screen, iterator[0], iterator[1], iterator[2])
