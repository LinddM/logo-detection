# no hay que hacer sliding window
import cv2 as cv
from video import *

def img_annotate(img, text):
    """ Annotate an image with text
    """
    cv.putText(img, text,(10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 0))
    # # Maybeee
    # PONER ACA EL TEMPLATE MATCHING (CUADRITO VERDE)
    # HACER ACA LAS PIRAMIDES
    return img

def captureThread(source=0):
    """
    """

    capThreaded = VideoCaptureThread(source).start()
    cps = CountsPerSec().start()

    while True:
        frame = capThreaded.frame
        if not capThreaded.ret or cv.waitKey(1) == ord("q"):
            capThreaded.stop()
            break
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
        
        cv.imshow("CAPTURE_THREAD", frame)
        cps.increment()

if __name__ == '__main__':
    filename = 0
    
    captureThread(filename)

##### Template matching

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('lenna.png',0)
# img2 = img.copy()
# template = cv.imread('lenna_por.png',0)
# w, h = template.shape[::-1]
# # All the 6 methods for comparison in a list
# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#     # Apply template Matching
#     res = cv.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv.rectangle(img,top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()