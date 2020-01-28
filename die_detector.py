import numpy as np
import cv2, imutils

from guava_colors import HSVColors
from guava_utils import GuavaUtils
from guava_blob import BlobDetector

class DieDetector:
    def __init__(self):
        self.num_die = 4
        self.color_boundaries = HSVColors().color_boundaries()
        self.util = GuavaUtils()
        self.blob = BlobDetector()

    def iterate_colors(self, image):
        images = []
        die_counts = []

        for boundary in self.color_boundaries:
            filtered = self.util.filter_color(image, boundary)
            die_count = len(self.blob.count_die(filtered))

            images.append(filtered)
            die_counts.append(die_count)

        return (images, die_counts)
