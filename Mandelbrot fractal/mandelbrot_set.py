
class mandelbrot_set:
    def __init__(self, num_iters, radius, re_z_0, im_z_0, parameter):
        self.SIZE = 600
        self.SCALE = 1
        self.x_0 = 0
        self.y_0 = 0
        self.num_iterations = num_iters
        self.coords_history = []
        self.radius = radius
        self.z_0 = complex(re_z_0, im_z_0)
        self.parameter = parameter






