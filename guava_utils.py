import imutils, cv2

class GuavaUtils:
    def __init__(self):
        self.crop_ratio = 0.2
        self.blur_kernel_size = (7,7)
        self.resize_width = 600

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

    def preprocess(self, image):
        resized = self.resize_image(image)
        cropped = self.crop_image(resized)

        return cropped

    def postprocess(self, image):
        grayscaled = self.grayscale_image(image)
        blurred = self.blur_image(grayscaled)

        return blurred

    def show_default(self, image):
        preprocessed = self.preprocess(image)
        processed = self.postprocess(preprocessed)

        cv2.imshow('Default Processed Image', processed)
