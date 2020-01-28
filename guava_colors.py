import numpy as np

class GuavaColors:
    def __init__(self):
        self.boundaries = self.color_boundaries()

    def numpy_boundaries(self, boundaries):
        return [np.array(bound, dtype = 'uint8') for bound in boundaries]

class HSVColors(GuavaColors):
    def __init__(self):
        super().__init__()
        self.color_space = "HSV"

    def color_space_boundaries(self):
        boundaries =[
            # light blue:
            ([82, 0, 70], [132, 180, 225]),
            # dark blue:
            ([107, 180, 70], [132, 255, 225]),
            # red:
            ([0, 120, 70], [20, 255, 225]),
            # green:
            ([40, 120, 70], [82, 255, 225]),
        ]
        return boundaries

    def color_boundaries(self):
        return [self.numpy_boundaries(bounds) for bounds in self.color_space_boundaries()]


class BGRColors(GuavaColors):
    def __init__(self):
        super().__init__()
        self.color_space = "BGR"

    def color_space_boundaries(self):
        boundaries =[
            # light blue: ([140, 98, 85], [149, 108, 96])
            ([100, 70, 60], [160, 130, 120]),
            # dark blue: ([101, 30, 4], [112, 50, 43])
            ([80, 20, 0], [112, 60, 60]),
            # red: ([0, 39, 186], [13, 52, 200])
            ([0, 20, 150], [40, 80, 220]),
            # green: ([48, 80, 5], [104, 118, 14])
            ([30, 60, 0], [90, 140, 50]),
        ]
        return boundaries

    def color_boundaries(self):
        return [self.numpy_boundaries(bounds) for bounds in self.color_space_boundaries()]

