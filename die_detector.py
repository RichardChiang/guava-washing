import numpy as np
import cv2, imutils

from guava_colors import GuavaColors
from guava_utils import GuavaUtils

class DieDetector:
    def __init__(self):
        self.num_die = 4
        self.color_boundaries = GuavaColors().color_boundaries()
        self.guava_utils = GuavaUtils()

    def iterate_colors(self, image):
        images = []

        for boundary in self.color_boundaries:
            lower, upper = boundary

            mask = cv2.inRange(image, lower, upper)
            output = cv2.bitwise_and(image, image, mask = mask)

            images.append(output)

        return images
