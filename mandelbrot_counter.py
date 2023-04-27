from numba import njit


@njit(fastmath=True)
def mandelbrot_count(user_view, scale, size, coordinates, num_iterations, radius, z_0, parameter):
    for j in range(size):
        b = (j / scale + user_view[1]) / (parameter * 75) - parameter
        for i in range(size):
            a = (i / scale + user_view[0]) / (parameter * 75) - parameter
            c = complex(a, b)
            z = complex(z_0)
            depth = 0
            for depth in range(num_iterations):
                z = z ** 5 + c
                if abs(z) > radius:
                    break
            color = depth * 2.55
            yield i + coordinates[0], j + coordinates[1], (color, color, color)
