# # no hay que hacer sliding window
from video import VideoCaptureThread
import cv2 as cv
import numpy as np

def template_match(frame, template, w, h):
    """ 
    """
    imageGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(imageGray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.5)

    for pt in zip(*loc[::-1]):
        cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

def pyramid(img, scale=0.7, min_size=(50, 50)):
    yield img
    
    while True:
        img = cv.resize(img, None,fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)
        if ((img.shape[0]<min_size[0]) and img.shape[1]<min_size[1]):
            break
        yield img

def captureThread(source=0):
    """
    """
    template = cv.resize(cv.imread('Logo-UFM-50-anios-01-2.png', 0), (618, 584), interpolation=cv.INTER_LINEAR)
    capThreaded = VideoCaptureThread(source).start()
    while True:
        frame = capThreaded.frame
        if not capThreaded.ret or cv.waitKey(1) == ord("q"):
            capThreaded.stop()
            break
        
        for temp in pyramid(template):
            w, h = temp.shape[::-1]
            template_match(frame, temp, w, h)
        cv.imshow("Logo detection", frame)


if __name__ == '__main__':
    filename = 0
    captureThread(filename)