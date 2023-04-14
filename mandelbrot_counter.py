from numba import njit

from fractal_mandelbrot import SIZE


@njit(fastmath=True)
def mandelbrot(user_view, scale, num_of_iterations, y_bords, x_bords):
    for y in range(y_bords[0] + user_view[1], y_bords[1] + user_view[1]):
        for x in range(x_bords[0] + user_view[0], x_bords[1] + user_view[0]):
            a = x / scale
            b = y / scale
            c = complex(a, b)
            z = complex(0)
            n = 0
            for n in range(num_of_iterations):
                z = z ** 5 + c
                if abs(z) > 100:
                    break
            color = n * 2.55
            yield x + SIZE//2 - user_view[0], y + SIZE//2 - user_view[1], (color, color, color)