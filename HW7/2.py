img_path = 'img.jpeg'

from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
 
def find_point(p):
    rect = np.zeros((4, 2), dtype = "float32")
    s = p.sum(axis = 1)
    rect[0] = p[np.argmin(s)]
    rect[2] = p[np.argmax(s)]
    diff = np.diff(p, axis = 1)
    rect[1] = p[np.argmin(diff)]
    rect[3] = p[np.argmax(diff)]
 
    return rect

def transform(img, p):
    rect = find_point(p)
    (a, b, c, d) = rect
    w1 = np.sqrt(((c[0] - d[0]) ** 2) + ((c[1] - d[1]) ** 2))
    w2 = np.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))
    max_w = max(int(w1), int(w2))
    h1 = np.sqrt(((b[0] - c[0]) ** 2) + ((b[1] - c[1]) ** 2))
    h2 = np.sqrt(((a[0] - d[0]) ** 2) + ((a[1] - d[1]) ** 2))
    max_h = max(int(h1), int(h2))
    dst = np.array([[0, 0], [max_w - 1, 0], [max_w - 1, max_h - 1], [0, max_h - 1]], dtype = "float32")
    warped = cv2.warpPerspective(image, cv2.getPerspectiveTransform(rect, dst), (max_w, max_h))
 
    return warped

def get_res_camscanner(image):
    img = image.copy()
    r = img.shape[0] / 500.0
    img2 = img.copy()
    img = imutils.resize(img, height = 500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edge = cv2.Canny(gray, 75, 200)
    cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    img2 = transform(img2, screenCnt.reshape(4, 2) * r)
    
    return img2

