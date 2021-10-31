from threading import Thread
import cv2 as cv
from datetime import datetime

class VideoCaptureThread:
    """ Threaded VideoCapture from cv2
    """

    def __init__(self, src=0):
        self.cap = cv.VideoCapture(src)
        self.ret, self.frame = self.cap.read()
        self.stopped = False

    def start(self):
        #create thread and start executing
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