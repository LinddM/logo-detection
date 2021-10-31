# # no hay que hacer sliding window
from video import CountsPerSec, VideoCaptureThread
import cv2 as cv
import numpy as np

def template_match(frame, template, w, h):
    """ Annotate an image with text
    """
    imageGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(imageGray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.4)

    for pt in zip(*loc[::-1]):
        cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)

def captureThread(source=0):
    """
    """

    template = cv.imread('Logo-UFM-50-anios-01-2.png', 0)
    w, h = template.shape[::-1]
    capThreaded = VideoCaptureThread(source).start()
    cps = CountsPerSec().start()

    while True:
        frame = capThreaded.frame
        if not capThreaded.ret or cv.waitKey(1) == ord("q"):
            capThreaded.stop()
            break
        
        temp_small = cv.resize(template, (618, 584), interpolation=cv.INTER_LINEAR)
        template_match(frame, temp_small, w, h)
        cv.imshow("CAPTURE_THREAD", frame)


if __name__ == '__main__':
    filename = 0
    
    captureThread(filename)