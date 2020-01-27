import numpy as np

class GuavaColors:
    def __init__(self):
        self.boundaries = self.color_boundaries()

    # TODO: dynamically retrieve colors
    def die_colors(self):
        colors =[
            # light blue: ([140, 98, 85], [149, 108, 96])
            ([100, 70, 60], [160, 130, 120]),
            # dark blue: ([101, 30, 4], [112, 50, 43])
            ([80, 20, 0], [112, 60, 60]),
            # red: ([0, 39, 186], [13, 52, 200])
            ([0, 20, 150], [40, 80, 220]),
            # green: ([48, 80, 5], [104, 118, 14])
            ([30, 60, 0], [90, 140, 50]),
        ]

        return colors

    def color_boundaries(self):
        return [self.numpy_boundaries(bounds) for bounds in self.die_colors()]

    def numpy_boundaries(self, boundaries):
        return [np.array(bound, dtype = 'uint8') for bound in boundaries]

