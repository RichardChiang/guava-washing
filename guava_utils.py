import imutils, cv2
import numpy as np

class GuavaUtils:
    def __init__(self):
        self.crop_ratio = 0.32
        self.blur_kernel_size = (7,7)
        self.resize_width = 1200
        self.thresholds = [50, 0, 60, 0]
        self.color_space = "HSV"

    def resize_image(self, image):
        return imutils.resize(image, width=self.resize_width)

    def crop_image(self, image):
        h, w, _ = image.shape
        left, right = int(w*self.crop_ratio), int(w*(1-self.crop_ratio))
        cropped = image[0:h, left:right]

        return cropped

    def hsv_image(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def grayscale_image(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def blur_image(self, image):
        return cv2.GaussianBlur(image, self.blur_kernel_size, 0)

    def threshold_image(self, image, index):
        return cv2.threshold(image, self.thresholds[index], 255, cv2.THRESH_BINARY)[1]

    def invert_image(self, image):
        return cv2.bitwise_not(image)

    def preprocess(self, image):
        resized = self.resize_image(image)
        cropped = self.crop_image(resized)
        hsv_image = self.hsv_image(cropped)

        return hsv_image

    def postprocess(self, image, index):
        grayscaled = self.grayscale_image(image)
        threshed = self.threshold_image(grayscaled, index)
        # blurred = self.blur_image(grayscaled)

        return threshed

    def show_default(self, image):
        preprocessed = self.preprocess(image)
        processed = self.postprocess(preprocessed)

        cv2.imshow('Default Processed Image', processed)

    def filter_color(self, image, color_boundary):
        lower, upper = color_boundary

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)

        return output

    def display_results(self, window_name, image, text):
        org = (50, 50)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color = (0, 0, 255)
        thickness = 2

        cv2.putText(
            image,
            text,
            org,
            fontFace,
            fontScale,
            color,
            thickness
        )

        cv2.imshow(window_name, image)


