from numba import njit


@njit(fastmath=True)
def mandelbrot_scale(user_view, scale, size, coordinates):
    for j in range(size):
        b = (j / scale + user_view[1]) / 150 - 2
        for i in range(size):
            a = (i / scale + user_view[0]) / 150 - 2
            c = complex(a, b)
            z = complex(0)
            depth = 0
            for depth in range(100):
                z = z ** 5 + c
                if abs(z) > 20:
                    break
            color = depth * 2.55
            yield i + coordinates[0], j + coordinates[1], (color, color, color)
