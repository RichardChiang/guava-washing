import cv2
import numpy as np
from guava_blob import BlobDetector
from guava_utils import GuavaUtils

def main():
    cap = cv2.VideoCapture(0)
    bd = BlobDetector()
    utils = GuavaUtils()

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        viewable = utils.preprocess(frame)
        img = utils.postprocess(viewable)
        h, w = img.shape

        keypoints = bd.count_die(img)
        bd.display_keypoints(viewable, keypoints)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
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
