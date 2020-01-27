import cv2, imutils
import numpy as np
from guava_utils import GuavaUtils

class BlobDetector:
    def __init__(self):
        self.detector = self.init_detector()

    def init_detector(self):
        params = cv2.SimpleBlobDetector_Params()

        params.filterByColor = True
        params.blobColor = 255

        params.filterByInertia = True
        params.minInertiaRatio = 0.45

        return cv2.SimpleBlobDetector_create(params)

    def count_die(self, image):
        return self.detector.detect(image)

    def display_keypoints(self, image, keypoints):
        img_with_keypoints = cv2.drawKeypoints(
            image, keypoints,
            np.array([]), (0,0,255),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )
        cv2.imshow('Keypoint on Image', img_with_keypoints)

