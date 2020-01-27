import imutils, cv2

class GuavaUtils:
    def __init__(self):
        self.crop_ratio = 0.32
        self.blur_kernel_size = (3,3)
        self.resize_width = 1200
        self.thresholds = [21, 0, 0, 0]

    def resize_image(self, image):
        return imutils.resize(image, width=self.resize_width)

    def crop_image(self, image):
        h, w, _ = image.shape
        left, right = int(w*self.crop_ratio), int(w*(1-self.crop_ratio))
        cropped = image[0:h, left:right]

        return cropped

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

        return cropped

    def postprocess(self, image, index):
        grayscaled = self.grayscale_image(image)
        # blurred = self.blur_image(cropped)
        threshed = self.threshold_image(grayscaled, index)

        return threshed

    def show_default(self, image):
        preprocessed = self.preprocess(image)
        processed = self.postprocess(preprocessed)

        cv2.imshow('Default Processed Image', processed)

    def filter_color(self, image, color_boundary):
        lower, upper = color_boundary

        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)

        return ouput
