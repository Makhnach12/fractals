from numba import njit


@njit(fastmath=True)
def mandelbrot_count(user_view, scale, size_x, size_y,
                     coordinates, num_iterations, radius, z_0, parameter):
    for j in range(size_y):
        b = (j / scale + user_view[1]) / (300 / parameter) - parameter
        for i in range(size_x):
            a = (i / scale + user_view[0]) / (300 / parameter) - parameter
            c = complex(a, b)
            z = z_0
            depth = 0
            for depth in range(num_iterations):
                z = z ** 5 + c
                if abs(z) > radius:
                    break
            if depth == num_iterations - 1:
                color = 100 * 2.55
            else:
                color = depth * 2.55
            yield i + coordinates[0], j + coordinates[1], (color, color, color)
