# Boris Rendón y Maite de la Roca

from threading import Thread
import cv2 as cv
import numpy as np

class VideoCaptureThread:
    """ Threaded VideoCapture from opencv
    """
    def __init__(self, src=0):
        self.cap = cv.VideoCapture(src)
        self.ret, self.frame = self.cap.read()
        self.stopped = False

    def start(self):
        Thread(target=self.capture, args=()).start()
        return self

    def capture(self):
        while not self.stopped:
            if not self.ret:
                self.stop()
            else:
                self.ret, self.frame = self.cap.read()

    def stop(self):
        self.stopped = True

def template_match(frame, template, w, h):
    """ Implement template matching from opencv
    Args: 
        frame (numpy array): Source image
        template (numpy array): Template image
        width (int): Width of the template image
        height (int): Height of the template image
    Returns:
        Creates rectange where it detects the logo
    """
    imageGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(imageGray, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.5)

    for pt in zip(*loc[::-1]):
        cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

def pyramid(img, scale=0.75, min_size=(50, 50)):
    ''' Build a pyramid for an image until min_size dimensions are reached
    Args: 
        img (numpy array): Source image
        scale (float): Scaling factor
        min_size (tuple): Size of pyramid
    Returns:
        Pyramid generator
    '''
    yield img
    
    while True:
        img = cv.resize(img, None,fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)
        if ((img.shape[0]<min_size[0]) and img.shape[1]<min_size[1]):
            break
        yield img

def readThread(source=0):
    """Threading for reading the video
    Args: 
        source (int): Source of the video to be captured
    Returns:
        Reads video and detects logo putting a rectangle on it
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
    readThread(filename)