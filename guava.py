import cv2, imutils
import numpy as np

from guava_blob import BlobDetector
from guava_utils import GuavaUtils
from guava_tweaker import GuavaTweaker
from die_detector import DieDetector

def main():
    cap = cv2.VideoCapture(0)

    bd = BlobDetector()
    utils = GuavaUtils()
    dd = DieDetector()

    DEBUG = True
    WINDOW_NAME = 'image'

    cv2.namedWindow(WINDOW_NAME)

    tweaker = None
    if DEBUG:
        tweaker = GuavaTweaker(window_name=WINDOW_NAME)
        tweaker.debug()

    while(True):
        ret, frame = cap.read()

        viewable = utils.preprocess(frame)
        masked_images = dd.iterate_colors(viewable)

        if DEBUG:
            for i, threshold in enumerate(tweaker.threshold_names):
                t = cv2.getTrackbarPos(threshold, WINDOW_NAME)
                utils.thresholds[i] = t

        postprocessed_images = masked_images

        for i, image in enumerate(masked_images):
            postprocessed_images[i] = utils.postprocess(image, i)

        image = np.hstack(postprocessed_images)
        image = imutils.resize(image, width=1600)

        keypoints = bd.count_die(image)
        img_with_keypoints = bd.display_keypoints(image, keypoints)

        cv2.imshow(WINDOW_NAME, img_with_keypoints)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def ab_testing(img):
    h, w = img.shape

    top = np.empty(shape=(h,1))
    bot = np.empty(shape=(h,1))

    for i in range(1,11):
        baseline, diff = 70, 5
        threshold = baseline + diff * i

        thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]

        if i < 6: top = np.hstack((top, thresh))
        if i >= 6: bot = np.hstack((bot, thresh))

    img = np.vstack((top, bot))

    cv2.imshow('frame', img)

main()
